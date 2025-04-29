import os
import shutil

class FileTools:
    """
    FileTools-Klasse für einfache Datei- und Ordner-Operationen.
    """

    def create_folder(self, path):
        """
        Erstellt einen Ordner, falls dieser noch nicht existiert.

        :param path: Pfad zum Ordner.
        """
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"[FileTools] Ordner erstellt: {path}")
        else:
            print(f"[FileTools] Ordner existiert bereits: {path}")

    def delete_file(self, file_path):
        """
        Löscht eine Datei, falls sie existiert.

        :param file_path: Pfad zur Datei.
        """
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"[FileTools] Datei gelöscht: {file_path}")
        else:
            print(f"[FileTools] Datei nicht gefunden: {file_path}")

    def copy_file(self, source_path, destination_path):
        """
        Kopiert eine Datei von Quelle zu Ziel.

        :param source_path: Pfad zur Quelldatei.
        :param destination_path: Pfad zum Ziel.
        """
        try:
            shutil.copy2(source_path, destination_path)
            print(f"[FileTools] Datei kopiert: {source_path} -> {destination_path}")
        except Exception as e:
            print(f"[FileTools] Fehler beim Kopieren: {e}")

    def file_exists(self, path):
        """
        Prüft, ob eine Datei existiert.

        :param path: Pfad zur Datei.
        :return: True wenn existiert, False sonst.
        """
        return os.path.isfile(path)

    def folder_exists(self, path):
        """
        Prüft, ob ein Ordner existiert.

        :param path: Pfad zum Ordner.
        :return: True wenn existiert, False sonst.
        """
        return os.path.isdir(path)