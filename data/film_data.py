import datetime
import random

from decimal import Decimal
from lorem_text import lorem


class FilmData:

    ratings = ("PG", "R", "NC-17", "PG-13", "G")

    update_set1 = {
        "rental_duration": random.randint(15, 20),
        "rental_rate": Decimal(random.randint(10, 100)),
        "replacement_cost": Decimal(random.randint(10, 100))
    }

    @staticmethod
    def new_film_data(amount: str) -> dict:
        payload = {
            "film_id": random.randint(1000, 9999),
            "title": lorem.words(3),
            "description": lorem.sentence() if amount == "max" else None,
            "release_year": random.randint(1990, 2024) if amount == "max" else None,
            "language_id": random.randint(1, 6),  # the number of language ids from the language table
            "rental_duration": random.randint(1, 14),
            "rental_rate": Decimal(random.randint(10, 100)),
            "length": random.randint(1, 3) if amount == "max" else None,
            "replacement_cost": Decimal(random.randint(10, 100)),
            "rating": random.choice(FilmData.ratings) if amount == "max" else None,
            "last_update": datetime.datetime.now(),
            "special_features": [lorem.words(1)] if amount == "max" else None,
            "fulltext": "{test}"
        }
        return payload



