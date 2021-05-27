from typing import List

from models import objects, MaterialFormat, DoesNotExist


async def get_material_format(media_format_id: int) -> MaterialFormat:
    try:
        material_format = await objects.get(MaterialFormat, id=media_format_id)
    except DoesNotExist:
        material_format = None
    return material_format


async def get_material_format_list() -> List[MaterialFormat]:
    material_format_list = await objects.execute(
        MaterialFormat.select().where(MaterialFormat.is_active == True).order_by('id'))
    return material_format_list
