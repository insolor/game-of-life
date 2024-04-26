from bitarray import bitarray


SIZE = 64


class Block:
    __slots__ = ("x", "y", "rows")

    x: int
    y: int

    rows: tuple[bitarray]  # https://pypi.org/project/bitarray/

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.rows = tuple(bitarray(SIZE) for _ in range(SIZE))

    @property
    def coords(self) -> tuple[int, int]:
        return (self.x, self.y)
    
    def __setitem__(self, local_coords: tuple[int, int], value: int) -> None:
        x, y = local_coords
        self.rows[y][x] = value
    
    def __getitem__(self, local_coords: tuple[int, int]) -> int:
        x, y = local_coords
        return self.rows[y][x]


class Field:
    __slots__ = ("blocks",)
    blocks: dict[tuple[int, int], Block]

    def __init__(self) -> None:
        self.blocks = dict()

    @staticmethod
    def convert_coords(x: int, y: int) -> tuple[tuple[int, int], tuple[int, int]]:
        return tuple(zip(divmod(x, SIZE), divmod(y, SIZE)))
    
    def __setitem__(self, coords: tuple[int, int], value: int) -> None:
        x, y = coords
        block_coords, local_coords = self.convert_coords(x, y)
        
        block = self.blocks.get(block_coords)
        if not block:
            block = Block(*block_coords)
            self.blocks[block_coords] = block
        
        block[local_coords] = value
    
    def __getitem__(self, coords: tuple[int, int]) -> int:
        x, y = coords
        block_coords, local_coords = self.convert_coords(x, y)
        
        block = self.blocks.get(block_coords)
        if not block:
            return 0
        
        return block[local_coords]
