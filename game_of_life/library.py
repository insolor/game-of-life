from game_of_life.models import Field

GLIDER = """
 X
  X
XXX
""".strip("\n")

SPACESHIP = """
X  X
    X
X   X
 XXXX
""".strip("\n")


def put_object(field: Field, obj: str, x: int, y: int):
    for i, row in enumerate(obj.splitlines()):
        for j, item in enumerate(row):
            if item != " ":
                field[x+j, y+i] = 1
