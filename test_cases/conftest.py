import time

import pytest
from selenium import webdriver
from Library.config import Config
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=["Chrome","Firefox","Edge"])

def _driver(request):

    if request.param == "Chrome":
         driver = webdriver.Chrome(executable_path=Config.Chrome_Driver_Path)


    elif request.param == "Firefox":
        options = Options()
        options.binary_location= r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path,options=options)
        time.sleep(10)

    else:
         driver = webdriver.Edge(executable_path=Config.Edge_Driver_Path)

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    print(driver.title)
    # driver.save_screenshot("text_flights.png")
    driver.close()





