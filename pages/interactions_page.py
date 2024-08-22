import time
import allure
import random

from pages.base_page import BasePage
from config.links import InteractionsPageLinks
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragabblePageLocators


class SortablePage(BasePage):
    PAGE_URL = InteractionsPageLinks.SORTABLE
    locators = SortablePageLocators()

    @allure.step("Getting sortable items from the page")
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        with allure.step("Extracting text from each visible element"):
            return [item.text for item in item_list]

    @allure.step("Changing tab order and verifying new order")
    def change_tab_order(self, name_tab):
        tabs = {
            'List':
                {'tab': self.locators.TAB_LIST,
                 'tab_items': self.locators.TAB_LIST_ITEMS},
            'Grid':
                {'tab': self.locators.TAB_GRID,
                 'tab_items': self.locators.TAB_GRID_ITEMS}
        }
        with allure.step(f"Clicking on the '{name_tab}' tab"):
            self.element_is_visible(tabs[name_tab]['tab']).click()

        with allure.step(f"Getting the order of items before change in '{name_tab}' tab"):
            order_before = self.get_sortable_items(tabs[name_tab]['tab_items'])
        with allure.step(f"Performing drag-and-drop operation in '{name_tab}' tab"):
            item_list = random.sample(self.elements_are_visible(tabs[name_tab]['tab_items']), k=2)
            item_what = item_list[0]
            item_where = item_list[1]
            self.action_drag_and_drop_to_element(item_what, item_where)
        with allure.step(f"Getting the order of items after change in '{name_tab}' tab"):
            order_after = self.get_sortable_items(tabs[name_tab]['tab_items'])
        return order_before, order_after


class SelectablePage(BasePage):
    PAGE_URL = InteractionsPageLinks.SELECTABLE
    locators = SelectablePageLocators()

    @allure.step("Clicking selectable items")
    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        with allure.step("Selecting a random number of items"):
            num_subjects = random.randint(1, len(item_list))
            selected_items = random.sample(item_list, num_subjects)
        with allure.step("Clicking on each selected item"):
            for item in selected_items:
                item.click()

    @allure.step("Selecting tab and getting active item texts")
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
        with allure.step(f"Clicking on the '{name_tab}' tab"):
            self.element_is_visible(tabs[name_tab]['tab']).click()
        with allure.step(f"Clicking selectable items in the '{name_tab}' tab"):
            self.click_selectable_item(tabs[name_tab]['tab_items'])
        with allure.step(f"Getting texts of active items in the '{name_tab}' tab"):
            active_element = self.elements_are_visible(tabs[name_tab]['tab_active_items'])
            selected_element_text = [element.text for element in active_element]
        return selected_element_text


class ResizablePage(BasePage):
    PAGE_URL = InteractionsPageLinks.RESIZABLE
    locators = ResizablePageLocators()

    @allure.step("Parsing width and height from size string")
    def get_px_from_width_height(self, value_of_size):
        with allure.step("Splitting size string to extract width and height"):
            width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
            height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step("Getting max and min size of the resizable box")
    def get_max_min_size(self, element):
        with allure.step("Getting the style attribute from the resizable element"):
            size = self.element_is_visible(element)
            size_value = size.get_attribute('style')
        return size_value

    @allure.step("Changing size of the resizable box")
    def change_size_resizable_box(self):
        with allure.step("Getting the starting size of the resizable box"):
            starting_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))

        with allure.step("Increasing the size of the resizable box"):
            self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE),
                                                350, 150)
            max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))

        with allure.step("Decreasing the size of the resizable box"):
            self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE),
                                                -400, -200)
            min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))

        return starting_size, max_size, min_size

    @allure.step("Changing size of the resizable element")
    def change_size_resizable(self):
        with allure.step("Getting the starting size of the resizable element"):
            starting_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))

        with allure.step("Increasing the size of the resizable element"):
            self.action_drag_and_drop_by_offset(self.element_is_visible(
                self.locators.RESIZABLE_HANDLE), random.randint(1, 380), random.randint(1, 300)
            )
            max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))

        with allure.step("Decreasing the size of the resizable element"):
            self.action_drag_and_drop_by_offset(self.element_is_visible(
                self.locators.RESIZABLE_HANDLE), random.randint(-500, -1), random.randint(-500, -1)
            )
            min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))

        return starting_size, max_size, min_size


class DroppablePage(BasePage):
    PAGE_URL = InteractionsPageLinks.DROPPABLE
    locators = DroppablePageLocators()

    @allure.step("Performing simple drop action")
    def drop_simple(self):
        with allure.step("Checking the default state of the simple tab"):
            tab_simple_status = self.element_is_visible(self.locators.SIMPLE_TAB).get_attribute('aria-selected')

        with allure.step("Performing drag and drop action"):
            drag_div = self.element_is_visible(self.locators.SIMPLE_DRAG_BOX)
            drop_box = self.element_is_visible(self.locators.SIMPLE_DROP_BOX)
            self.action_drag_and_drop_to_element(drag_div, drop_box)

        return tab_simple_status, drop_box.text

    @allure.step("Performing accept drop action")
    def drop_accept(self):
        with allure.step("Selecting the Accept tab"):
            self.element_is_visible(self.locators.ACCEPT_TAB).click()

        with allure.step("Getting the not acceptable and acceptable drag boxes and the drop box"):
            drag_not_acceptable = self.element_is_visible(self.locators.ACCEPT_DRAG_BOX_NOT_ACCEPTABLE)
            drag_acceptable = self.element_is_visible(self.locators.ACCEPT_DRAG_BOX_ACCEPTABLE)
            drop_box = self.element_is_visible(self.locators.ACCEPT_DROP_BOX)

        with allure.step("Performing drag and drop action with not acceptable box"):
            self.action_drag_and_drop_to_element(drag_not_acceptable, drop_box)
            drop_text_not_acceptable = drop_box.text

        with allure.step("Performing drag and drop action with acceptable box"):
            self.action_drag_and_drop_to_element(drag_acceptable, drop_box)
            drop_text_acceptable = drop_box.text

        return drop_text_not_acceptable, drop_text_acceptable

    @allure.step("Performing prevent propagation drop action")
    def drop_prevent_propogation(self):
        with allure.step("Clicking on the Prevent Propagation tab"):
            self.element_is_visible(self.locators.PREVENT_TAB).click()

        with allure.step("Getting drag box and drop boxes for not greedy and greedy cases"):
            drag_box = self.element_is_visible(self.locators.PREVENT_DRAG_BOX)
            not_greedy_outer_drop = self.element_is_visible(self.locators.PREVENT_NOT_GREEDY_DROP_BOX)
            not_greedy_inner_drop = self.element_is_visible(self.locators.PREVENT_NOT_GREEDY_INNER_DROP_BOX)
            greedy_outer_drop = self.element_is_visible(self.locators.PREVENT_GREEDY_DROP_BOX)
            greedy_inner_drop = self.element_is_visible(self.locators.PREVENT_GREEDY_INNER_DROP_BOX)

        self.action_drag_and_drop_to_element(drag_box, not_greedy_inner_drop)
        self.action_drag_and_drop_to_element(drag_box, greedy_inner_drop)

        return not_greedy_outer_drop.text, not_greedy_inner_drop.text, greedy_outer_drop.text, greedy_inner_drop.text

    @allure.step("Performing revert draggable action")
    def drop_revert_draggable(self, name_drag):
        with allure.step(f"Getting the drag box for {name_drag} and the drop box"):
            drags = {
                'Will Revert': self.locators.REVERT_DRAG_BOX,
                'Not Revert': self.locators.REVERT_NOT_DRAG_BOX
            }

        self.element_is_visible(self.locators.REVERT_TAB).click()
        drag = self.element_is_visible(drags[name_drag])
        drop_box = self.element_is_visible(self.locators.REVERT_DROP_BOX)
        self.action_drag_and_drop_to_element(drag, drop_box)

        with allure.step("Getting position after move and after revert"):
            position_after_move = drag.get_attribute('style')
            time.sleep(1)
            position_after_revert = drag.get_attribute('style')
        return position_after_move, position_after_revert


class DragabblePage(BasePage):
    PAGE_URL = InteractionsPageLinks.DRAGABBLE
    locators = DragabblePageLocators()

    @allure.step("Getting position of the element")
    def get_position_element(self, element):
        position_element = element.get_attribute('style')
        elem = position_element.split(';')
        if len(elem) > 2:
            position = [elem[1], elem[2]]
            return position
        else:
            return position_element

    @allure.step("Changing position of the draggable element of type '{type_drag}'")
    def change_position_drags(self, type_drag):
        drags = {
            'Drag me': {
                'locator': self.locators.SIMPLE_DRAG,
                'tab': self.locators.SIMPLE_TAB
            },
            'Only X': {
                'locator': self.locators.AXIS_ONLY_X,
                'tab': self.locators.AXIS_TAB
            },
            'Only Y': {
                'locator': self.locators.AXIS_ONLY_Y,
                'tab': self.locators.AXIS_TAB
            }
        }
        with allure.step(f"Selecting the tab for {type_drag} drag type"):
            self.element_is_visible(drags[type_drag]['tab']).click()
        drag = self.element_is_visible(drags[type_drag]['locator'])
        with allure.step(f"Getting position before moving the element"):
            before_move = self.get_position_element(drag)
        with allure.step(f"Dragging the element and dropping it to a new position"):
            self.action_drag_and_drop_by_offset(drag, random.randint(50, 100), random.randint(50, 100))
        with allure.step(f"Getting position after moving the element"):
            after_move = self.get_position_element(drag)
        return before_move, after_move

    @allure.step("Dragging element in restricted container of type '{type_drag}'")
    def container_restricted(self, type_drag):
        drags = {
            'Drag box': self.locators.CONTAINER_DRAG_BIG_BOX,
            'Drag parent': self.locators.CONTAINER_DRAG_SMALL_BOX
        }
        with allure.step("Selecting the container tab"):
            self.element_is_visible(self.locators.CONTAINER_TAB).click()
        drag = self.element_is_visible(drags[type_drag])
        with allure.step(f"Dragging the element and dropping it within the restricted container"):
            self.action_drag_and_drop_by_offset(drag, 700, 300)
        with allure.step(f"Getting the position of the element after moving"):
            position_after_move = self.get_position_element(drag)
        return position_after_move
