from test_UI_ymironova_pw.pages.base_pages import BasePage
from test_UI_ymironova_pw.pages.locators import sale_locators as loc
from playwright.sync_api import expect


class SalePage(BasePage):
    page_url = "/sale.html"

    def open_page_in_new_tab(self):
        picture = self.find(loc.picture_loc)
        with self.page.context.expect_page() as new_page_event:
            self.page.keyboard.down("Control")
            picture.click()
            self.page.keyboard.up("Control")
        new_page = new_page_event.value
        title = new_page.locator('[class="page-title"]')
        expect(title).to_have_text("Women Sale")

    def open_page_in_same_tab(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        text = self.find(loc.text_loc)
        text.click()

    def open_point(self):
        point = self.page.get_by_role("link", name="Hoodies and Sweatshirts").nth(0)
        point.click()

    def check_correct_section(self):
        expect(self.find(loc.section_loc)).to_have_text("Women")
