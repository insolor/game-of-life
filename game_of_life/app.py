import pyxel
from game_of_life.display import display_field

from game_of_life.library import glider
from game_of_life.models import Field


class App:
    width: int
    height: int
    field: Field
    
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
        # pyxel.rect(100, 100, 20, 20, 15)
        display_field(self.field, )


def main():
    App().run()
