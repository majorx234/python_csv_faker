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

    with open("games_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            gameid = i
            name = fake.games()
            description = fake.sentence()
            publicationdate = fake.date()
            developer = name + "studios"
            trailerurl = "https://www.google.com/search?q="+name

            writer.writerow({
                "GameId" : gameid,
                "Name" : name,
                "Description": description,
                "Publicationdate": publicationdate,
                "Developer": developer,
                "TrailerUrl": trailerurl
            })
    
if __name__ == '__main__':
    records = 10
    headers = ["GameId","Name","Description","Publicationdate","Developer","TrailerUrl"]
    datagenerate(records, headers)
    print("CSV generation complete!")
