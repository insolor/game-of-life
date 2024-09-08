from itertools import repeat
from multiprocessing import Pool, cpu_count

from game_of_life.models import BLOCK_SIZE, Field

LIVE_RULES = (2, 3)
BORN_RULES = (3,)


def calculate_cell(field: Field, x: int, y: int) -> int:
    cell_value = field[x, y]
    s = -cell_value
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            s += field[x + dx, y + dy]

    if cell_value:
        return int(s in LIVE_RULES)

    return int(s in BORN_RULES)


def calculate_block(field: Field, block_x: int, block_y: int) -> Field:
    new_field = Field()
    field_x = block_x * BLOCK_SIZE
    field_y = block_y * BLOCK_SIZE

    for x in range(field_x - 1, field_x + BLOCK_SIZE + 1):
        for y in range(field_y - 1, field_y + BLOCK_SIZE + 1):
            new_field[x, y] = calculate_cell(field, x, y)

    return new_field


def calculate_block_func(args: tuple[Field, tuple[int, int]]) -> Field:
    field, (block_x, block_y) = args
    return calculate_block(field, block_x, block_y)


def field_next_step(field: Field) -> Field:
    print("Blocks:", len(field.blocks))
    new_field = Field()

    with Pool(processes=cpu_count() - 1) as pool:
        fields = pool.imap_unordered(calculate_block_func, zip(repeat(field), field.blocks))

        for f in fields:
            new_field.merge(f)

    return new_field
