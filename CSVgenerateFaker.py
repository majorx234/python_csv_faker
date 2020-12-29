#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:55:19 2019
@author: krishnaparekh
"""

import csv
from faker import Faker
import datetime
from games_provider import GamesProvider
from passwords_provider import PasswordsProvider

def datagenerate(records, headers):
    fake = Faker('en_US')

    fake.add_provider(PasswordsProvider)
    fake.add_provider(GamesProvider)

    with open("users_data2.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            userId = i
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            email = Fname +"."+ Lname + domain_name
            username = Fname + "X234"
            writer.writerow({
                "UserID" : userId,
                "FirstName" : Fname,
                "LastName": Lname,
                "Email": email,
                "UserName": username,
                "Password": fake.passwords(),
                "Lieblingsgame": fake.games()
            })
    
if __name__ == '__main__':
    records = 10
    headers = ["UserID","FirstName","LastName","UserName","Password","Email","Lieblingsgame" ]
    datagenerate(records, headers)
    print("CSV generation complete!")
