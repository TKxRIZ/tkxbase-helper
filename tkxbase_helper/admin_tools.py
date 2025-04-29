import os
import json
import hashlib
import getpass
from colorama import Fore, Style
from datetime import datetime

class AdminPWManager:
    """
    Erweiterter AdminPWManager mit Lockout, farbigen Logs, Passwort-Reset und Exception-Handling.
    Verwaltet das Setzen, Prüfen und Zurücksetzen eines Admin-Passworts mit SHA-256-Hashing.
    """

    def __init__(self, config_file=".admin_config.json", max_attempts=3):
        """
        Initialisiert den AdminPWManager.

        :param config_file: Pfad zur JSON-Datei, in der das Passwort gespeichert wird.
        :param max_attempts: Maximale Anzahl erlaubter Fehlversuche vor Sperrung.
        """
        self.config_file = config_file
        self.success_message = "[SUCCESS] Passwort korrekt."
        self.fail_message = "[ERROR] Falsches Passwort."
        self.max_attempts = max_attempts
        self.attempts = 0
        self.locked = False

    def hash_password(self, password):
        """
        Hasht ein Passwort mit SHA-256.

        :param password: Klartext-Passwort.
        :return: Passwort-Hash als Hex-String.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def _log(self, message, level="info"):
        """
        Gibt eine farbige Log-Nachricht mit Zeitstempel aus.

        :param message: Die Nachricht.
        :param level: "info", "success", "warning", "error".
        """
        color = {
            "info": Fore.CYAN,
            "success": Fore.GREEN,
            "warning": Fore.YELLOW,
            "error": Fore.RED
        }.get(level, Fore.WHITE)
        now = datetime.now()
        time_stamp = f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] "
        print(f"{color}{time_stamp}[AdminPWManager] {message}{Style.RESET_ALL}")

    def set_admin_password(self, force_reset=False):
        """
        Setzt ein neues Admin-Passwort.

        :param force_reset: Erzwingt das Zurücksetzen auch wenn ein Passwort existiert.
        """
        try:
            if os.path.exists(self.config_file) and not force_reset:
                self._log("Admin-Passwort existiert bereits.", "info")
                return

            pw1 = getpass.getpass("Neues Admin-Passwort eingeben: ")
            pw2 = getpass.getpass("Passwort wiederholen: ")
            if pw1 != pw2:
                self._log("Passwörter stimmen nicht überein.", "error")
                return

            hashed = self.hash_password(pw1)
            with open(self.config_file, "w") as f:
                json.dump({"admin_password": hashed}, f)

            self._log("Admin-Passwort wurde gesetzt!", "success")
        except Exception as e:
            self._log(f"Fehler beim Setzen des Passworts: {e}", "error")

    def reset_admin_password(self):
        """
        Setzt das Admin-Passwort zurück, indem die gespeicherte Passwortdatei gelöscht wird.
        """
        try:
            if os.path.exists(self.config_file):
                os.remove(self.config_file)
                self._log("Admin-Passwort wurde zurückgesetzt.", "warning")
            else:
                self._log("Kein Admin-Passwort zum Zurücksetzen gefunden.", "info")
        except Exception as e:
            self._log(f"Fehler beim Zurücksetzen des Passworts: {e}", "error")

    def check_admin_password(self):
        """
        Fragt das Admin-Passwort ab und prüft auf Richtigkeit.
        Sperrt nach zu vielen Fehlversuchen.

        :return: True bei Erfolg, False sonst.
        """
        if self.locked:
            self._log("Zu viele Fehlversuche. Zugang gesperrt!", "error")
            return False

        try:
            if not os.path.exists(self.config_file):
                self._log("Kein Admin-Passwort gesetzt!", "error")
                return False

            with open(self.config_file, "r") as f:
                config = json.load(f)

            stored_hash = config.get("admin_password")
            if not stored_hash:
                self._log("Keine Passwort-Hash gefunden.", "error")
                return False

            for attempt in range(self.max_attempts):
                entered_pw = getpass.getpass("Admin-Passwort eingeben: ")
                entered_hash = self.hash_password(entered_pw)

                if entered_hash == stored_hash:
                    self._log(self.success_message, "success")
                    self.attempts = 0
                    return True
                else:
                    self.attempts += 1
                    remaining = self.max_attempts - self.attempts
                    if remaining > 0:
                        self._log(f"{self.fail_message} ({remaining} Versuche übrig)", "warning")
                    else:
                        self._log("Zu viele Fehlversuche. Zugang gesperrt!", "error")
                        self.locked = True
                        return False

            return False
        except Exception as e:
            self._log(f"Fehler bei der Passwortprüfung: {e}", "error")
            return False

    def set_messages(self, success_message, fail_message):
        """
        Setzt individuelle Erfolg- und Fehlermeldungen.

        :param success_message: Nachricht bei Erfolg.
        :param fail_message: Nachricht bei Fehler.
        """
        self.success_message = success_message
        self.fail_message = fail_message