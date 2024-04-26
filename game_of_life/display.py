import pyxel
from game_of_life.models import Block, Field, SIZE


def display_block(block: Block, scale: int, screen_x: int, screen_y: int) -> None:
    for x in range(SIZE):
        for y in range(SIZE):
            if block[x, y]:
                base_coords = screen_x + x * scale, screen_y + y * scale
                pyxel.rectb(*base_coords, scale, scale, 15)


def display_field(field: Field, scale: int = 16) -> None:
    block = field.blocks[0, 0]
    display_block(block, scale, 0, 0)
