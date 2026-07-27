from core.device import Device

PACKAGE = "com.kosmokominfo"

device = Device()

print(device.info())

device.start_app(PACKAGE)

device.wait(3)

device.screenshot("screenshots/kosmo.png")

device.dump("screenshots/kosmo.xml")
