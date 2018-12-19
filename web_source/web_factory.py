from selenium import webdriver
from web.SeleniumWeb import WebObject


def get_web(browser):
    print("Method get_web is triggered second")
    if browser == "chrome":
        return WebObject(webdriver.Chrome("C:/Pradeep/chromedriver.exe"))