#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:55:19 2019
@author: krishnaparekh
"""

#Kd_ID(pk),Kd_Firma,Kd_Strasse,Kd_PLZ,Kd_Ort

import csv
from faker import Faker
from faker.providers import company 
from faker.providers import address

def datagenerate(records, headers):
    fake = Faker('de_DE')

    fake.add_provider(company)
    fake.add_provider(address)

    with open("kunde.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            Kd_ID = i
            Kd_Firma = fake.company()
            Kd_Strasse = fake.street_address()
            Kd_PLZ = fake.postcode()
            Kd_Ort = fake.city()

            writer.writerow({
                "Kd_ID" : Kd_ID,
                "Kd_Firma" : Kd_Firma,
                "Kd_Strasse": Kd_Strasse,
                "Kd_PLZ": Kd_PLZ,
                "Kd_Ort": Kd_Ort
            })
    
if __name__ == '__main__':
    records = 10
    headers = ["Kd_ID","Kd_Firma","Kd_Strasse","Kd_PLZ","Kd_Ort"]
    datagenerate(records, headers)
    print("CSV generation complete!")
