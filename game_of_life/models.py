from game_of_life.simple_bitarray import BitArray64

BLOCK_SIZE = 64


class Block:
    __slots__ = ("rows",)

    rows: tuple[BitArray64, ...]

    def __init__(self) -> None:
        self.rows = tuple(BitArray64() for _ in range(BLOCK_SIZE))
    
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
        block_x, local_x = divmod(x, BLOCK_SIZE)
        block_y, local_y = divmod(y, BLOCK_SIZE)
        return (block_x, block_y), (local_x, local_y)
    
    def __setitem__(self, coords: tuple[int, int], value: int) -> None:
        x, y = coords
        block_coords, local_coords = self.convert_coords(x, y)
        
        block = self.blocks.get(block_coords)
        if not block:
            if not value:
                return  # Don't create a new block, if the value is empty

            block = Block()
            self.blocks[block_coords] = block
        
        block[local_coords] = value
    
    def __getitem__(self, coords: tuple[int, int]) -> int:
        x, y = coords
        block_coords, local_coords = self.convert_coords(x, y)
        
        block = self.blocks.get(block_coords)
        if not block:
            return 0
        
        return block[local_coords]
