from game_of_life.models import BLOCK_SIZE, Field


def calculate_cell(field: Field, x: int, y: int) -> int:
    s = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            s += field[x + dx, y + dy]

    cell_value = field[x, y]
    s -= cell_value

    if cell_value:
        return int(s in (2, 3))
    else:
        return int(s == 3)


def field_next_step(field: Field) -> Field:
    new_field = Field()
    calculated = set()

    for (block_x, block_y), block in field.blocks.items():
        field_x = block_x * BLOCK_SIZE
        field_y = block_y * BLOCK_SIZE

        for x in range(field_x - 1, field_x + BLOCK_SIZE + 1):
            for y in range(field_y - 1, field_y + BLOCK_SIZE + 1):
                if (x, y) in calculated:
                    continue

                new_field[x, y] = calculate_cell(field, x, y)
                calculated.add((x, y))

    return new_field
