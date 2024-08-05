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
    SIMPLE_TAB = ("xpath", "//a[@id='droppableExample-tab-simple']")
    SIMPLE_DRAG_BOX = ("xpath", "//div[@id='draggable']")
    SIMPLE_DROP_BOX = ("xpath", "//div[@id='simpleDropContainer']/div[@id='droppable']")

    # Accept
    ACCEPT_TAB = ("xpath", "//a[@id='droppableExample-tab-accept']")
    ACCEPT_DRAG_BOX_ACCEPTABLE = ("xpath", "//div[@id='acceptable']")
    ACCEPT_DRAG_BOX_NOT_ACCEPTABLE = ("xpath", "//div[@id='notAcceptable']")
    ACCEPT_DROP_BOX = ("xpath", "//div[@id='acceptDropContainer']/div[@id='droppable']")

    # Prevent Propogation
    PREVENT_TAB = ("xpath", "//a[@id='droppableExample-tab-preventPropogation']")
    PREVENT_DRAG_BOX = ("xpath", "//div[@id='dragBox']")
    PREVENT_NOT_GREEDY_DROP_BOX = ("xpath", "//div[@id='notGreedyDropBox']/p")
    PREVENT_NOT_GREEDY_INNER_DROP_BOX = ("xpath", "//div[@id='notGreedyInnerDropBox']/p")
    PREVENT_GREEDY_DROP_BOX = ("xpath", "//div[@id='greedyDropBox']/p")
    PREVENT_GREEDY_INNER_DROP_BOX = ("xpath", "//div[@id='greedyDropBoxInner']/p")