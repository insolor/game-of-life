from dataclasses import dataclass

import pyxel

from game_of_life.models import Field

DRAW_COLOR = pyxel.COLOR_WHITE


@dataclass
class DisplayParams:
    width: int
    height: int
    pixel_offset_x: int
    pixel_offset_y: int
    scale: int = 16

    def scale_at(self, mouse_x: int, mouse_y: int, new_scale: int) -> None:
        old_scale = self.scale
        self.pixel_offset_x = (self.pixel_offset_x - mouse_x) * new_scale / old_scale + mouse_x
        self.pixel_offset_y = (self.pixel_offset_y - mouse_y) * new_scale / old_scale + mouse_y
        self.scale = new_scale


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
                if params.scale <= 1:
                    pyxel.pset(screen_x, screen_y, DRAW_COLOR)
                else:
                    pyxel.rectb(screen_x, screen_y, params.scale, params.scale, DRAW_COLOR)
