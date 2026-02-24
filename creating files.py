# import json
#
# employee = {
#     "firstName": "Kimberly",
#     "lastName": "Alvarado",
#     "age": "19"
# }
#
# file_path = "C:\\Users\\Cess\\Desktop\\data.json"
#
# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file saved to {file_path}")
# except FileExistsError:
#     print(f"json file already exists in {file_path}")

# from htdrs import Car
# car_1 = Car('subaru', 'outback', 2018, 'blue')
# car_2 = Car('Ford', 'Mustang', 2000, 'red')
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)
#
# car_2.drive()
# car_2.stop()

import csv
import os
import random

file_path = "C:\\Users\\Cess\\Desktop.csv"

def bank_database():
    try:
        with open(file_path, "x", newline="") as file:
            writer = csv.writer(file)
    except FileExistsError:
        print("File already exists")