from typing import Optional, List, Union

from models import objects, TGUser

from .material_format import get_material_format


async def get_or_create_user(user_id: int, username: Optional[str] = None) -> List[Union[TGUser, bool]]:
    user, created = await objects.get_or_create(TGUser, user_id=user_id)

    # если юзернейм указан и он не является настоящим юзернеймом (а новым)
    if username and user.username != username:
        user.username = username
        await objects.update(user, ['username'])
    return [user, created]


async def get_user_list() -> List[TGUser]:
    user_list = await objects.execute(TGUser.select().where(TGUser.blocked_by_user == False))
    return user_list


async def set_user__name(user: TGUser, name: str):
    user.name = name
    await objects.update(user, ['name'])


async def set_user__media_format(user: TGUser, media_format_id: int):
    material_format = await get_material_format(media_format_id)
    if material_format:
        user.material_format = material_format
        await objects.update(user, ['material_format'])
