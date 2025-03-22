from playwright.sync_api import Page, expect, BrowserContext


def test_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    page_text = page.locator('#result-text')
    expect(page_text).to_have_text('Ok')


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button = page.get_by_role('link', name='Click')
    with context.expect_page() as new_pag_event:
        button.click()
    new_page = new_pag_event.value
    text_page = new_page.locator('#result-text')
    expect(text_page).to_have_text('I am a new page in a new tab')
    new_page.close()
    expect(button).to_be_enabled()


def test_click_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    expect(button).to_have_class('mt-4 text-danger btn btn-primary')
    button.click()
