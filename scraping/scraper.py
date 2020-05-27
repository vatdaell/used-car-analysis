import json
import pickle 
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time


class Car():
    def __init__(self):
        self.year = None
        self.make = None
        self.model = None
        self.trim = None
        self.body = None
        self.condition = None
        self.km = None
        self.transmission = None
        self.drivetrain = None
        self.colour = None
        self.fuel = None
        self.doors = None
        self.seats = None
        self.sunroof = 0
        self.alloy_wheels = 0
        self.navigation_system = 0
        self.bluetooth = 0
        self.push_start = 0
        self.parking_assist = 0
        self.cruise_control = 0
        self.trailer_hitch = 0
        self.air_conditioning = 0
        self.description = None
        self.price = 0
        self.title = None
        self.location = None
        self.condition = None
        self.url = None


def kijiji_scraper(driver:webdriver) -> Car:
    car = Car()
    available = True
    try:
        car.title = driver.find_element_by_class_name('title-2323565163').text
        car.price = driver.find_element_by_class_name("currentPrice-2842943473").text
        car.location = driver.find_element_by_class_name("address-3617944557").text
        car.description = driver.find_element_by_class_name("descriptionContainer-3544745383").text
    except Exception:
        available = False
        print("Listing Unavailable")

    if available:
        try:
            driver.find_element_by_class_name("showMoreButton-4078245409").click()
        except Exception:
            print("No extra info")

        try:
            attributes = driver.find_elements_by_tag_name("dd")[1:]
            labels = driver.find_elements_by_tag_name("dt")
            for index,attr in enumerate(attributes):
                label = labels[index].text
                attribute = attr.text

                # Based on the label set the attribute
                if label == "Year":
                    car.year = attribute
                elif label == "Make":
                    car.make = attribute
                elif label == "Model":
                    car.model = attribute
                elif label == "Trim":
                    car.trim = attribute
                elif label == "Body Type":
                    car.body = attribute
                elif label == "Condition":
                    car.condition = attribute
                elif label == "Kilometers":
                    car.km = attribute
                elif label == "Condition":
                    car.condition = attribute
                elif label == "Transmission":
                    car.transmission = attribute
                elif label == "Drivetrain":
                    car.drivetrain = attribute
                elif label == "Colour":
                    car.colour = attribute
                elif label == "Fuel Type":
                    car.fuel = attribute
                elif label == "No. of Doors":
                    car.doors = attribute
                elif label == "No. of Seats":
                    car.seats = attribute
                
        except Exception:
            print("Listing Unavailable")

        try:
            boolean_attr = driver.page_source
            if "Sunroof" in boolean_attr:
                car.sunroof = 1
            if "Alloy wheels" in boolean_attr:
                car.alloy_wheels = 1
            if "Navigation system" in boolean_attr:
                car.navigation_system = 1
            if "Bluetooth" in boolean_attr:
                car.bluetooth = 1
            if "Push button start" in boolean_attr:
                car.push_start = 1
            if "Parking assistant" in boolean_attr:
                car.parking_assist = 1
            if "Cruise control" in boolean_attr:
                car.cruise_control = 1
            if "Trailer hitch" in boolean_attr:
                car.trailer_hitch = 1
            if "Air conditioning" in boolean_attr:
                car.air_conditioning = 1

        except Exception:
            print("Features bool error")


    return car

def kijiji_autos_scraper(parameter_list):
    pass

if __name__ == "__main__":
    chrome_driver_path = './chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument('--headless')
    webdriver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    MASTER_LOAD = []
    with webdriver as driver:
        with open('urls.json') as json_file:
            data = json.load(json_file)
            unq_data = (np.unique(data))
            driver.set_page_load_timeout(30)
            rate_lim = 1
            for index, url in enumerate(unq_data):
                print("Listing: {}".format(index+1))
                try:
                    
                    if index >= 0:
                        if(rate_lim == 10):
                            rate_lim = 0
                            time.sleep(60)

                        driver.get(url)
                        rate_lim += 1
                        if "kijijiautos.ca" in url:
                            pass
                        else:
                            car=kijiji_scraper(driver) 
                            car.url = url
                            MASTER_LOAD.append(car)
                            """
                            print(car.title)
                            print(car.price)
                            print(car.location)
                            print(car.year)
                            print(car.make)
                            print(car.model)
                            print(car.trim)
                            print(car.body)
                            print(car.condition)
                            print(car.km)
                            print(car.condition)
                            print(car.transmission)
                            print(car.drivetrain)
                            print(car.colour)
                            print(car.fuel)
                            print(car.doors)
                            print(car.seats)
                            print(car.sunroof)
                            print(car.alloy_wheels)
                            print(car.navigation_system)
                            print(car.bluetooth)
                            print(car.push_start)
                            print(car.parking_assist)
                            print(car.cruise_control)
                            print(car.trailer_hitch)
                            print(car.air_conditioning)
                            """
                        if index%10 == 0:
                            with open("stored_car_data.pkl", 'wb') as pickle_file:
                                pickle.dump(MASTER_LOAD, pickle_file)
                except Exception as e:
                    print(str(e))

                
    driver.close()
                    
    with open("stored_car_data.pkl", 'wb') as pickle_file:
        pickle.dump(MASTER_LOAD, pickle_file)