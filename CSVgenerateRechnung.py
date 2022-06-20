#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:55:19 2019
@author: krishnaparekh
"""

#Rg_ID(pk),Rg_KdID(fk),Rg_Datum,Rg_Summe,Rg_AnzPos

import csv
from random import randrange
from faker import Faker
from faker.providers import date_time

def datagenerate(records, headers):
    fake = Faker('de_DE')

    fake.add_provider(date_time)
    
    with open("rechnung.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            Rg_ID = i
            Rg_KdID = randrange(10)
            Rg_Datum = fake.date()
            Rg_Summe = (randrange(10)+1) * 1000 -1
            Rg_AnzPos = randrange(5)

            writer.writerow({
                "Rg_ID" : Rg_ID,
                "Rg_KdID" : Rg_KdID,
                "Rg_Datum": Rg_Datum,
                "Rg_Summe": Rg_Summe,
                "Rg_AnzPos": Rg_AnzPos
            })
    
if __name__ == '__main__':
    records = 10
    headers = ["Rg_ID","Rg_KdID","Rg_Datum","Rg_Summe","Rg_AnzPos"]
    datagenerate(records, headers)
    print("CSV generation complete!")
