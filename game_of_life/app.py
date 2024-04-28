import pyxel

from game_of_life.display import display_field
from game_of_life.engine import field_next_step
from game_of_life.library import put_object, GLIDER, SPACESHIP
from game_of_life.models import Field


class App:
    width: int
    height: int
    field: Field

    frame_delay: int = 4
    next_display_frame: int | None = None
    
    def __init__(self, width=1024, height=768):
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
    
    def draw(self):
        pyxel.cls(0)
        display_field(self.field, 0, 0, self.width // self.scale, self.height // self.scale, self.scale)

        if self.next_display_frame is None:
            self.update_next_display_frame()
        elif pyxel.frame_count >= self.next_display_frame:
            self.field = field_next_step(self.field)
            self.update_next_display_frame()

    def update_next_display_frame(self):
        self.next_display_frame = pyxel.frame_count + self.frame_delay


def main():
    App().run()
