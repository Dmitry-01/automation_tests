import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownload, DynamicPropertiesPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_field_form()

            assert input_data == output_data

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "Yes have not been selected"
            assert output_impressive == 'Impressive', "Impressive have not been selected"
            assert output_no == 'No', "No have not been selected"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            print(table_result)
            assert key_word in table_result, "The person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            time.sleep(3)
            web_table_page.search_some_person(lastname)
            print(lastname)
            time.sleep(3)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            print(age)
            print(row)
            assert age in row, "The person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            time.sleep(3)
            web_table_page.search_some_person(email)
            time.sleep(3)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert  text == "No rows found"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], "The number of rows in the table has not been changed or has changed incorrectly"

    class TestButtonPage:

        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'x')
            button_page.open()
            double = button_page.click_on_the_diffrent_button('double')
            right = button_page.click_on_the_diffrent_button('right')
            click = button_page.click_on_the_diffrent_button('click')

            assert double == 'You have done a double click', 'The double click button was not pressed'
            assert right == 'You have done a right click', 'The right click button was not pressed'
            assert click == 'You have done a dynamic click', 'The dynamic click button was not pressed'

    class TestLinksPage:

        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        def test_broken_link(self,driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "the link works or the status code in son 400"

    class TestUploadAndDownload:

        def test_upload_file(self, driver):
            upload_and_download = UploadAndDownload(driver, 'https://demoqa.com/upload-download')
            upload_and_download.open()
            fale_name , result = upload_and_download.upload_file()
            assert fale_name == result, "the file has not been uploaded"

        def test_download_file(self, driver):
            upload_and_download = UploadAndDownload(driver, 'https://demoqa.com/upload-download')
            upload_and_download.open()
            check = upload_and_download.download_file()
            assert check is True, "the file has not been downloaded"

    class TestDynamicPropertiesPage:


        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed()
            assert color_before != color_after, "colors have not been changed"

        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()

            assert appear is True, "button didn't appear after 5 second"

        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()

            assert enable is True, "button didn't enable after 5 second"

