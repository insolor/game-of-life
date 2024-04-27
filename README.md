# Game of Life

Classic [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

Plans

- [ ] implement gui using [pyxel](https://github.com/kitao/pyxel)
  - [ ] display field on the screen
    - [x] display one block
    - [ ] display visible part of the field
    - [ ] pan field with the middle mouse button
    - [ ] change scale with the mouse wheel
  - [ ] field editor
- [x] infinite field:
  - field is split into 32x32 (or 64x64) blocks, where each line in a block is an integer, where each cell is a bit
- [x] game loop

See [models.py](game_of_life/models.py) for inner implementation of the game field.

## Online demo

https://insolor.github.io/game-of-life/

## Running locally
Install dependencies
```
poetry install
```
Then run
```
poetry run app
```
Or
```
python -m game_of_life
```
from an activated venv.

Or
```
pyxel run main.py
```

## Building to html
```
make all
```
