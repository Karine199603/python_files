import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ------------------- Browser fixture -------------------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://lms.threadqa.ru/xpath-practice-hub")
    yield driver
    driver.quit()


# ------------------- Helper function -------------------
def get_username_field(driver, timeout=10):
    """Waits until the username input field is visible and returns it"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-testid='username-field']")
        )
    )


# ------------------- Tests -------------------
def test_username_field_accepts_text(driver):
    field = get_username_field(driver)
    assert field.get_attribute("placeholder") == "Введите ваше имя"
    field.send_keys("Karine")
    assert field.get_attribute("value") == "Karine"


def test_username_field_can_be_cleared(driver):
    field = get_username_field(driver)
    field.send_keys("text_to_clear")
    field.clear()
    assert field.get_attribute("value") == ""


def test_username_field_accept_digits(driver):
    field = get_username_field(driver)
    field.send_keys("123")
    assert field.get_attribute("value") == "123"