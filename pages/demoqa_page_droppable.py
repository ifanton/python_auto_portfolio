from components.components import WebElement
from pages.base_page import BasePage


class DroppablePage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/droppable'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.page_header = WebElement(driver, 'div.pattern-backgound.playgound-header')
        self.draggable_element = WebElement(driver, '#draggable')
        self.droppable_element = WebElement(driver, '#simpleDropContainer > #droppable')
        self.page_tab_accept = WebElement(driver, '#droppableExample-tab-accept')
        self.acceptable_element = WebElement(driver, '#acceptable')
        self.not_acceptable_element = WebElement(driver, '#notAcceptable')
        self.accept_droppable_element = WebElement(driver, '#acceptDropContainer > #droppable')
        self.page_tab_prevent = WebElement(driver, '#droppableExample-tab-preventPropogation')
        self.drag_box = WebElement(driver, '#dragBox')
        self.not_greedy_drop_box_inner = WebElement(driver, '#notGreedyInnerDropBox')
        self.not_greedy_drop_box_outer = WebElement(driver, '#notGreedyDropBox')
        self.greedy_drop_box_inner = WebElement(driver, '#greedyDropBoxInner')
        self.greedy_drop_box_outer = WebElement(driver, '#greedyDropBox')
        self.page_tab_revert = WebElement(driver, '#droppableExample-tab-revertable')
        self.revertable_element = WebElement(driver, '#revertable')
        self.not_revertable_element = WebElement(driver, '#notRevertable')
        self.revert_droppable_element = WebElement(driver, '#revertableDropContainer > #droppable')
