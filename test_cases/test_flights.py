import pytest

from POM.Flights import flight_module
from Data_.reading_obj import ReadExcel
from Library.config import Config

class TestFlightDetails:
    # obj = ReadExcel()
    # data = obj.read_test_data(Config.FLIGHT_TEST_DATASHEET)

    @pytest.mark.parametrize("from_txt,to_txt",[("Hyderabad","Bengaluru"),("Tirupati","Pune")])
    def test_flights(self,_driver,from_txt,to_txt):
        flight=flight_module(_driver)
        flight.oneway()
        flight.from_textfield_btn()
        flight.enter_from_textfield(from_txt)
        flight.from_textfield_suggestion()
        flight.departure()
        flight.To_textfield_btn()
        flight.enter_To_textfield(to_txt)
        flight.To_textfield_suggestion()
        flight.flight_traveller()
        flight.enter_adult()
        flight.enter_children()
        flight.enter_infants()
        flight.enter_Travel_Class()
        flight.click_Apply()
        flight.enter_faretype_Regular()
        flight.click_Search_btn()






