from dataclasses import dataclass

import pyxel

from game_of_life.display import DisplayParams, display_field
from game_of_life.engine import field_next_step
from game_of_life.library import GLIDER, SPACESHIP, put_object
from game_of_life.models import Field

SCALING_MULTIPLIER = 1.25


@dataclass
class PanningParams:
    initial_mouse_x: int
    initial_mouse_y: int
    initial_offset_x: int
    initial_offset_y: int

    def offset_x(self, mouse_x: int) -> int:
        return self.initial_offset_x + mouse_x - self.initial_mouse_x

    def offset_y(self, mouse_y: int) -> int:
        return self.initial_offset_y + mouse_y - self.initial_mouse_y


class App:
    field: Field
    display_params: DisplayParams
    panning_params: PanningParams | None = None

    frame_delay: int = 4
    next_display_frame: int | None = None

    running: bool = True
    step: bool = False

    def __init__(self, width: int = 800, height: int = 600) -> None:
        self.field = Field()

        self.display_params = DisplayParams(
            width=width,
            height=height,
            scale=16,
        )

        put_object(self.field, SPACESHIP, 1, 1)
        put_object(self.field, GLIDER, 1, 10)

    def run(self) -> None:
        pyxel.init(self.display_params.width, self.display_params.height)
        pyxel.mouse(visible=True)
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if pyxel.btnr(pyxel.KEY_Q):
            pyxel.quit()

        self.panning()
        self.scaling()
        self.running_controls()
        self.edit()

    def panning(self) -> None:
        if pyxel.btnr(pyxel.MOUSE_BUTTON_MIDDLE):
            # finish view panning
            self.panning_params = None

        if self.panning_params:
            # recalculate offset during the panning
            self.display_params.pixel_offset_x = self.panning_params.offset_x(pyxel.mouse_x)
            self.display_params.pixel_offset_y = self.panning_params.offset_y(pyxel.mouse_y)
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_MIDDLE):
            # start view panning
            self.panning_params = PanningParams(
                initial_mouse_x=pyxel.mouse_x,
                initial_mouse_y=pyxel.mouse_y,
                initial_offset_x=self.display_params.pixel_offset_x,
                initial_offset_y=self.display_params.pixel_offset_y,
            )

    def running_controls(self) -> None:
        if pyxel.btnr(pyxel.KEY_SPACE):
            self.running = not self.running

        if pyxel.btnr(pyxel.KEY_RETURN):
            self.running = False
            self.step = True

        if pyxel.btnr(pyxel.KEY_RIGHT):
            if not self.running:
                self.running = True
            else:
                self.frame_delay = max(1, self.frame_delay - 1)

        if pyxel.btnr(pyxel.KEY_LEFT):
            if not self.running:
                self.running = True
            else:
                self.frame_delay = self.frame_delay + 1

    def scaling(self) -> None:
        """
        Change the scale using the mouse wheel
        """
        if pyxel.mouse_wheel:
            old_scale = self.display_params.scale
            new_scale = max(1, old_scale * SCALING_MULTIPLIER**pyxel.mouse_wheel)
            self.display_params.scale_at(pyxel.mouse_x, pyxel.mouse_y, new_scale)

    def edit(self) -> None:
        if self.running:
            return

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            field_x, field_y = self.display_params.screen_to_field_coords(pyxel.mouse_x, pyxel.mouse_y)
            self.field[field_x, field_y] = 1

        if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            field_x, field_y = self.display_params.screen_to_field_coords(pyxel.mouse_x, pyxel.mouse_y)
            self.field[field_x, field_y] = 0

        if pyxel.btnr(pyxel.KEY_F12):
            self.field.clear()

    def draw(self) -> None:
        pyxel.cls(0)
        display_field(self.field, self.display_params)

        if self.next_display_frame is None:
            self.update_next_display_frame()
        elif pyxel.frame_count >= self.next_display_frame and (self.running or self.step):
            self.field = field_next_step(self.field)
            self.update_next_display_frame()

            self.step = False

    def update_next_display_frame(self) -> None:
        self.next_display_frame = pyxel.frame_count + self.frame_delay


def main() -> None:
    App().run()


if __name__ == "__main__":
    main()
