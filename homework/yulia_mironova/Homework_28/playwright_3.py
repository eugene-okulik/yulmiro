from playwright.sync_api import Page, expect, Route
import re
import json


def test_rewrite_header(page: Page):

    def rewrite_apple(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 16 про"
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(re.compile('step0_iphone'), rewrite_apple)
    page.goto('https://www.apple.com/shop/buy-iphone')
    cards = page.locator('[class="rf-hcard-content-title"]')
    phone = cards.nth(0)
    phone.click()
    new_header = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(new_header).to_have_text('яблокофон 16 про')
