import pyxel

from game_of_life.models import Block, Field, BLOCK_SIZE


def display_block(block: Block, scale: int, screen_x: int, screen_y: int) -> None:
    for x in range(BLOCK_SIZE):
        for y in range(BLOCK_SIZE):
            if block[x, y]:
                base_x, base_y = screen_x + x * scale, screen_y + y * scale
                pyxel.rectb(base_x, base_y, scale, scale, 15)


def display_field(field: Field, scale: int = 16) -> None:
    block = field.blocks.get((0, 0))
    if block:
        display_block(block, scale, 0, 0)
