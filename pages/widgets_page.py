import random
import time
from datetime import date

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_date
from locators.widgets_page_locators import AccordianPageLocators, DataPickerLocators, SliderLocators, \
    ProgressBarLocators, TabsPageLocators, ToolTipsLocators
from pages.base_page import BasePage

class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accardion_num):
        accardion = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD}
                     }
        section_title = self.element_is_visible(accardion[accardion_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accardion[accardion_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accardion[accardion_num]['content']).text
        return [section_title.text, len(section_content)]

class DataPickerPage(BasePage):

    locators = DataPickerLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATA_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATA_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATA_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATA_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_clickable(self.locators.DATA_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATA_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATA_AND_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(self.locators.DATA_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATA_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATA_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATA_AND_TIME_TIME_LIST, 'date.time')
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after


    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_offset(slider_input, random.randint(1,100), 0)

        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')

        return value_before, value_after

class ProgressBarPage(BasePage):
    locators = ProgressBarLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(3)
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after

class TabsPage(BasePage):
    locators = TabsPageLocators()
    def check_tabs(self, name_tab):
        tabs = {'what':
                    {'title': self.locators.TABS_WHAT,
                    'content': self.locators.TABS_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TABS_ORIGIN,
                    'content': self.locators.TABS_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TABS_USE,
                    'content': self.locators.TABS_USE_CONTENT},
                'more':
                    {'title': self.locators.TABS_MORE,
                     'content': self.locators.TABS_MORE_CONTENT}
                }
        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        what_content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(what_content)

class ToolTipsPage(BasePage):
    locators = ToolTipsLocators()

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        time.sleep(1)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK,self.locators.TOOL_TIP_CONTRARY_LINK)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK,self.locators.TOOL_TIP_SECTION_LINK)

        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section



    # click_me_button.find_element(By.XPATH, self.locators.CLICK_ME_BUTTON).click()
    # CLICK_ME_BUTTON = ("//*[text()='Click Me']")
