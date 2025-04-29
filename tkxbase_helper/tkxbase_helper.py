# tkxbase_helper.py
"""
TKxBASE Helper - Master-Import für alle CLI-Tools.
Importiert CLtools, AdminPWManager und FileTools zusammen.
"""

from .cli_tools import CLtools
from .admin_tools import AdminPWManager
from .file_tools import FileTools

class TKxBASEHelper:
    """
    Zentraler Zugriffspunkt auf alle TKxBASE Helper-Module.
    """

    def __init__(self, prefix="[TKxBASE] ", show_time=True):
        """
        Initialisiert CLtools, AdminPWManager und FileTools.

        :param prefix: Prefix für Konsolenausgaben (Standard: "[TKxBASE] ").
        :param show_time: True, wenn Zeitstempel angezeigt werden sollen.
        """
        self.cli = CLtools(prefix=prefix, show_time=show_time)
        self.admin = AdminPWManager()
        self.files = FileTools()


    def version(self):
        """
        Gibt die aktuelle Version des Toolkits zurück.
        """
        return "TKxBASE Helper v1.0 🚀"
    
