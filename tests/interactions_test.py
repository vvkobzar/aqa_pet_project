from pages.interactions_page import SortablePage, SelectablePage


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
