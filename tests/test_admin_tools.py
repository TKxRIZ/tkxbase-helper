from tkxbase_helper import *
import time

admin = AdminPWManager()

# Nur zum Testen (setzt ein neues Passwort!)
admin.set_admin_password(force_reset=True)
time.sleep(3)
# Danach kannst du checken
if admin.check_admin_password():
    print("success")
else:
    print("error")