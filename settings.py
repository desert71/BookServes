"""File with settings and configs for this project"""

from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
) # connect string for the database

TEST_DATABASE_URL = env.str(
    "TEST_DATABASE_URL",
    default="postgresql+asyncpg://postgres_test:postgres_test@localhost:5433/postgres_test"
) # connect string for the test database