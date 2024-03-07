# [Boilerplate] Testing postgreSQL databse with pytest and psycopg2

## Description:
Basic boilerplate to start testing postgresql databases using pytest and psycopg2 library.
This boilerplate utilizes [PostgreSQL Sample Database](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)
as a test database. The database needs to be set up to be able to run these tests.
Test reports are generated via `pytest-html` plugin.

### 1. Install python environment:
All the requirements for this boilerplate are already in the `pipfile` and `pipfile.lock`. 
You need only to clone the project and set up python virtual environment.
```
  python -m pip install --upgrade pip
  pip install pipenv
  pipenv install --system
```

### 2. Run tests:
Run all set of tests:
```
pytest
```
Run one particular test:
```
pytest -k <name of the test>
```
Run tests marked with a specific mark:
```
pytest -m <name of pytest mark>
```

### 3. Generate report:
There is no need to call pytest-html directly. Everything has been done in **pytest.ini**. 
A self-contained html report is generated automatically after the test execution.