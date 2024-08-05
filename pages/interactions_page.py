import random
import time

from config.links import InteractionsPageLinks
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragabblePageLocators
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


class SelectablePage(BasePage):
    PAGE_URL = InteractionsPageLinks.SELECTABLE
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        num_subjects = random.randint(1, len(item_list))
        selected_items = random.sample(item_list, num_subjects)
        for item in selected_items:
            item.click()

    def select_tab_items(self, name_tab):
        tabs = {
            'List':
                {'tab': self.locators.TAB_LIST,
                 'tab_items': self.locators.TAB_LIST_ITEMS,
                 'tab_active_items': self.locators.TAB_LIST_ACTIVE_ITEMS},
            'Grid':
                {'tab': self.locators.TAB_GRID,
                 'tab_items': self.locators.TAB_GRID_ITEMS,
                 'tab_active_items': self.locators.TAB_GRID_ACTIVE_ITEMS},
        }
        self.element_is_visible(tabs[name_tab]['tab']).click()
        self.click_selectable_item(tabs[name_tab]['tab_items'])
        active_element = self.elements_are_visible(tabs[name_tab]['tab_active_items'])
        selected_element_text = [element.text for element in active_element]
        return selected_element_text


class ResizablePage(BasePage):
    PAGE_URL = InteractionsPageLinks.RESIZABLE
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_visible(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        starting_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE),
                                            350, 150)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE),
                                            -400, -200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return starting_size, max_size, min_size

    def change_size_resizable(self):
        starting_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 380), random.randint(1, 300)
                                            )
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-500, -1), random.randint(-500, -1)
                                            )
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return starting_size, max_size, min_size


class DroppablePage(BasePage):
    PAGE_URL = InteractionsPageLinks.DROPPABLE
    locators = DroppablePageLocators()

    def drop_simple(self):
        tab_simple_status = self.element_is_visible(self.locators.SIMPLE_TAB).get_attribute('aria-selected')
        drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_BOX)
        drop_box = self.element_is_visible(self.locators.SIMPLE_DROP_BOX)
        self.action_drag_and_drop_to_element(drag_div, drop_box)
        return tab_simple_status, drop_box.text

    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_not_acceptable = self.element_is_visible(self.locators.ACCEPT_DRAG_BOX_NOT_ACCEPTABLE)
        drag_acceptable = self.element_is_visible(self.locators.ACCEPT_DRAG_BOX_ACCEPTABLE)
        drop_box = self.element_is_visible(self.locators.ACCEPT_DROP_BOX)

        self.action_drag_and_drop_to_element(drag_not_acceptable, drop_box)
        drop_text_not_acceptable = drop_box.text

        self.action_drag_and_drop_to_element(drag_acceptable, drop_box)
        drop_text_acceptable = drop_box.text

        return drop_text_not_acceptable, drop_text_acceptable

    def drop_prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_box = self.element_is_visible(self.locators.PREVENT_DRAG_BOX)
        not_greedy_outer_drop = self.element_is_visible(self.locators.PREVENT_NOT_GREEDY_DROP_BOX)
        not_greedy_inner_drop = self.element_is_visible(self.locators.PREVENT_NOT_GREEDY_INNER_DROP_BOX)
        greedy_outer_drop = self.element_is_visible(self.locators.PREVENT_GREEDY_DROP_BOX)
        greedy_inner_drop = self.element_is_visible(self.locators.PREVENT_GREEDY_INNER_DROP_BOX)

        self.action_drag_and_drop_to_element(drag_box, not_greedy_inner_drop)
        self.action_drag_and_drop_to_element(drag_box, greedy_inner_drop)

        return not_greedy_outer_drop.text, not_greedy_inner_drop.text, greedy_outer_drop.text, greedy_inner_drop.text

    def drop_revert_draggable(self, name_drag):
        drags = {
            'Will Revert': self.locators.REVERT_DRAG_BOX,
            'Not Revert': self.locators.REVERT_NOT_DRAG_BOX
        }
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag = self.element_is_visible(drags[name_drag])
        drop_box = self.element_is_visible(self.locators.REVERT_DROP_BOX)
        self.action_drag_and_drop_to_element(drag, drop_box)
        position_after_move = drag.get_attribute('style')
        time.sleep(1)
        position_after_revert = drag.get_attribute('style')
        return position_after_move, position_after_revert


class DragabblePage(BasePage):
    PAGE_URL = InteractionsPageLinks.DRAGABBLE
    locators = DragabblePageLocators()

    def get_element_position(self, element):
        return element.location

    def change_drag_position(self, tab_name, drag_name):
        tabs = {
            'Simple': self.locators.SIMPLE_TAB,
            'Axis Restricted': self.locators.AXIS_TAB
        }
        drags = {
            'Drag me': self.locators.SIMPLE_DRAG,
            'Only X': self.locators.AXIS_ONLY_X,
            'Only Y': self.locators.AXIS_ONLY_Y
        }

        self.element_is_visible(tabs[tab_name]).click()
        drag = self.element_is_visible(drags[drag_name])
        drag_position_before = self.get_element_position(drag)
        self.action_drag_and_drop_by_offset(drag, random.randint(100, 500), random.randint(100, 500))
        drag_position_after = self.get_element_position(drag)
        return drag_position_before, drag_position_after

