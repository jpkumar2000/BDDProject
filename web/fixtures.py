from selenium import webdriver
from .SeleniumWeb import WebObject


def browser_chrome(context, timeout=30, **kwargs):
    browser = webdriver.Chrome("C:/Pradeep/chromedriver.exe")
    web_object = WebObject(browser)
    context.web = web_object
    yield context.web
    browser.quit()