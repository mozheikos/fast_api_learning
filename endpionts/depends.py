from repositories.users import UserRep
from db.base import database


def get_user_repository() -> UserRep:
    return UserRep(database)

