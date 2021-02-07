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
import hashlib

def datagenerate(records, headers):
    fake = Faker('en_US')

    fake.add_provider(PasswordsProvider)

    with open("users_data3.csv", 'wt') as csvFile:
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
            password = fake.passwords()
            premd5password = password.encode()
            md5password = hashlib.md5(premd5password)
            md5password_digest = md5password.hexdigest()
            writer.writerow({
                "UserId" : userId,
                "FirstName" : Fname,
                "LastName": Lname,
                "UserName": username,
                "Password":  md5password_digest,
                "Email": email
            })
            print("user: " + username + " password: " + password + " hash: " + md5password_digest )   
    
if __name__ == '__main__':
    records = 10
    headers = ["UserId","FirstName","LastName","UserName","Email","Password" ]
    datagenerate(records, headers)
    print("CSV generation complete!")
