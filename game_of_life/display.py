from dataclasses import dataclass
from typing import TYPE_CHECKING

import pyxel

from game_of_life.models import BLOCK_SIZE

if TYPE_CHECKING:
    from game_of_life.models import Block, Field

DRAW_COLOR = pyxel.COLOR_WHITE


@dataclass
class DisplayParams:
    width: int
    height: int
    scale: int
    pixel_offset_x: int = 0
    pixel_offset_y: int = 0

    def scale_at(self, mouse_x: int, mouse_y: int, new_scale: int) -> None:
        old_scale = self.scale
        self.pixel_offset_x = (self.pixel_offset_x - mouse_x) * new_scale / old_scale + mouse_x
        self.pixel_offset_y = (self.pixel_offset_y - mouse_y) * new_scale / old_scale + mouse_y
        self.scale = new_scale

    def screen_to_field_coords(self, screen_x: int, screen_y: int) -> tuple[int, int]:
        return int((screen_x - self.pixel_offset_x) // self.scale), int((screen_y - self.pixel_offset_y) // self.scale)


def display_field(field: "Field", params: DisplayParams) -> None:
    block_pixel_size = BLOCK_SIZE * params.scale

    for (block_x, block_y), block in field.blocks.items():
        block_screen_x = block_x * block_pixel_size + params.pixel_offset_x
        if (block_screen_x + block_pixel_size) < 0 or block_screen_x > params.width:
            continue

        block_screen_y = block_y * block_pixel_size + params.pixel_offset_y
        if (block_screen_y + block_pixel_size) < 0 or block_screen_y > params.height:
            continue

        display_block(block, params, block_screen_x, block_screen_y)


def display_block(block: "Block", params: DisplayParams, screen_x: int, screen_y: int) -> None:
    for y, row in enumerate(block.rows):
        if not row.value:
            continue

        cell_screen_y = screen_y + y * params.scale
        if not (cell_screen_y + params.scale > 0 or cell_screen_y < params.height):
            continue

        for x, cell in enumerate(row):
            if not cell:
                continue

            cell_screen_x = screen_x + x * params.scale

            if not (cell_screen_x + params.scale > 0 or cell_screen_x < params.width):
                continue

            if params.scale <= 1:
                pyxel.pset(cell_screen_x, cell_screen_y, DRAW_COLOR)
            else:
                pyxel.rectb(cell_screen_x, cell_screen_y, params.scale, params.scale, DRAW_COLOR)
