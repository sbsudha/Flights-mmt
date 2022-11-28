from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(20)

@when('open make_my_trip page')
def openpage(context):
    context.driver.get("https://www.makemytrip.com/")
    context.driver.maximize_window()
    time.sleep(2)
@then('click flight module')
def flightmodule(context):
    context.driver.find_element_by_xpath('//li[@data-cy="menu_Flights"]').click()
    time.sleep(3)

@then('click oneway Trip')
def oneway(context):
    context.driver.find_element_by_xpath('//li[@data-cy="oneWayTrip"]').click()
    time.sleep(2)

@then('enter the From places "Bengaluru"')
def From(context):
    context.driver.find_element_by_xpath('//span[text()="From"]').click()
    time.sleep(2)
    context.driver.find_element("xpath",'//input[@placeholder="From"]').send_keys("Bengaluru")
    time.sleep(2)
    context.driver.find_element("xpath",'//li[@class="react-autosuggest__suggestion react-autosuggest__suggestion--first"]').click()
    time.sleep(2)


@then('click the Departure')
def Departure(context):
    context.driver.find_element_by_xpath("//div[text()='December 2022']/../..//div[@aria-label='Mon Dec 05 2022']").click()
    time.sleep(2)

@then('enter the To places "Pune"')
def To(context):
    context.driver.find_element("xpath", '//span[text()="To"]').click()
    time.sleep(2)
    context.driver.find_element("xpath", '//input[@aria-controls="react-autowhatever-1"]').send_keys("Pune")
    time.sleep(2)

    context.driver.find_element("xpath", '//li[@class="react-autosuggest__suggestion react-autosuggest__suggestion--first"]').click()
    time.sleep(2)


@then('click the TRAVELLERS & CLASS')
def Travellers(context):
    context.driver.find_element("xpath", '//div[@data-cy="flightTraveller"]').click()
    time.sleep(2)
    context.driver.find_element("xpath", '//li[@data-cy="adults-2"]').click()
    time.sleep(2)
    context.driver.find_element("xpath", '//li[@data-cy="children-1"]').click()
    time.sleep(2)
    context.driver.find_element("xpath", '//li[@data-cy="infants-0"]').click()
    context.driver.find_element("xpath", '//li[text()="Economy/Premium Economy"]').click()

@then('click on Apply')
def Apply(context):
    context.driver.find_element("xpath", '//button[text()="APPLY"]').click()
    time.sleep(2)

@then('click the Fare type')
def Faretype(context):
    context.driver.find_element("xpath", '//p[text()="Regular "]').click()
    time.sleep(2)

@then('click on search')
def search(context):
    context.driver.find_element("xpath", '//a[text()="Search"]').click()
    time.sleep(2)

@then('close browser')
def closeBrowser(context):
    context.driver.close()







