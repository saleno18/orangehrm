

import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.parametrize("menu_item", DashboardPage.EXPECTED_MENU_ITEMS)
def test_main_menu_item_visible_and_clickable(logged_in_dashboard, menu_item):
    assert logged_in_dashboard.is_menu_item_visible_and_clickable(menu_item), (
        f"Menu item '{menu_item}' should be visible and clickable after login."
    )
