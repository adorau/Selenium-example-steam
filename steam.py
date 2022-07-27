from config import ConfigManager
from driver import Driver
from singleton import Singleton


class SteamPage(metaclass=Singleton):

    @staticmethod
    def open_steam_page():
        Driver().open_page(ConfigManager().config["STEAM_PAGE"])
        return Driver().driver.title == "Witamy na Steam"

    def click_new_and_noteworthy(self):
        return self.click_element_on_page("NEW_AND_NOTEWORTHY")

    def click_top_seller(self):
        return self.click_element_on_page("TOP_SELLERS")

    def click_action_checkbox(self):
        return self.click_element_on_page("ACTION")

    def click_lan_co_op_checkbox(self):
        if self.click_element_on_page("NARROW_BY_NUMBER_OF_PLAYERS"):
            return self.click_element_on_page("LAN_CO_OP")
        return False

    def click_steamos_linux_checkbox(self):
        return self.click_element_on_page("STEAM_OS_LINUX")

    def get_name_of_the_first_game(self):
        return self.get_text_from_element("FIRST_GAME_NAME")

    def get_date_of_the_first_game(self):
        return self.get_text_from_element("FIRST_GAME_DATE")

    def get_price_of_the_first_game(self):
        return self.get_text_from_element("FIRST_GAME_PRICE")

    @staticmethod
    def get_text_from_element(element):
        element = Driver().find_element_by(path=ConfigManager().config[element])
        if element:
            return True, element.text
        else:
            return False

    @staticmethod
    def click_element_on_page(element):
        element = Driver().find_element_by(path=ConfigManager().config[element])
        if element:
            element.click()
            return True
        else:
            return False

    def click_first_game(self):
        return self.click_element_on_page("FIRST_GAME_IMG")

    @staticmethod
    def quit_page():
        Driver().quit()
