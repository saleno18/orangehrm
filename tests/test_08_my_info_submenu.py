

import pytest
from pages.my_info_page import MyInfoPage


def test_my_info_submenu_items_present(logged_in_dashboard, driver):
    logged_in_dashboard.click_menu_item("My Info")

    my_info_page = MyInfoPage(driver)
    visible_items = my_info_page.get_visible_submenu_items()

    for expected_item in MyInfoPage.EXPECTED_SUBMENU_ITEMS:
        assert expected_item in visible_items, (
            f"Expected sub-menu item '{expected_item}' to be listed under My Info."
        )


@pytest.mark.parametrize("submenu_item", ["Personal Details", "Contact Details", "Emergency Contacts"])
def test_my_info_submenu_item_opens_correct_page(logged_in_dashboard, driver, submenu_item):
    logged_in_dashboard.click_menu_item("My Info")

    my_info_page = MyInfoPage(driver)
    assert my_info_page.is_submenu_item_clickable(submenu_item), (
        f"Sub-menu item '{submenu_item}' should be clickable."
    )
    my_info_page.click_submenu_item(submenu_item)

    header = my_info_page.get_current_section_header()
    assert header, f"Expected a page header to load after clicking '{submenu_item}'."
