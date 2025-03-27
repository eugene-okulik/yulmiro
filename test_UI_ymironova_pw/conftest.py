import pytest
from playwright.sync_api import BrowserContext
from pages.create_account_pages import CreateAccount
from pages.eco_friendly_pages import EcoFriendlyPage
from pages.sale_pages import SalePage


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    return page


@pytest.fixture()
def create_acc_page(page):
    return CreateAccount(page)

@pytest.fixture()
def create_eco_friendly_page(page):
    return EcoFriendlyPage(page)

@pytest.fixture()
def create_sale_page(page):
    return SalePage(page)