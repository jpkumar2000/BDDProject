from behave import given, when, then
from behave.log_capture import capture


@given("the user is on the search page")
def user_on_search_page(context):
    print("Called 4th")
    context.web.open("http://blazedemo.com/")
    #context.wbe.open("https://jpkumar2000.outsystemscloud.com/PreviewInDevices/?DeviceName=Desktop&URL=/WebTestApp/Entry1.aspx?_ts=636807426769853767")


@when("the user selects Paris as departure city")
def user_select_departure_city(context):
    print("Called 5th")
    context.web.find_by_xpath("//*[@name='fromPort']/option[text()='Paris']").click()

@when("the user select London as a destination city")
def user_select_destination_city(context):
    print("Called 6th")
    context.web.find_by_xpath("//select[@name='toPort']/option[text()='London']").click()

@when("clicks on the Find Flights button")
def user_clicks_on_find_flights(context):
    print("Called 7th")
    context.web.find_by_xpath("//input[@type='submit']").click()

@then("flights are presented on the search result page")
def flights_are_found(context):
    print("Called 8th")
    elements = context.web.finds_by_xpath("//table/tbody/tr")
    assert len(elements) > 1