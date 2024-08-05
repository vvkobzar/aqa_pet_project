class SortablePageLocators:
    TAB_LIST = ("xpath", "//a[@id='demo-tab-list']")
    TAB_LIST_ITEMS = ("xpath", "//div[@id='demo-tabpane-list']//div[@class='list-group-item list-group-item-action']")
    TAB_GRID = ("xpath", "//a[@id='demo-tab-grid']")
    TAB_GRID_ITEMS = ("xpath", "//div[@id='demo-tabpane-grid']//div[@class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    TAB_LIST = ("xpath", "//a[@id='demo-tab-list']")
    TAB_LIST_ITEMS = (
        "xpath", "//ul[@id='verticalListContainer']/li[@class='mt-2 list-group-item list-group-item-action']")
    TAB_LIST_ACTIVE_ITEMS = (
        "xpath", "//ul[@id='verticalListContainer']/li[@class='mt-2 list-group-item active list-group-item-action']")

    TAB_GRID = ("xpath", "//a[@id='demo-tab-grid']")
    TAB_GRID_ITEMS = ("xpath", "//div[@id='demo-tabpane-grid']//li[@class='list-group-item list-group-item-action']")
    TAB_GRID_ACTIVE_ITEMS = (
        "xpath", "//div[@id='demo-tabpane-grid']//li[@class='list-group-item active list-group-item-action']")


class ResizablePageLocators:
    RESIZABLE_BOX = ("xpath", "//div[@id='resizableBoxWithRestriction']")
    RESIZABLE_BOX_HANDLE = ("xpath", "//div[@id='resizableBoxWithRestriction']"
                                     "/span[@class='react-resizable-handle react-resizable-handle-se']")

    RESIZABLE = ("xpath", "//div[@id='resizable']")
    RESIZABLE_HANDLE = (
        "xpath", "//div[@id='resizable']/span[@class='react-resizable-handle react-resizable-handle-se']")


class DroppablePageLocators:
    # Simple
    TAB_SIMPLE = ("xpath", "//a[@id='droppableExample-tab-simple']")
    SIMPLE_DROP_CONTAINER_HANDLE = (
        "xpath", "//div[@id='simpleDropContainer']/div[@class='drag-box mt-4 ui-draggable ui-draggable-handle']")
    SIMPLE_DROP_CONTAINER_DROPPABLE = (
        "xpath", "//div[@id='simpleDropContainer']/div[contains(@class, 'drop-box ui-droppable')]")
    SIMPLE_DROP_CONTAINER_DROPPABLE_TEXT = (
        "xpath", "//div[@id='simpleDropContainer']/div[contains(@class, 'drop-box ui-droppable')]/p")
