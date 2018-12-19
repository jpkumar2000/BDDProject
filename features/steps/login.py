from behave import given, when, then
from behave.log_capture import capture


@given("the user is on the login page")
def user_on_login_page(context):
    print("Called 4th")
    #context.web.open("http://blazedemo.com/")
    context.web.open("https://jpkumar2000.outsystemscloud.com/PreviewInDevices/?DeviceName=Desktop&URL=/WebTestApp/Entry1.aspx?_ts=636807426769853767")


@when("the user enters the username")
def user_enters_username(context):
    print("Called 5th")
    context.web.switch_to_frame("iframe")
    context.web.find_by_xpath('//*[@id="OutSystemsUIWeb_wt14_block_wtLogin_OutSystemsUIWeb_wt15_block_wtLogin_OutSystemsUIWeb_wt26_block_wtInput_wtUserNameInput"]').send_keys("jpkumar2000@gmail.com")
    #context.web.find_by_ID("OutSystemsUIWeb_wt14_block_wtLogin_OutSystemsUIWeb_wt15_block_wtLogin_OutSystemsUIWeb_wt26_block_wtInput_wtUserNameInput").send_keys("jpkumar2000@gmail.com")
    context.web.switch_to_default()

@when("the user enters the password")
def user_enters_password(context):
    print("Called 6th")
    context.web.switch_to_frame("iframe")
    context.web.find_by_xpath("//*[@id='OutSystemsUIWeb_wt14_block_wtLogin_OutSystemsUIWeb_wt15_block_wtLogin_OutSystemsUIWeb_wt6_block_wtInput_wtPasswordInput']").send_keys("pradeep@1977")
    context.web.switch_to_default()

@when("clicks on the Log In button")
def user_clicks_on_Log_In_Button(context):
    print("Called 7th")
    context.web.switch_to_frame("iframe")
    context.web.find_by_xpath("//*[@id='OutSystemsUIWeb_wt14_block_wtLogin_OutSystemsUIWeb_wt15_block_wtLogin_wt13']").click()
    context.web.switch_to_default()

@then("request page will be loaded")
def request_form_is_loaded(context):
    print("Called 8th")
    #context.web.find_ids("wt41_OutSystemsUIWeb_wt2_block_wtContent_wtMainContent_OutSystemsUIWeb_wt28_block_wtColumn1_OutSystemsUIWeb_wt25_block_wtContent_wtShortDescription")
    context.web.switch_to_frame("iframe")
    elements = context.web.finds_by_xpath("//*[@id='wt41_OutSystemsUIWeb_wt2_block_wtContent_wtMainContent_OutSystemsUIWeb_wt28_block_wtColumn1_OutSystemsUIWeb_wt25_block_wtContent_wtShortDescription']")
    context.web.switch_to_default()
    assert len(elements) > 0
    #context.web.switch_to_default()