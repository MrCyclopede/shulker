import json

from typing import Union

from shulker.components.BlockCoordinates import BlockCoordinates
from shulker.components.NBT import NBT

from shulker.functions.base_functions import *


def meta_summon(entity: str, coords: BlockCoordinates, nbt_data: NBT) -> dict:
    instructions = {"list": []}
    instructions["list"].append(f"summon {entity} {coords} {nbt_data}")
    return instructions


def summon(
    entity: str,
    coords: Union[BlockCoordinates, tuple],
    nbt_data: Union[NBT, dict, str]
) -> Union[bool, str]:
    """
    Returns a bool that is set to True
    if no message was sent back by the game or the
    message itself if there was an issue

    Summons an entity
    """

    check_output_channel()
    
    # Get the list of entity from registries.json
    with open("mc_data/registries.json", "r") as f:
        registries = json.load(f)
        entities = registries["minecraft:entity_type"]["entries"]
        
    if type(entity) is not str:
        raise TypeError(f"Expected type str, got {type(entity)}")
    elif entity.replace("minecraft:", "") not in entities.replace("minecraft:", ""):
        raise ValueError(f"Entity {entity} is not a valid entity")
    
    coords = format_arg(coords, BlockCoordinates)
    nbt_data = format_arg(nbt_data, NBT)

    instructions = meta_summon(entity, coords, nbt_data)

    for line in instructions["list"]:
        status = post(line)

    return True if status.startswith("") else status
