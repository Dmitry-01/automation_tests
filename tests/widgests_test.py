import time
from pages.elements_page import AutoCompletePage
from pages.widgets_page import AccordianPage, DataPickerPage, SliderPage, ProgressBarPage, TabsPage, ToolTipsPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == "What is Lorem Ipsum?" and first_content > 0
            assert second_title == "Where does it come from?" and second_content > 0
            assert third_title == "Why do we use it?" and third_content > 0

    class TestAutoCompletePage:
        def test_till_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result
            print(colors)
            print(colors_result)

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            print(count_value_before)
            print(count_value_after)
            assert count_value_before != count_value_after

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result

    class TestDatePickerPage:

        def test_change_date(self, driver):
            data_picker_page = DataPickerPage(driver, "https://demoqa.com/date-picker")
            data_picker_page.open()
            value_date_before, value_date_after = data_picker_page.select_date()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after

        def test_change_date_time(self, driver):
            data_picker_page = DataPickerPage(driver, "https://demoqa.com/date-picker")
            data_picker_page.open()
            value_date_before, value_date_after = data_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after

    class TestSliderPage:

        def test_clider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after

    class TestTabsPage:
        def test_tabs(self, driver):
            tabs = TabsPage(driver, "https://demoqa.com/tabs")
            tabs.open()
            # time.sleep(3/)
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            # more_button, more_content = tabs.check_tabs('more')
            print(what_button, what_content)
            print(origin_button, origin_content)

            assert what_button == 'What' and what_content != 0, 'the tab "What" was not pressed or the text is missing '
            assert origin_button == 'Origin' and origin_content != 0, 'the tab "Origin" was not pressed or the text is missing '
            assert use_button == 'Use' and use_content != 0, 'the tab "Use" was not pressed or the text is missing '
            assert what_button == 'More' and what_content != 0, 'the tab "More" was not pressed or the text is missing '

    class TestToolTips:

        def test_toll_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()

            assert button_text == "You hovered over the Button", "hover missding or incorrect content"
            assert field_text == "You hovered over the text field", "hover missding or incorrect content"
            assert contrary_text == "You hovered over the Contrary", "hover missding or incorrect content"
            assert section_text == "You hovered over the 1.10.32", "hover missding or incorrect content"
