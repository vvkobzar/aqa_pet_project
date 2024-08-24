import allure
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage


@allure.epic("UI Tests")
@allure.feature("Interactions")
class TestInteractions:

    @allure.story("Sortable")
    class TestSortablePage:

        @allure.title("Sortable")
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver)
            sortable_page.open()

            list_before, list_after = sortable_page.change_tab_order('List')
            grid_before, grid_after = sortable_page.change_tab_order('Grid')

            with allure.step("Checking that the order of the 'List' tab has changed"):
                assert list_before != list_after, "the order of the list has not been changed"

            with allure.step("Checking that the order of the 'Grid' tab has changed"):
                assert grid_before != grid_after, "the order of the grid has not been changed"

    @allure.story("Selectable")
    class TestSelectablePage:

        @allure.title("Selectable")
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver)
            selectable_page.open()

            items_list = selectable_page.select_tab_items('List')
            items_grid = selectable_page.select_tab_items('Grid')

            with allure.step("Checking that at least one element was selected in the 'List' tab"):
                assert len(items_list) > 0, "no elements were selected"

            with allure.step("Checking that at least one element was selected in the 'Grid' tab"):
                assert len(items_grid) > 0, "no elements were selected"

    @allure.story("Resizable")
    class TestResizablePage:

        @allure.title("Resizable box expected maximum and minimum size")
        def test_resizable_box_expected_maximum_and_minimum_size(self, driver):
            resizable_page = ResizablePage(driver)
            resizable_page.open()

            starting_size, max_size, min_size = resizable_page.change_size_resizable_box()

            with allure.step("Checking that the starting size of the resizable box is as expected"):
                assert starting_size == ('200px', '200px'), (
                    "the starting size does not correspond to the expected result"
                )
            with allure.step("Checking that the maximum size of the resizable box is as expected"):
                assert max_size == ('500px', '300px'), (
                    "the maximum size does not correspond to the expected result"
                )
            with allure.step("Checking that the minimum size of the resizable box is as expected"):
                assert min_size == ('150px', '150px'), (
                    "the minimum size does not correspond to the expected result"
                )

        @allure.title("Resizable")
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver)
            resizable_page.open()

            starting_size, max_size, min_size = resizable_page.change_size_resizable()

            with allure.step("Checking that the size has changed from the starting size"):
                assert starting_size != max_size and min_size, (
                    "resizable has not been changed"
                )
            with allure.step("Checking that the size has changed from the minimum size"):
                assert max_size != min_size, (
                    "resizable has not been changed"
                )

    @allure.story("Droppable")
    class TestDroppablePage:

        @allure.title("Simple droppable")
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open()

            tab_simple_status, drop_box_text = droppable_page.drop_simple()

            with allure.step("Checking that the simple tab is open by default"):
                assert tab_simple_status == 'true', (
                    "the simple tab is not open by default"
                )
            with allure.step("Checking that the element has been dropped successfully"):
                assert drop_box_text == "Dropped!", (
                    "the element has not been dropped"
                )

        @allure.title("Accept droppable")
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open()

            drop_text_not_acceptable, drop_text_acceptable = droppable_page.drop_accept()

            with allure.step("Checking that the not acceptable drag has not been accepted"):
                assert drop_text_not_acceptable == "Drop here", (
                    "the not acceptable drag has been accepted "
                )
            with allure.step("Checking that the acceptable drag has been accepted"):
                assert drop_text_acceptable == "Dropped!", (
                    "the acceptable drag has not been accepted"
                )

        @allure.title("Prevent propogation droppable")
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open()

            (not_greedy_outer_drop, not_greedy_inner_drop,
             greedy_outer_drop, greedy_inner_drop) = droppable_page.drop_prevent_propogation()

            with allure.step("Checking that the not greedy outer drop box text has been changed"):
                assert not_greedy_outer_drop == 'Dropped!', (
                    "the not greedy outer drop box text has not been changed"
                )
            with allure.step("Checking that the not greedy inner drop box text has been changed"):
                assert not_greedy_inner_drop == 'Dropped!', (
                    "the not greedy inner drop box text has not been changed"
                )
            with allure.step("Checking that the greedy outer drop box text has not been changed"):
                assert greedy_outer_drop == "Outer droppable", (
                    "the greedy outer drop box text has been changed"
                )
            with allure.step("Checking that the greedy inner drop box text has been changed"):
                assert greedy_inner_drop == 'Dropped!', (
                    "the greedy inner drop box text has not been changed"
                )

        @allure.title("Revert draggable droppable")
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open()

            revert_position_after_move, revert_position_after_revert = (
                droppable_page.drop_revert_draggable('Will Revert')
            )
            not_revert_position_after_move, not_revert_position_after_revert = (
                droppable_page.drop_revert_draggable('Not Revert')
            )

            with allure.step("Checking that the 'Will Revert' element has reverted to its original position"):
                assert revert_position_after_move != revert_position_after_revert, "the element has not reverted"

            with allure.step("Checking that the 'Not Revert' element remains in its moved position"):
                assert not_revert_position_after_move == not_revert_position_after_revert, "the element has reverted"

    @allure.story("Dragabble")
    class TestDragabblePage:

        @allure.title("Simple dragabble")
        def test_simple_dragabble(self, driver):
            dragabble_page = DragabblePage(driver)
            dragabble_page.open()

            before_move_position, after_move_position = dragabble_page.change_position_drags('Drag me')

            with allure.step("Checking that the element's position has changed after dragging"):
                assert before_move_position != after_move_position, "element in not dragged"

        @allure.title("Axis restricted draggable")
        def test_axis_restricted_draggable(self, driver):
            dragabble_page = DragabblePage(driver)
            dragabble_page.open()

            only_x_before, only_x_after = dragabble_page.change_position_drags('Only X')
            only_y_before, only_y_after = dragabble_page.change_position_drags('Only Y')

            with allure.step("Checking that the element's position has changed on X-axis"):
                assert only_x_before != only_x_after, "element in not dragged"
                assert only_x_after[1] == ' top: 0px', (
                    'element has shifted along the x-axis'
                )
            with allure.step("Checking that the element's position has changed on Y-axis"):
                assert only_y_before != only_y_after, "element in not dragged"
                assert only_y_after[0] == ' left: 0px', (
                    'element has shifted along the y-axis'
                )

        @allure.title("Container restricted")
        def test_container_restricted(self, driver):
            dragabble_page = DragabblePage(driver)
            dragabble_page.open()

            box_drag_actual_result = dragabble_page.container_restricted('Drag box')
            box_drag_expected_result = [" left: 674px", " top: 106px"]

            parent_drag_actual_result = dragabble_page.container_restricted('Drag parent')
            parent_drag_expected_result = [" left: 15px", " top: 88px"]

            with allure.step("Checking that the 'Drag box' did not move outside its container"):
                assert box_drag_actual_result == box_drag_expected_result, "box drag goes out of the box"

            with allure.step("Checking that the 'Drag parent' did not move outside its container"):
                assert parent_drag_actual_result == parent_drag_expected_result, "parent drag goes out of the box"
