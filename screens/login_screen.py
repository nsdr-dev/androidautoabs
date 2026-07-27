from core.device import Device


class LoginScreen:
    """
    Screen Object untuk halaman Login KOSMO.
    Seluruh selector halaman login diletakkan di sini.
    """

    # ==========================
    # Selectors
    # ==========================
    USERNAME = "com.kosmokominfo:id/etUsername"
    PASSWORD = "com.kosmokominfo:id/etPassword"
    LOGIN_BUTTON = "com.kosmokominfo:id/btnLogin"

    def __init__(self, device: Device):
        self.device = device

    def is_open(self):
        """
        Mengecek apakah halaman login sedang tampil.
        """
        return self.device.exists_id(self.LOGIN_BUTTON)

    def input_username(self, username: str):
        self.device.set_text(self.USERNAME, username)

    def input_password(self, password: str):
        self.device.set_text(self.PASSWORD, password)

    def click_login(self):
        self.device.click_id(self.LOGIN_BUTTON)
    #
    # def login(self, username: str, password: str):
    #     """
    #     Login lengkap:
    #     1. Isi username
    #     2. Isi password
    #     3. Klik tombol login
    #     """
    #
    #     if not self.is_open():
    #         raise RuntimeError("Login screen tidak sedang terbuka.")
    #
    #     self.input_username(username)
    #     self.input_password(password)
    #     self.click_login()

    def login(self, username: str, password: str):
        if not self.is_open():
            raise RuntimeError("Login screen tidak sedang terbuka.")

        self.input_username(username)
        self.input_password(password)
        self.device.press("back")
        self.device.wait(1)
        # DEBUG
        self.device.screenshot("screenshots/before_click.png")
        self.device.dump("screenshots/before_click.xml")

        self.click_login()
