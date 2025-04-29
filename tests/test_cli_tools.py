from tkxbase_helper.cli_tools import CLtools

cli = CLtools()

cli.printCL("Test Info", level="info")
cli.printCL("Test Erfolg", level="success")
cli.printCL("Test Warnung", level="warning")
cli.printCL("Test Fehler", level="error")