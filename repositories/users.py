import datetime
from .base import BaseRep
from typing import List, Optional, Any, Coroutine
from db.models import users
from models.user import User, UserIn
from core.security import hash_passwd


class UserRep(BaseRep):

    async def get_all(self, limit: int = 100, skip: int = 0) -> Optional[List[User]]:
        query = users.select().limit(limit).offset(skip)
        users_list = await self.session.fetch_all(query)
        return [User.parse_obj(x) for x in users_list]

    async def get_by_id(self, pk: int) -> Optional[User]:
        query = users.select().where(users.c.id == pk).first()
        user = await self.session.fetch_one(query)
        if not user:
            return
        return User.parse_obj(user)

    async def get_by_username(self, username: str) -> Optional[User]:
        pass

    async def create(self, instance: UserIn) -> User:

        user = User(
            username=instance.username,
            name=instance.name,
            lastname=instance.lastname,
            hashed_password=hash_passwd(instance.password),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )

        values = {**user.dict()}
        values.pop("id", None)
        print(values)
        query = users.insert().values(**values)
        user.id = await self.session.execute(query)
        return user

    async def update(self, instance: UserIn) -> Coroutine[Any, Any, Optional[User]]:
        pass
