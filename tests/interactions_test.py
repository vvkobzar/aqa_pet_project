from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


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