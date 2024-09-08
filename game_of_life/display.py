from dataclasses import dataclass

import pyxel

from game_of_life.models import Field


@dataclass
class DisplayParams:
    width: int
    height: int
    pixel_offset_x: int
    pixel_offset_y: int
    scale: int = 16


def display_field(field: Field, params: DisplayParams) -> None:
    x_start, x_offset = divmod(-params.pixel_offset_x, params.scale)
    y_start, y_offset = divmod(-params.pixel_offset_y, params.scale)
    x_end = x_start + params.width / params.scale
    y_end = y_start + params.height / params.scale

    for x in range(int(x_start), int(x_end) + 1):
        screen_x = (x - x_start) * params.scale - x_offset
        for y in range(int(y_start), int(y_end) + 1):
            if field[x, y]:
                screen_y = (y - y_start) * params.scale - y_offset
                pyxel.rectb(screen_x, screen_y, params.scale, params.scale, 15)
