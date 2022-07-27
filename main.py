from logger_utils import LoggerUtils
from steam import SteamPage
import pytest
from string_utils import StringUtils


@pytest.fixture()
def pre_post_cond():
    LoggerUtils().log_precondition("Open page.")
    assert SteamPage().open_steam_page(), "Open steam page failed"
    yield
    LoggerUtils().log_clean_up("Quit page.")
    SteamPage().quit_page()


def test_task2(pre_post_cond):
    # TOP SELLERS
    LoggerUtils().log_test_step("Click new and noteworthy element.")
    assert SteamPage().click_new_and_noteworthy(), "Click new and noteworthy failed"

    LoggerUtils().log_test_step("Click top sellers element.")
    assert SteamPage().click_top_seller(), "Click top sellers failed"

    LoggerUtils().log_test_step("Click action checkbox.")
    assert SteamPage().click_action_checkbox(), "Click action checkbox failed"

    LoggerUtils().log_test_step("Click lan co-op checkbox.")
    assert SteamPage().click_lan_co_op_checkbox(), "Click LAN co-op checkbox failed"

    LoggerUtils().log_test_step("Click SteamOS + Linux checkbox.")
    assert SteamPage().click_steamos_linux_checkbox(), "Click SteamOS + Linux checkbox failed"

    LoggerUtils().log_test_step("Get name of the first game.")
    success, value = SteamPage().get_name_of_the_first_game()
    assert success, "Getting name of first game failed"
    LoggerUtils().log_info_message(value)

    LoggerUtils().log_test_step("Get date of the first game.")
    success, value = SteamPage().get_date_of_the_first_game()
    assert success, "Getting game date of first game failed"
    LoggerUtils().log_info_message(value)

    LoggerUtils().log_test_step("Get price of the first game.")
    success, value = SteamPage().get_price_of_the_first_game()
    assert success, "Getting price of first game failed"
    if "\n" in value:
        LoggerUtils().log_info_message(StringUtils().split_by(value, "\n")[1])
    else:
        LoggerUtils().log_info_message(value)

    LoggerUtils().log_test_step("Get first game.")
    assert SteamPage().click_first_game(), "Getting first game failed"
