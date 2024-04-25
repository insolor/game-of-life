import pyxel


class App:
    width: int
    height: int
    
    def __init__(self, width=1024, height=768):
        self.width = width
        self.height = height

    def run(self):
        pyxel.init(self.width, self.height)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnr(pyxel.KEY_Q):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(100, 100, 20, 20, 15)


def main():
    App().run()
