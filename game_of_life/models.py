from bitarray import bitarray


class Block:
    __slots__ = ("x", "y", "rows")

    x: int
    y: int

    rows: tuple[bitarray]  # https://pypi.org/project/bitarray/

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.rows = tuple(bitarray(32) for _ in range(32))

    @property
    def coords(self):
        return (self.x, self.y)


class Field:
    __slots__ = ("blocks",)
    blocks: dict[tuple[int, int], Block]
