

from pages.claim_page import ClaimPage
from config.config import CLAIM_REQUEST


def test_initiate_and_submit_claim_request(logged_in_dashboard, driver):
    logged_in_dashboard.click_menu_item("Claim")

    claim_page = ClaimPage(driver)
    claim_page.click_submit_claim_tab()
    claim_page.initiate_claim(
        event_name=CLAIM_REQUEST["event_name"],
        currency=CLAIM_REQUEST["currency"],
        remarks=CLAIM_REQUEST["remarks"],
    )

    assert claim_page.is_claim_submitted_successfully(), (
        "The claim request should be successfully submitted with a confirmation shown."
    )
