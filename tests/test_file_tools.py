from tkxbase_helper.file_tools import FileTools

files = FileTools()

files.create_folder("testordner")
files.copy_file("quelle.txt", "testordner/ziel.txt")  # Beispiel: musst selbst quelle.txt anlegen
files.delete_file("testordner/ziel.txt")