# from selenium import webdriver
# import time
# path=r"C:\Users\Sudha\Downloads\chromedriver_win32\chromedriver.exe"
# driver= webdriver.Chrome(path)
# driver.get("https://www.makemytrip.com/")
# driver.maximize_window()
# time.sleep(2)
# driver.implicitly_wait(30)

from Library.config import Config
from Data_.reading_obj import ReadExcel
import time

class flight_module:
    obj_1 = ReadExcel()
    locator_flight = obj_1.read_locator(Config.FLIGHT_LOCATOR_SHEET)

    def __init__(self,driver):
        self.driver = driver

    def oneway(self):
        locator = self.locator_flight["oneway_trip"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def from_textfield_btn(self):
        locator = self.locator_flight["oneway_from_textfield_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def enter_from_textfield(self,from_txt):
        locator = self.locator_flight["from_textfield"]
        self.driver.find_element(*locator).send_keys(from_txt)
        time.sleep(2)

    def from_textfield_suggestion(self):
        locator = self.locator_flight["from_textfield_dropdown"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def departure(self):
        locator = self.locator_flight["oneway_departure"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def To_textfield_btn(self):
        locator = self.locator_flight["oneway_To_textfield_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def enter_To_textfield(self,to_txt):
        locator = self.locator_flight["To_textfield"]
        self.driver.find_element(*locator).send_keys(to_txt)
        time.sleep(2)

    def To_textfield_suggestion(self):
        locator = self.locator_flight["To_textfield_dropdown"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def flight_traveller(self):
        locator = self.locator_flight['flight_traveller']
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def enter_adult(self):
        locator = self.locator_flight["flight_traveller_adult"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def enter_children(self):
        locator = self.locator_flight["flight_traveller_children"]
        self.driver.find_element(*locator).click()

    def enter_infants(self):
        locator = self.locator_flight["flight_traveller_infants"]
        self.driver.find_element(*locator).click()

    def enter_Travel_Class(self):
        locator = self.locator_flight["choose_Travel_Class"]
        self.driver.find_element(*locator).click()

    def click_Apply(self):
        locator = self.locator_flight["click_Apply_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def enter_faretype_Regular(self):
        locator = self.locator_flight["faretype_Regular"]
        self.driver.find_element(*locator).click()

    def click_Search_btn(self):
        locator = self.locator_flight["Search_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(2)









