#!/usr/bin/env python3

from faker import Faker
fake = Faker()

# first, import a similar Provider or use the default one
from faker.providers import BaseProvider

# create new provider class
class FooProvider(BaseProvider):
    def foo(self):
        return 'bar'

# then add new provider to faker instance
fake.add_provider(FooProvider)

# now you can use:
print(fake.foo())
print(type(fake.foo()))

# 'bar'        