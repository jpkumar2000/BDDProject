from behave import use_fixture
from web.fixtures import browser_chrome
from web_source.web_factory import get_web

def before_all(context):
    print("Method called fist before_all")
    web_object = get_web(context.config.userdata['browser'])
    context.web = web_object