"""File with settings and configs for this project"""

from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://USER1:123456@0.0.0.0:5432/DB1"
) # connect string for the database