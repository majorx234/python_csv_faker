#!/usr/bin/env python3
from random import randrange
from faker import Faker

# first, import a similar Provider or use the default one
from faker.providers import BaseProvider

# create new provider class extends BaseProvider
class PasswordsProvider(BaseProvider):
  # constructor
  def __init__(self, generator):
    # call constructor of base class
    super().__init__(generator)
    # set default values of class members  
    self.passwords_array = []
    self.passwords_array_size = 0
    # open files with data store it in array
    with open('passwords.txt') as passwords_file:
      for row in passwords_file:
        self.passwords_array.append(row.rstrip('\n') )
    self.passwords_array_size = len(self.passwords_array)
    
  def passwords(self):
    rand = randrange( self.passwords_array_size)	
    return self.passwords_array[rand]


if __name__ == '__main__':
  fake = Faker()	
  # then add new provider to faker instance
  fake.add_provider(PasswordsProvider)

  # now you can use:
  print(fake.passwords())
     