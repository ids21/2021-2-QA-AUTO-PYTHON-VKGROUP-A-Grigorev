from dataclasses import dataclass

import faker

fake = faker.Faker()


class Builder:

    @staticmethod
    def topic(title=None, text=None):

        @dataclass
        class Topic:
            title: str = None
            text: str = None
            id: int = None

        if title is None:
            title = fake.lexify(text='??????? ??? ???')

        if text is None:
            text = fake.bothify(text='????? ?? ?? ?? #### ???#?#? #### ?? ??# ###')

        return Topic(title=title, text=text)
