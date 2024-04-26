from game_of_life.models import Field


def glider(field: Field, x: int, y: int):
    #  X
    #   X
    # XXX
    
    field[x + 1, y + 0] = 1
    field[x + 2, y + 1] = 1
    field[x + 0, y + 2] = 1
    field[x + 1, y + 2] = 1
    field[x + 2, y + 2] = 1
