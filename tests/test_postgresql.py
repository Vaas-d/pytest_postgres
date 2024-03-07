import pytest

from data.film_data import FilmData as film_data

pytestmark = pytest.mark.film


@pytest.mark.setup("new film")
@pytest.mark.teardown("remove film")
@pytest.mark.parametrize("data_amount", ["max", "min"])
def test_add_new_film(film_test_setup, data_amount) -> None:
    """Test to verify that the data submitted via UI matches the data entry in
    the actual database

    """
    connection, data = film_test_setup
    expected_result = data["film"]
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT * FROM film WHERE title='{data["film"]["title"]}';"""
        )
        result = cursor.fetchone()
        columns = [key for key in expected_result.keys()]
    actual_result = dict(zip(columns, result))
    for key in actual_result.keys():
        if key != "fulltext":
            assert actual_result[key] == expected_result[key], "Actual result does not match the Expected result"


@pytest.mark.setup("new film")
@pytest.mark.setup("update film")
@pytest.mark.test_args(film_data.update_set1)
@pytest.mark.teardown("remove film")
def test_update_existing_film(film_test_setup) -> None:
    """Test to verify that the data updates submitted via UI were successfully
    implemented on an actual entry in the database

    """
    connection, data = film_test_setup
    original_entry = data["film"]
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT * FROM film WHERE title='{data["film"]["title"]}';"""
        )
        result = cursor.fetchone()
        columns = [key for key in original_entry.keys()]
    actual_entry = dict(zip(columns, result))
    for key, value in film_data.update_set1.items():
        if key != "fulltext":
            assert actual_entry[key] != original_entry[key], "Original entry was not changed!"
            assert actual_entry[key] == value, "Actual entry does not match the test data!"