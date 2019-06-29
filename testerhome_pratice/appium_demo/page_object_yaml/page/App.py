from testerhome_pratice.appium_demo.page_object_strengthen.driver.AndroidClient import AndroidClient
from testerhome_pratice.appium_demo.page_object_strengthen.page.BasePage import BasePage
from testerhome_pratice.appium_demo.page_object_strengthen.page.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        # AndroidClient.restart_app()
        cls.getClient().restart_app()
        return MainPage()
