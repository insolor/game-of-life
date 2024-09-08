# Game of Life

[![Tests](https://github.com/insolor/game-of-life/actions/workflows/pytest.yml/badge.svg)](https://github.com/insolor/game-of-life/actions/workflows/pytest.yml)
[![Deploy](https://github.com/insolor/game-of-life/actions/workflows/deploy.yml/badge.svg)](https://github.com/insolor/game-of-life/actions/workflows/deploy.yml)
[![Run in browser](https://img.shields.io/badge/Demo-run-blue)](https://insolor.github.io/game-of-life/)

Classic [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

Plans

- [x] infinite field:
  - field is split into 32x32 (or 64x64) blocks, where each line in a block is an integer number, where each bit is a cell
  - the whole field is a dict where keys are block coordinates and values are blocks  
    See [models.py](game_of_life/models.py) for inner implementation of the game field.
- [x] game loop
- [ ] implement gui using [pyxel](https://github.com/kitao/pyxel)
  - [x] display field on the screen
    - [x] draw visible part of the field
    - [x] change scale with the mouse wheel
    - [x] pan field view with the middle mouse button
  - [x] controls (start/stop, step buttons)
  - [x] edit with the mouse, clear the field
  - [ ] add a help screen
- [ ] optimizations:
  - [ ] use parallelization (blocks can be processed independently, so it's possible to process subsets of blocks in different threads/processes)
  - [ ] rewrite parts in cython?

## Online demo

<https://insolor.github.io/game-of-life/>

## Running locally

Install dependencies

```shell
poetry install
```

Then run

```shell
poetry run app
```

Or using [poethepoet](https://github.com/nat-n/poethepoet):

```shell
poe run
```

Or

```shell
poetry shell  # activate the virtual environment
python -m game_of_life
```

Or

```shell
poetry shell
pyxel run main.py
```

Or

```shell
make run
```

## Building to html

```shell
make all
```
