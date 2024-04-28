import pyxel

from game_of_life.models import Field


def display_field(field: Field, x_start, y_start, x_end, y_end, scale: int = 16) -> None:
    for x in range(x_start, x_end):
        screen_x = (x - x_start) * scale
        for y in range(y_start, y_end):
            if field[x, y]:
                screen_y = (y - y_start) * scale
                pyxel.rectb(screen_x, screen_y, scale, scale, 15)
