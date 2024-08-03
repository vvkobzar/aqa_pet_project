import random

from config.links import InteractionsPageLinks
from locators.interactions_page_locators import SortablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    PAGE_URL = InteractionsPageLinks.SORTABLE
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_tab_order(self, name_tab):
        tabs = {
            'List':
                {'tab': self.locators.TAB_LIST,
                 'tab_items': self.locators.TAB_LIST_ITEMS},
            'Grid':
                {'tab': self.locators.TAB_GRID,
                 'tab_items': self.locators.TAB_GRID_ITEMS}
        }
        self.element_is_visible(tabs[name_tab]['tab']).click()
        order_before = self.get_sortable_items(tabs[name_tab]['tab_items'])
        item_list = random.sample(self.elements_are_visible(tabs[name_tab]['tab_items']), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(tabs[name_tab]['tab_items'])
        return order_before, order_after
