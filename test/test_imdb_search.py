
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.imdb_search_page import IMDbSearchPage
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_imdb_search(driver):
    # Create an instance of the IMDbSearchPage
    search_page = IMDbSearchPage(driver)

    # Load the IMDb search page
    search_page.load()

    # Enter search data into the form fields
    search_page.enter_name('Brad Pitt')  # Example name
    search_page.select_gender('male')  # Example gender selection
    search_page.enter_birth_date('1963')  # Example birth date

    # Perform the search
    search_page.click_search()

    # Validate the search result (e.g., check for the presence of a result)
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'lister-item-header'))
        # Replace with actual locator for search results
    )
