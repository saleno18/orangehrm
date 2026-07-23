

from pages.leave_page import LeavePage
from config.config import LEAVE_ASSIGNMENT


def test_assign_leave_to_employee(logged_in_dashboard, driver):
    logged_in_dashboard.click_menu_item("Leave")

    leave_page = LeavePage(driver)
    leave_page.click_assign_leave_tab()
    leave_page.assign_leave(
        employee_name=LEAVE_ASSIGNMENT["employee_name"],
        leave_type=LEAVE_ASSIGNMENT["leave_type"],
    )

    assert leave_page.is_leave_assigned_successfully(), (
        "Leave should be assigned successfully and a confirmation shown."
    )
