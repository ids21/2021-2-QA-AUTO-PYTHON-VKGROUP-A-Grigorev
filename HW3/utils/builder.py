from dataclasses import dataclass, asdict

import faker

fake = faker.Faker()


@dataclass
class Segment(object):
    logicType: str = None
    name: str = None
    pass_condition: int = None
    relations: list = None


@dataclass
class Campaign(object):
    name: str = None
    read_only: bool = False
    date_start: None = None
    date_end: None = None
    autobidding_mode: str = None
    budget_limit_day: None = None
    budget_limit: None = None
    conversion_funnel_id: None = None
    objective: str = None
    enable_offline_goals: bool = None
    targetings: dict = None
    age_restrictions: None = None
    uniq_shows_period: str = None
    uniq_shows_limit: None = None
    banner_uniq_shows_limit: None = None
    mixing: str = None
    utm: None = None
    enable_utm: bool = None
    price: str = None
    enable_utm = None
    max_price: str = None
    package_id: int = None
    banners: list = None


class Builder:

    @staticmethod
    def create_campaign_data():
        return asdict(
            Campaign(
                name=fake.bothify(text="Campaign ##########"),
                read_only=False,
                conversion_funnel_id=None,
                objective="reach",
                enable_offline_goals=False,
                targetings={
                    "split_audience": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                        8,
                        9,
                        10
                    ],
                    "sex": [
                        "male",
                        "female"
                    ],
                    "age": {"age_list":
                            [0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                             34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                             58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75
                             ],
                            "expand": True
                            },
                    "geo": {
                        "regions": [
                            188
                        ]
                    },
                    "interests_soc_dem": [],
                    "segments": [],
                    "interests": [],
                    "fulltime": {
                        "flags": [
                            "use_holidays_moving",
                            "cross_timezone"
                        ],
                        "mon": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                        "tue": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                        "wed": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                        "thu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                        "fri": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                        "sat": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                        "sun": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
                    },
                    "pads": [
                        102646,
                        102651,
                        102656
                    ],
                    "mobile_types": [
                        "tablets",
                        "smartphones"
                    ],
                    "mobile_vendors": [],
                    "mobile_operators": []
                },
                age_restrictions=None,
                date_start=None,
                date_end=None,
                autobidding_mode="max_shows",
                uniq_shows_period="day",
                uniq_shows_limit=None,
                banner_uniq_shows_limit=None,
                budget_limit_day="100",
                budget_limit="1000",
                mixing="recommended",
                utm=None,
                enable_utm=True,
                price="21",
                max_price="0",
                package_id=960,
                banners=[
                    {
                        "urls": {
                            "primary": {
                                "id": 55382448
                            }
                        },
                        "textblocks": {},
                        "content": {
                            "image_240x400": {
                                "id": 9663047
                            }
                        },
                        "name": ""
                    }
                ]
            )
        )

    @staticmethod
    def create_segment_data():
        return asdict(
            Segment(
                logicType='or',
                name=fake.bothify('Segment ########'),
                pass_condition=1,
                relations=[
                    {
                        "object_type": "remarketing_player",
                        "params": {"right": 0, "type": "positive", "left": 365}
                    },
                ]
            )
        )