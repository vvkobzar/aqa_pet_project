class AccordianPageLocators:
    CARD_FIRST = ("xpath", "//div[@id='section1Heading']")
    CARD_FIRST_COLLAPSE_STATUS = ("xpath", "//div[@id='section1Heading']/following-sibling::div[@class]")
    CARD_FIRST_TEXT = ("xpath", "//div[@id='section1Content']/p")
    CARD_SECOND = ("xpath", "//div[@id='section2Heading']")
    CARD_SECOND_COLLAPSE_STATUS = ("xpath", "//div[@id='section2Heading']/following-sibling::div[@class]")
    CARD_SECOND_TEXT = ("xpath", "//div[@id='section2Content']/p")
    CARD_THIRD = ("xpath", "//div[@id='section3Heading']")
    CARD_THIRD_COLLAPSE_STATUS = ("xpath", "//div[@id='section3Heading']/following-sibling::div[@class]")
    CARD_THIRD_TEXT = ("xpath", "//div[@id='section3Content']/p")


class AutoCompletePageLocators:
    MULTIPLE_COLOR_FIELD = ("xpath", "//input[@id='autoCompleteMultipleInput']")
    COLOR_NAMES = ("xpath", "//div[@class='css-12jo7m5 auto-complete__multi-value__label']")
    COLOR_REMOVE_BUTTON = ("xpath", "//div[@class='css-xb97g8 auto-complete__multi-value__remove']")
    ALL_REMOVE_COLOR_FIELD_BUTTON = ("xpath", "//div[@class='auto-complete__indicators css-1wy0on6']")
