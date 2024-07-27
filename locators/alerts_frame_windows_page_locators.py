class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = ("xpath", "//button[@id='tabButton']")
    NEW_TAB_TEXT = ("xpath", "//h1[@id='sampleHeading']")
    NEW_WINDOW_BUTTON = ("xpath", "//button[@id='windowButton']")


class AlertsPageLocators:
    CLICK_BUTTON_TO_SEE_ALERT = ("xpath", "//button[@id='alertButton']")
    ALERT_APPEAR_5_SEC_BUTTON = ("xpath", "//button[@id='timerAlertButton']")
    ALERT_CONFIRM_BOX_APPEAR_BUTTON = ("xpath", "//button[@id='confirmButton']")
    ALERT_CONFIRM_BOX_RESULT = ("xpath", "//span[@id='confirmResult']")
    ALERT_PROMPT_BOX_WILL_APPEAR_BUTTON = ("xpath", "//button[@id='promtButton']")
    ALERT_PROMPT_BOX_WILL_APPEAR_RESULT = ("xpath", "//span[@id='promptResult']")


class FramesPageLocators:
    FIRST_FRAME = ("xpath", "//iframe[@id='frame1']")
    SECOND_FRAME = ("xpath", "//iframe[@id='frame2']")
    TITLE_FRAME = ("xpath", "//h1[@id='sampleHeading']")


