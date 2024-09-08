import pyxel

from game_of_life.display import display_field
from game_of_life.engine import field_next_step
from game_of_life.library import put_object, GLIDER, SPACESHIP
from game_of_life.models import Field


class App:
    width: int
    height: int
    field: Field

    x_shift: int = 0
    y_shift: int = 0

    frame_delay: int = 4
    next_display_frame: int | None = None
    
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.scale = 16
        self.field = Field()

        put_object(self.field, SPACESHIP, 1, 1)
        put_object(self.field, GLIDER, 1, 10)

    def run(self):
        pyxel.init(self.width, self.height)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
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
            old_scale = self.scale
            self.scale = max(1, self.scale + pyxel.mouse_wheel)
            self.x_shift = self.x_shift * old_scale // self.scale
            self.y_shift = self.y_shift * old_scale // self.scale

    def draw(self):
        pyxel.cls(0)
        display_field(self.field, self.x_shift, self.y_shift, self.width // self.scale, self.height // self.scale, self.scale)

        if self.next_display_frame is None:
            self.update_next_display_frame()
        elif pyxel.frame_count >= self.next_display_frame:
            self.field = field_next_step(self.field)
            self.update_next_display_frame()

    def update_next_display_frame(self):
        self.next_display_frame = pyxel.frame_count + self.frame_delay


def main():
    App().run()
