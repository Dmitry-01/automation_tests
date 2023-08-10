import random
import time
from datetime import date

from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select

from generator.generator import generated_date
from locators.widgets_page_locators import AccordianPageLocators, DataPickerLocators, SliderLocators, \
    ProgressBarLocators
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

