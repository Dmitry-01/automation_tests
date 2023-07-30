import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    # Строка ниже позволяет автоматически скачивать последнюю версию chromedriver
    # Благодаря этой команде запускается и открывается наш браузер

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager(version='114.0.5735.90').install())

    driver.maximize_window()
    yield driver
    driver.quit()