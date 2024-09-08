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


def field_next_step(field: Field) -> Field:
    new_field = Field()
    calculated = set()

    for block_x, block_y in field.blocks:
        field_x = block_x * BLOCK_SIZE
        field_y = block_y * BLOCK_SIZE

        for x in range(field_x - 1, field_x + BLOCK_SIZE + 1):
            for y in range(field_y - 1, field_y + BLOCK_SIZE + 1):
                if (x, y) in calculated:
                    continue

                new_field[x, y] = calculate_cell(field, x, y)
                calculated.add((x, y))

    return new_field
