#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 30 18:55:19 2020
@author: Lotte&Major
"""
import csv
from faker import Faker
import datetime
from games_provider import GamesProvider
from random import randrange

def primaryKeygenerator(list_of_used_game_user_touples):  
  while True: 
    gameid = randrange(10) 
    userid = randrange(10) 
    if gameid in list_of_used_game_user_touples :  
      list_of_used_user_touples = list_of_used_game_user_touples[gameid]
      if userid in list_of_used_user_touples : 
        print("bewertung gibts schon, neu random")
      else : 
        list_of_used_user_touples[userid] = "true"   
        list_of_used_game_user_touples[gameid] = list_of_used_user_touples 
        break
    else:  
      list_of_used_game_user_touples[gameid] =  { userid : "true" } 
      break   
  return gameid, userid, list_of_used_game_user_touples

def datagenerate(records, headers):
    fake = Faker('en_US')
    fake.add_provider(GamesProvider)

    with open("ratings_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        
        # erstelle Müllbeutel = leer
        list_of_used_game_user_touples = {}
        
        for i in range(records):
            graphic_value = randrange(5) + 1
            sound_value   = randrange(5) + 1
            addict_value  = randrange(5) + 1
            gameid, userid, list_of_used_game_user_touples = primaryKeygenerator( list_of_used_game_user_touples )
            
            writer.writerow({
                "Graphic" : graphic_value,
                "Sound" : sound_value,
                "AddictiveScore": addict_value,
                "OptionalComment": fake.sentence(),
                "UserId": userid,
                "GameId": gameid
            })
    
if __name__ == '__main__':
    records = 10
    headers = ["Graphic","Sound","AddictiveScore","OptionalComment","UserId", "GameId"]
    datagenerate(records, headers)
    print("CSV generation complete!")


