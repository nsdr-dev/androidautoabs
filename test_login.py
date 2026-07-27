from core.device import Device
from screens.login_screen import LoginScreen

PACKAGE = "com.kosmokominfo"

device = Device()

device.start_app(PACKAGE)

device.wait(2)

device.screenshot("screenshots/debug_login.png")
device.dump("screenshots/debug_login.xml")

device.wait(3)

login = LoginScreen(device)

print("Username :", device.exists_id("com.kosmokominfo:id/etUsername"))
print("Password :", device.exists_id("com.kosmokominfo:id/etPassword"))
print("Login    :", device.exists_id("com.kosmokominfo:id/btnLogin"))

login.login(
    username="bada001",
    password="M@$@$m2424F!)!)f1010"
)

device.wait(3)
device.wait_text("Kehadiran")

device.screenshot("screenshots/login_result.png")
