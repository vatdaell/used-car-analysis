import pickle
import csv
from scraper import Car



def transform_data(x):
    data = {
        "price":x.price,
        "location":x.location,
        "year":x.year,
        "make":x.make,
        "model":x.model,
        "trim":x.trim,
        "body":x.body,
        "title":x.title,
        "condition":x.condition,
        "km":x.km,
        "condition":x.condition,
        "transmission":x.transmission,
        "drivetrain":x.drivetrain,
        "colour":x.colour,
        "fuel":x.fuel,
        "doors":x.doors,
        "seats":x.seats,
        "sunroof":x.sunroof,
        "alloy_wheels":x.alloy_wheels,
        "navigation_system":x.navigation_system,
        "bluetooth":x.bluetooth,
        "push_start":x.push_start,
        "parking_assist":x.parking_assist,
        "cruise_control":x.cruise_control,
        "trailer_hitch":x.trailer_hitch,
        "air_conditioning":x.air_conditioning,
        "description": x.description,
        "url":x.url,
    }

    return data




cars = pickle.load( open( "car_storage.pkl", "rb" )) 
cars_transformed = list(map(transform_data, cars))
cars_1 = pickle.load( open( "car_storage_1.pkl", "rb" )) 
cars_transformed_1 = list(map(transform_data, cars))
cars_2 = pickle.load( open( "car_storage_2", "rb" )) 
cars_transformed_2 = list(map(transform_data, cars))
cars_3 = pickle.load( open( "car_storage_3", "rb" )) 
cars_transformed_3 = list(map(transform_data, cars))

csv_file = "data.csv"
try:
    with open(csv_file, 'w',  encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=cars_transformed[0].keys())
        writer.writeheader()
        for data in cars_transformed:
            writer.writerow(data)

        for data in cars_transformed_1:
            writer.writerow(data)

        for data in cars_transformed_2:
            writer.writerow(data)

        for data in cars_transformed_3:
            writer.writerow(data)

        
except IOError:
    print("I/O error")

