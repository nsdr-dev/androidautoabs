import time
import uiautomator2 as u2


class Device:
    def __init__(self):
        self.d = u2.connect()

    # =========================
    # Device Information
    # =========================
    def info(self):
        return self.d.info

    # =========================
    # App Control
    # =========================
    def start_app(self, package):
        self.d.app_start(package, stop=True)

    def stop_app(self, package):
        self.d.app_stop(package)

    # =========================
    # UI Interaction
    # =========================
    # def click_id(self, resource_id):
    #     self.d(resourceId=resource_id).click()

    # def click_id(self, resource_id):
    #     print(f"[CLICK] {resource_id}")
    #     self.d(resourceId=resource_id).wait(timeout=10)
    #     self.d(resourceId=resource_id).click()

    def click_id(self, resource_id):
        print(f"[CLICK] {resource_id}")
        obj = self.d(resourceId=resource_id)
        print("Exists:", obj.exists)
        obj.click()

    def click_text(self, text):
        print(f"[CLICK TEXT] {text}")
        self.d(text=text).wait(timeout=10)
        self.d(text=text).click()

    def set_text(self, resource_id, value):
        print(f"[SET TEXT] {resource_id}")
        self.d(resourceId=resource_id).wait(timeout=10)
        self.d(resourceId=resource_id).set_text(value)

    # def exists(self, resource_id):
    #     return self.d(resourceId=resource_id).exists

    def exists_id(self, resource_id):
        return self.d(resourceId=resource_id).exists

    def exists_text(self, text):
        return self.d(text=text).exists
    # =========================
    # Utilities
    # =========================
    def screenshot(self, filename):
        self.d.screenshot(filename)

    def dump(self, filename):
        xml = self.d.dump_hierarchy()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(xml)
        return xml

    def wait(self, seconds):
        time.sleep(seconds)

    def wait_text(self, text, timeout=20):
        return self.d(text=text).wait(timeout=timeout)

    def press(self, key):
        self.d.press(key)

    def current_package(self):
        return self.d.app_current()["package"]
