


class Block:
    __slots__ = ("x", "y", "rows")

    x: int
    y: int

    rows: tuple[int]  # TODO: use tuple of bitarray: https://bitstring.readthedocs.io/en/stable/index.html
    
    def __init__(self) -> None:
        self.rows = tuple(0 for _ in range(32))
    
    @property
    def coords(self):
        return (self.x, self.y)


class Field:
    __slots__ = ("blocks",)
    blocks: dict[tuple[int, int], Block]
