from dataclasses import dataclass

import pyxel

from game_of_life.models import Field


@dataclass
class DisplayParams:
    x_start: int
    y_start: int
    x_end: int
    y_end: int
    pixel_offset_x: int
    pixel_offset_y: int
    scale: int = 16


def display_field(field: Field, params: DisplayParams) -> None:
    for x in range(params.x_start, params.x_end):
        screen_x = (x - params.x_start) * params.scale + params.pixel_offset_x
        for y in range(params.y_start, params.y_end):
            if field[x, y]:
                screen_y = (y - params.y_start) * params.scale + params.pixel_offset_y
                pyxel.rectb(screen_x, screen_y, params.scale, params.scale, 15)
