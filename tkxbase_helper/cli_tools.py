from colorama import Fore, Style, init
from datetime import datetime

# Colorama initialisieren (wichtig für Windows, Mac und Linux)
init(autoreset=True)

class CLtools:
    """
    Klasse für Konsolen-Tools mit farbigen Ausgaben und optionaler Zeitstempelanzeige.
    Ermöglicht das Setzen eines Präfixes, Ein- und Ausschalten der Zeitstempel sowie farbige Ausgaben nach Level.
    """

    def __init__(self, prefix="[CLTOOLS] ", show_time=True):
        """
        Initialisiert die CLtools-Klasse.
        
        :param prefix: String, der vor jeder Ausgabe als Präfix angezeigt wird (Standard: "[CLTOOLS] ").
        :param show_time: Bool, ob ein Zeitstempel vor der Ausgabe angezeigt wird (Standard: True).
        """
        self.prefix = prefix
        self.show_time = show_time

    def setCLPrefix(self, prefix):
        """
        Setzt das Präfix für die Konsolenausgaben.
        
        :param prefix: Neuer Präfix-String.
        """
        self.prefix = prefix

    def setShowTime(self, show_time):
        """
        Aktiviert oder deaktiviert die Anzeige des Zeitstempels vor Ausgaben.
        
        :param show_time: Bool, True für Anzeige, False für keine Anzeige.
        """
        self.show_time = show_time

    def printCL(self, text, level="info"):
        """
        Gibt einen Text in der Konsole mit farblicher Hervorhebung und optionalem Zeitstempel aus.
        
        :param text: Der auszugebende Text.
        :param level: Level der Nachricht zur Farbwahl (info, success, warning, error).
        """
        color = self._get_color(level)
        time_stamp = self._get_timestamp() if self.show_time else ""
        print(f"{color}{time_stamp}{self.prefix}{text}{Style.RESET_ALL}")

    def _get_color(self, level):
        """
        Bestimmt die Farbe basierend auf dem Level.
        
        :param level: String-Level der Nachricht.
        :return: Farbcode als String.
        """
        level = level.lower()
        if level == "info":
            return Fore.CYAN
        elif level == "success":
            return Fore.GREEN
        elif level == "warning":
            return Fore.YELLOW
        elif level == "error":
            return Fore.RED
        else:
            return Fore.WHITE

    def _get_timestamp(self):
        """
        Erzeugt einen aktuellen Zeitstempel im Format [YYYY-MM-DD HH:MM:SS].
        
        :return: Zeitstempel als String.
        """
        now = datetime.now()
        return f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] "