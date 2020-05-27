from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import json


url = 'https://www.kijiji.ca/b-cars-trucks/city-of-toronto/c174l1700273?ad=offering&for-sale-by=ownr'
chrome_driver_path = './chromedriver.exe'


chrome_options = Options()
chrome_options.add_argument('--headless')
webdriver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
MASTER_URL = []
page = 1


if __name__ == "__main__":
    with webdriver as driver:
        last_page = False
        driver.get(url)
        while not last_page:
            elems = driver.find_elements_by_css_selector(".title [href]")
            links = [elem.get_attribute('href') for elem in elems]
            MASTER_URL.extend(links)
            try:
                element=driver.find_element_by_partial_link_text("Next")
                print("FOUND")
                element.click()
                page +=1

            except NoSuchElementException:
                last_page = True
                print("No element found")
                
            if page%10 == 0:
                with open('urls.json', 'w') as filehandle:
                    json.dump(MASTER_URL, filehandle)

        driver.close()


    # open output file for writing
    with open('urls.json', 'w') as filehandle:
        json.dump(MASTER_URL, filehandle)