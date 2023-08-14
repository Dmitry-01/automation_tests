from pages.interactions_page import SortablePage, SelecablePage


class TestInteractions:
    class TestSortablePagePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()

            assert list_before != list_after, "the order of the list has not been changed"
            assert grid_before != grid_after, "the order of the list has not been changed"

    class TestSelecablePage:
        def test_selectable(self, driver):
            selectable_page = SelecablePage(driver,"https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_frid = selectable_page.select_grid_item()
            assert len(item_list) > 0 ,"no element were selected"
            assert len(item_frid) > 0 ,"no element were selected"