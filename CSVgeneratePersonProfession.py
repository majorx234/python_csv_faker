#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:55:19 2019
@author: krishnaparekh
"""

#Person_Profession_Id(PK),firstname,lastname,profession

import csv
from faker import Faker
from faker.providers import person 
from faker.providers import job

def datagenerate(records, headers):
    fake = Faker('de_DE')

    fake.add_provider(person)
    fake.add_provider(job)

    with open("person_profession.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            person_profession_id = i
            firstname = fake.first_name()
            lastname = fake.last_name()
            profession = fake.job()

            writer.writerow({
                "person_profession_id" : person_profession_id,
                "firstname" : firstname,
                "lastname": lastname,
                "profession": profession
            })
    
if __name__ == '__main__':
    records = 10
    headers = ["person_profession_id","firstname","lastname","profession"]
    datagenerate(records, headers)
    print("CSV generation complete!")
