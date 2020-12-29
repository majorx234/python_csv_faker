#!/usr/bin/env python3
from random import randrange
from faker import Faker

# first, import a similar Provider or use the default one
from faker.providers import BaseProvider

# create new provider class extends BaseProvider
class GamesProvider(BaseProvider):
  # constructor
  def __init__(self, generator):
    # call constructor of base class
    super().__init__(generator)
    self.games_array = []
    self.games_array_size = 0
    # open files with data store it in array
    with open('games.txt') as games_file:
      for row in games_file:
        self.games_array.append(row.rstrip('\n') )
    self.games_array_size = len(self.games_array)
    
  def games(self):
    rand = randrange( self.games_array_size)	
    return self.games_array[rand]


if __name__ == '__main__':
  fake = Faker()	
  # then add new provider to faker instance
  fake.add_provider(GamesProvider)

  # now you can use:
  print(type(fake.games()))
     