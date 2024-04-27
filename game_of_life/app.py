import pyxel

from game_of_life.display import display_field
from game_of_life.engine import field_next_step
from game_of_life.library import glider
from game_of_life.models import Field


class App:
    width: int
    height: int
    field: Field

    frame_delay: int = 10
    next_display_frame: int | None = None
    
    def __init__(self, width=1024, height=768):
        self.width = width
        self.height = height
        self.field = Field()
        
        glider(self.field, 1, 1)

    def run(self):
        pyxel.init(self.width, self.height)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnr(pyxel.KEY_Q):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(0)
        display_field(self.field)

        if self.next_display_frame is None:
            self.update_next_display_frame()
        elif pyxel.frame_count >= self.next_display_frame:
            self.field = field_next_step(self.field)
            self.update_next_display_frame()

    def update_next_display_frame(self):
        self.next_display_frame = pyxel.frame_count + self.frame_delay


def main():
    App().run()
