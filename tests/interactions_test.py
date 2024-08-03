from pages.interactions_page import SortablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver)
            sortable_page.open()

            list_before, list_after = sortable_page.change_tab_order('List')
            grid_before, grid_after = sortable_page.change_tab_order('Grid')

            assert list_before != list_after, "the order of the list has not been changed"
            assert grid_before != grid_after, "the order of the grid has not been changed"
