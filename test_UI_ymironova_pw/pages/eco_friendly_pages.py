from test_UI_ymironova_pw.pages.base_pages import BasePage
from test_UI_ymironova_pw.pages.locators import eco_friendly_locators as loc
from playwright.sync_api import expect


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'


    def choose_item(self):
        self.page.evaluate('window.scrollTo(0, 500)')
        cards = self.find(loc.cards_loc)
        card = cards.nth(0)
        name = self.find(loc.name_item_loc).nth(0).text_content()
        colour = self.find(loc.color_loc).nth(0)
        size = self.find(loc.size_loc).nth(0)
        button = self.find(loc.button_cart_loc).nth(0)
        card.hover()
        colour.click()
        size.click()
        button.click()
        expect(self.find(loc.message_successful_added_loc)).to_have_text(f'You added {name} to your shopping cart.')
        return name


    def open_cart(self):
        cart_link = self.page.get_by_role('link', name='shopping cart')
        cart_link.click()


    def check_item_in_cart(self, name):
        expect(self.find(loc.name_in_cart_loc)).to_have_text(name)


    def open_cart_icon(self):
        button_cart = self.find(loc.cart_icon_loc)
        button_cart.click()


    def check_item_in_cart_icon(self, name):
        expect(self.find(loc.cart_icon_item_name_loc)).to_have_text(name)


    def remove_item(self):
        remove_icon = self.find(loc.remove_icon_loc)
        remove_icon.click()


    def approve_alert(self):
        ok_button = self.find(loc.alert_accept_loc)
        ok_button.click()
        expect(self.find(loc.inform_message_loc)).to_have_text('You have no items in your shopping cart.')


    def select_sort(self):
        select_sort = self.find(loc.select_sort_loc).nth(0)
        select_sort.select_option('price')
        self.page.wait_for_url(
            'https://magento.softwaretestingboard.com/collections/eco-friendly.html?product_list_order=price')


    def check_sort(self):
        price = self.find(loc.price_loc)
        price_start = price.nth(0).text_content()
        price_finish = price.nth(11).text_content()
        price_start = float(price_start[1:])
        price_finish = float(price_finish[1:])
        assert price_start < price_finish
