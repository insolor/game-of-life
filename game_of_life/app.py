import pyxel


class App:
    def __init__(self):
        pyxel.init(1024, 768)
        pyxel.mouse(True)

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnr(pyxel.KEY_Q):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(100, 100, 20, 20, 15)


def main():
    App().run()
