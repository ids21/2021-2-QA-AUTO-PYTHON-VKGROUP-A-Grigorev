from dataclasses import dataclass

import faker

fake = faker.Faker()


@dataclass
class User(object):
    username: str = None
    password: str = None
    email: str= None

class Builder:

    @staticmethod
    def create_user():
        return User(
                username=fake.lexify('????????'),
                password=fake.bothify('????????##'),
                email=fake.email(),

            )
