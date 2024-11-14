from core import browser_actions, assertion
from helpers import json_helper

browser_actions.go_to("https://www.saucedemo.com/")
input_data = json_helper.loadJsonFile("source_demo_workflow")


def login(username, password):
    browser_actions.fill_text("username", username)
    browser_actions.fill_text("password", password)
    browser_actions.click("login-button")

    url = browser_actions.get_url()
    assertion.assert_equal("https://www.saucedemo.com/inventory.html", url, "Verify if user logged in successfully")

def get_products():
    products = browser_actions.find_elements("inventory_item")
    assertion.assert_greater_than(0, len(products), "Verify if products are available")
    return products


# main script starts from here.
username = input_data["users"][0]['username']
password = input_data["users"][0]['password']

login(username, password)
get_products()