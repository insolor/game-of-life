import pyxel

from game_of_life.display import DisplayParams, display_field
from game_of_life.engine import field_next_step
from game_of_life.library import GLIDER, SPACESHIP, put_object
from game_of_life.models import Field


class App:
    width: int
    height: int
    field: Field
    display_params: DisplayParams

    frame_delay: int = 4
    next_display_frame: int | None = None

    def __init__(self, width: int = 800, height: int = 600) -> None:
        self.width = width
        self.height = height
        self.field = Field()

        scale = 16
        self.display_params = DisplayParams(
            x_start=0,
            y_start=0,
            x_end=self.width // scale,
            y_end=self.height // scale,
            scale=scale,
        )

        put_object(self.field, SPACESHIP, 1, 1)
        put_object(self.field, GLIDER, 1, 10)

    def run(self) -> None:
        pyxel.init(self.width, self.height)
        pyxel.mouse(visible=True)
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if pyxel.btnr(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.MOUSE_BUTTON_MIDDLE):
            # start view panning
            ...

        if pyxel.btnr(pyxel.MOUSE_BUTTON_MIDDLE):
            # finish view panning
            ...

        if pyxel.mouse_wheel:
            # change the scale using the mouse wheel
            old_scale = self.display_params.scale
            new_scale = max(1, old_scale + pyxel.mouse_wheel)
            self.display_params.scale = new_scale
            self.display_params.x_start = self.display_params.x_start * old_scale // new_scale
            self.display_params.y_start = self.display_params.y_start * old_scale // new_scale

    def draw(self) -> None:
        pyxel.cls(0)
        display_field(self.field, self.display_params)

        if self.next_display_frame is None:
            self.update_next_display_frame()
        elif pyxel.frame_count >= self.next_display_frame:
            self.field = field_next_step(self.field)
            self.update_next_display_frame()

    def update_next_display_frame(self) -> None:
        self.next_display_frame = pyxel.frame_count + self.frame_delay


def main() -> None:
    App().run()
