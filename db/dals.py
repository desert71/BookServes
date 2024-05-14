from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User

###########################################################
# BLOCK FOR INTERACTION WITH DATABASE IN BUSINESS CONTEXT #
###########################################################


class UserDAL:
    """Data Access layer for operating user info"""
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create_user(
            self, name: str, surname: str, email: str
    ) -> User:
        new_user = User(
            name=name,
            surname=surname,
            email=email,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
    