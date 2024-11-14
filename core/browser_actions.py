from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def set_driver(driver: webdriver):
    global _driver
    _driver = driver


def get_url():
    return _driver.current_url


def go_to(url: str):
    _driver.get(url)


def find_element(element_text: str = None, id: str = None, xpath: str = None, attempts: int = 3):
    element = None
    while element is None and attempts > 0:
        try:
            if element_text:
                search_xpath = f"//*[text()='{element_text}' or @*='{element_text}']"
                element = _driver.find_element(By.XPATH, search_xpath)
            elif id:
                element = _driver.find_element(By.ID, id)
            elif xpath:
                element = _driver.find_element(By.XPATH, xpath)
            return element

        except Exception as e:
            print(f"Error finding element: {e}")
        attempts -= 1
        sleep(1)

def find_elements(element_text: str = None, id: str = None, xpath: str = None, attempts: int = 3):
    element = None
    while element is None and attempts > 0:
        try:
            if element_text:
                search_xpath = f"//*[text()='{element_text}' or @*='{element_text}']"
                element = _driver.find_elements(By.XPATH, search_xpath)
            elif id:
                element = _driver.find_elements(By.ID, id)
            elif xpath:
                element = _driver.find_elements(By.XPATH, xpath)
            return element

        except Exception as e:
            print(f"Error finding element: {e}")
        attempts -= 1
        sleep(1)


def fill_text(element_text: str, input_text: str, id: str = None, xpath: str = None):
    find_element(element_text, id, xpath).send_keys(input_text)


def click(element_text: str = None, id: str = None, xpath: str = None):
    find_element(element_text, id, xpath).click()
