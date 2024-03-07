import os

import psycopg2
import pytest

from dotenv import dotenv_values
from data.film_data import FilmData as film_data


root_dir = os.path.dirname(os.path.abspath(__file__))
config = dotenv_values(f"{root_dir}/.env")


@pytest.fixture()
def setup_markers(request) -> tuple:
    markers = list(request.node.iter_markers())
    setup = [marker.args[0] for marker in markers if marker.name == "setup"]
    teardown = [marker.args[0] for marker in markers if marker.name == "teardown"]
    args = [marker.args[0] for marker in markers if marker.name == "test_args"]
    params = [marker.args[0] for marker in markers if marker.name == "parametrize"]
    return setup, teardown, args, params


@pytest.fixture(scope="function")
def new_connection() -> None:
    with psycopg2.connect(
            host=config["HOST"],
            user=config["USER"],
            password=config["PASSWORD"],
            database=config["DB_NAME"],
            port=config["PORT"]
    ) as conn:
        print(type(conn))
        yield conn


@pytest.fixture(scope="function")
def film_test_setup(new_connection, setup_markers, request) -> tuple:
    connection = new_connection
    setup, teardown, args, params = setup_markers
    amount = request.node.callspec.id if len(params) != 0 else "min"
    data = {"film": film_data.new_film_data(amount=amount)}

    if "new film" in setup:
        columns = ', '.join([f"%({key})s" for key in data["film"].keys()])
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO film VALUES({columns});""", data["film"]
            )

    if "update film" in setup:
        updates = args[0]
        for key, value in updates.items():
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""UPDATE film SET {key}={value};""",
                )

    yield connection, data

    if "remove film" in teardown:
        film_id = data["film"]["film_id"]
        with connection.cursor() as cursor:
            cursor.execute(
                f"""DELETE FROM film WHERE film_id='{film_id}';"""
            )
