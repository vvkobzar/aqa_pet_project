from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver)
            sortable_page.open()

            list_before, list_after = sortable_page.change_tab_order('List')
            grid_before, grid_after = sortable_page.change_tab_order('Grid')

            assert list_before != list_after, "the order of the list has not been changed"
            assert grid_before != grid_after, "the order of the grid has not been changed"

    class TestSelectablePage:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver)
            selectable_page.open()

            items_list = selectable_page.select_tab_items('List')
            items_grid = selectable_page.select_tab_items('Grid')

            assert len(items_list) > 0, "no elements were selected"
            assert len(items_grid) > 0, "no elements were selected"

    class TestResizablePage:
        def test_resizable_box_expected_maximum_and_minimum_size(self, driver):
            resizable_page = ResizablePage(driver)
            resizable_page.open()

            starting_size, max_size, min_size = resizable_page.change_size_resizable_box()

            assert starting_size == ('200px', '200px'), (
                "the starting size does not correspond to the expected result"
            )
            assert max_size == ('500px', '300px'), (
                "the maximum size does not correspond to the expected result"
            )
            assert min_size == ('150px', '150px'), (
                "the minimum size does not correspond to the expected result"
            )

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver)
            resizable_page.open()

            starting_size, max_size, min_size = resizable_page.change_size_resizable()

            assert starting_size != max_size and min_size, (
                "resizable has not been changed"
            )
            assert max_size != min_size, (
                "resizable has not been changed"
            )

    class TestDroppablePage:
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open()

            tab_simple_status, drop_box_text = droppable_page.drop_simple()

            assert tab_simple_status == 'true', (
                "the simple tab is not open by default"
            )
            assert drop_box_text == "Dropped!", (
                "the element has not been dropped"
            )

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open()

            drop_text_not_acceptable, drop_text_acceptable = droppable_page.drop_accept()

            assert drop_text_not_acceptable == "Drop here", (
                "the not acceptable drag has been accepted "
            )
            assert drop_text_acceptable == "Dropped!", (
                "the acceptable drag has not been accepted"
            )

        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open()

            (not_greedy_outer_drop, not_greedy_inner_drop,
             greedy_outer_drop, greedy_inner_drop) = droppable_page.drop_prevent_propogation()

            assert not_greedy_outer_drop == 'Dropped!', (
                "the not greedy outer drop box text has not been changed"
            )
            assert not_greedy_inner_drop == 'Dropped!', (
                "the not greedy inner drop box text has not been changed"
            )
            assert greedy_outer_drop == "Outer droppable", (
                "the greedy outer drop box text has been changed"
            )
            assert greedy_inner_drop == 'Dropped!', (
                "the greedy inner drop box text has not been changed"
            )

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver)
            droppable_page.open()

            revert_position_after_move, revert_position_after_revert = (
                droppable_page.drop_revert_draggable('Will Revert')
            )
            not_revert_position_after_move, not_revert_position_after_revert = (
                droppable_page.drop_revert_draggable('Not Revert')
            )

            assert revert_position_after_move != revert_position_after_revert, "the element has not reverted"
            assert not_revert_position_after_move == not_revert_position_after_revert, "the element has reverted"

    class TestDragabblePage:
        def test_simple_dragabble(self, driver):
            dragabble_page = DragabblePage(driver)
            dragabble_page.open()

            before_move_position, after_move_position = dragabble_page.change_position_drags('Drag me')

            assert before_move_position != after_move_position, "element in not dragged"

        def test_axis_restricted_draggable(self, driver):
            dragabble_page = DragabblePage(driver)
            dragabble_page.open()

            only_x_before, only_x_after = dragabble_page.change_position_drags('Only X')
            only_y_before, only_y_after = dragabble_page.change_position_drags('Only Y')

            assert only_x_before != only_x_after, "element in not dragged"
            assert only_x_after[1] == ' top: 0px', (
                'element has shifted along the x-axis'
            )
            assert only_y_before != only_y_after, "element in not dragged"
            assert only_y_after[0] == ' left: 0px', (
                'element has shifted along the y-axis'
            )

        def test_container_restricted(self, driver):
            dragabble_page = DragabblePage(driver)
            dragabble_page.open()

            box_drag_actual_result = dragabble_page.container_restricted('Drag box')
            box_drag_expected_result = [" left: 674px", " top: 106px"]

            parent_drag_actual_result = dragabble_page.container_restricted('Drag parent')
            parent_drag_expected_result = [" left: 15px", " top: 88px"]

            assert box_drag_actual_result == box_drag_expected_result, "box drag goes out of the box"
            assert parent_drag_actual_result == parent_drag_expected_result, "parent drag goes out of the box"
