from urllib.request import urlopen
import urllib.parse as urlparse
from urllib.parse import parse_qs
from bs4 import BeautifulSoup 
import re
import csv

def get_page_urls(url):
    base_url = "https://www.kijiji.ca"
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.findAll('a', attrs={'href': re.compile("/v-cars-trucks/city-of-toronto/*/[1-9]*")})
    links = list(map(lambda x: "{}{}".format(base_url,x['href']), links))
    return links 

def get_details(url):
    data = dict({})
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')

    data['sunroof'] = 0
    data['alloywheels'] = 0
    data['aircondition'] = 0
    data['nav'] = 0
    data['bluetooth'] = 0
    data['pushstart'] = 0
    data['parkingassist'] = 0
    data['cruisecontrol'] = 0
    data['trailerhitch'] = 0
    data['url'] = url
    try:
        data['title'] = bs.find('h1',{'class':'title-2323565163','itemprop':'name'}).text
    except:
        data['title'] = None

    try:
        data['price'] = bs.find('span',itemprop='price').text
    except:
        data['price'] = None

    try:
        data['condition'] = bs.find(itemprop='itemCondition').text
    except:
        data['condition'] = None

    try:
        data['year'] = bs.find(itemprop='vehicleModelDate').text
    except:
        data['year'] = None
    
    try: 
        data['make'] = bs.find(itemprop='brand').text
    except:
        data['make'] = None

    try:
        data['model'] = bs.find(itemprop='model').text
    except:
        data['model'] = None

    try:
        data['trim'] = bs.find(itemprop='vehicleConfiguration').text
    except:
        data['trim'] = None

    try:
        data['colour'] = bs.find(itemprop='color').text
    except:
        data['colour'] = None

    try:
        data['body'] = bs.find(itemprop='bodyType').text
    except:
        data['body'] = None

    try:
        data['doors'] = bs.find(itemprop='numberOfDoors').text
    except:
        data['doors'] = None

    try:
        data['seating'] = bs.find(itemprop='seatingCapacity').text
    except:
        data['seating'] = None

    try:
        data['transmission'] = bs.find(itemprop='vehicleTransmission').text
    except:
        data['transmission'] = None

    try:
        data['fuel'] = bs.find(itemprop='fuelType').text
    except:
        data['fuel'] = None

    try:
        data['km'] = bs.find(itemprop='mileageFromOdometer').text
    except:
        data['km'] = None

    try:
        data['description'] = bs.find(itemprop='description').text
    except:
        data['description'] = None

    try:
        data['carfax'] = bs.find('a', {'class':'attributeLink-387024144'})['href']
        parsed = urlparse.urlparse(data['carfax'])
        data['vin'] = parse_qs(parsed.query)['vin'][0]
    except:
        data['carfax'] = None
        data['vin'] = None
    try:
        includes = bs.find(id='AttributeList').prettify()

        if "Sunroof" in includes:
            data['sunroof'] = 1

        if "Alloy wheels" in includes:
            data['alloywheels'] = 1

        if "Air conditioning" in includes:
            data['aircondition'] = 1
        
        if "Navigation system" in includes:
            data['nav'] = 1

        if "Bluetooth" in includes:
            data['bluetooth'] = 1

        if "Push button start" in includes:
            data['pushstart'] = 1
        
        if "Parking assistant" in includes:
            data['parkingassist'] = 1
        
        if "Cruise control" in includes:
            data['cruisecontrol'] = 1

        if "Trailer hitch" in includes:
            data['trailerhitch'] = 1

    except:
        pass

    return data

def main():
    MAIN_DATA= []
    csv_file = "extractedData.csv"
    for i in range(100):
        print("Page:{}".format(i+1))
        url = "https://www.kijiji.ca/b-cars-trucks/city-of-toronto/page-{}/c174l1700273?ad=offering&for-sale-by=ownr".format(i+1)
        for index,page in enumerate(get_page_urls(url)):
            print("Ad:{}".format(index+1))
            extracted = get_details(page)
            MAIN_DATA.append(extracted)

        try:
            with open(csv_file, 'w', encoding="utf-8") as csvfile:
                csv_columns = MAIN_DATA[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                writer.writerows(MAIN_DATA)

        except:
            print("Error saving")

    with open(csv_file, 'w', encoding="utf-8") as csvfile:
        csv_columns = MAIN_DATA[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(MAIN_DATA)


if __name__ == "__main__":
    main()