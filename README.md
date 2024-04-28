# Game of Life 
[![Tests](https://github.com/insolor/game-of-life/actions/workflows/pytest.yml/badge.svg)](https://github.com/insolor/game-of-life/actions/workflows/pytest.yml)
[![Deploy](https://github.com/insolor/game-of-life/actions/workflows/deploy.yml/badge.svg)](https://github.com/insolor/game-of-life/actions/workflows/deploy.yml)
[![Run in browser](https://img.shields.io/badge/Demo-run-blue)](https://insolor.github.io/game-of-life/)

Classic [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

Plans

- [x] infinite field:
  - field is split into 64x64 blocks, where each line in a block is an integer number, where each bit is a cell
  - the whole field is a dict where keys are block coordinates and values are blocks  
    See [models.py](game_of_life/models.py) for inner implementation of the game field.
- [x] game loop
- [ ] implement gui using [pyxel](https://github.com/kitao/pyxel)
  - [ ] display field on the screen
    - [x] draw visible part of the field
    - [ ] pan field view with the middle mouse button
    - [ ] change scale with the mouse wheel
  - [ ] controls (start/stop, step, clear buttons)
  - [ ] field editor



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
