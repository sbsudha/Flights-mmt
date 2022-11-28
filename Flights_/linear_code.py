from selenium import webdriver
import time

path=r"C:\Users\Sudha\Downloads\chromedriver_win32\chromedriver.exe"

driver_obj= webdriver.Chrome(path)
driver_obj.get("https://www.makemytrip.com/")

driver_obj.maximize_window()
time.sleep(2)


"oneway"
driver_obj.find_element("xpath",'//li[@data-cy="oneWayTrip"]').click()
driver_obj.find_element("xpath",'//span[text()="From"]').click()
driver_obj.find_element("xpath",'//input[@placeholder="From"]').send_keys("Hyderabad")
time.sleep(2)
driver_obj.find_element("xpath",'//li[@class="react-autosuggest__suggestion react-autosuggest__suggestion--first"]').click()
time.sleep(2)

## driver_obj.find_element("xpath",'//label[@for="departure"]')
driver_obj.find_element_by_xpath("//div[text()='December 2022']/../..//div[@aria-label='Mon Dec 05 2022']").click()
time.sleep(2)
driver_obj.find_element("xpath",'//span[text()="To"]').click()
driver_obj.find_element("xpath",'//input[@aria-controls="react-autowhatever-1"]').send_keys("Pune")
time.sleep(2)

driver_obj.find_element("xpath",'//li[@class="react-autosuggest__suggestion react-autosuggest__suggestion--first"]').click()
time.sleep(2)
driver_obj.find_element("xpath",'//div[@data-cy="flightTraveller"]').click()
driver_obj.find_element("xpath",'//li[@data-cy="adults-2"]').click()
driver_obj.find_element("xpath",'//li[@data-cy="children-1"]').click()
driver_obj.find_element("xpath",'//li[@data-cy="infants-0"]').click()
driver_obj.find_element("xpath",'//li[text()="Economy/Premium Economy"]').click()
time.sleep(2)
driver_obj.find_element("xpath",'//button[text()="APPLY"]').click()
time.sleep(2)
driver_obj.find_element("xpath",'//p[text()="Regular "]').click()
# driver_obj.find_element("xpath",'//p[text()="Student "]').click()
driver_obj.find_element("xpath",'//a[text()="Search"]').click()
driver_obj.close()