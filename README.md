# Game of Life

Classic [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

Plans

- [ ] implement gui using [pyxel](https://github.com/kitao/pyxel)
  - [ ] display field on the screen
  - [ ] field editor
- [ ] infinite field:
  - field is split into 32x32 (or 64x64) blocks, where each line in a block is an integer, where each cell is a bit
- [ ] game loop

See [models.py](game_of_life/models.py) for inner implementation of the game field.


## Running

```
poetry run app
```
or
```
python -m game_of_life
```
from an activated venv

or
```
pyxel run main.py
```
