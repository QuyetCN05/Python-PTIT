# import csv


# file_path = 'addresses.csv'


# with open(file_path, 'r', newline='') as csvfile:
   
#     csvreader = csv.reader(csvfile)

   
#     for row in csvreader:
#         s=row[5]
#         print(s)

import csv

with open('addresses.csv','r') as csvfile:
    f=csv.reader(csvfile)
    for row in f:
        s=row[5].strip()
        print(s)
