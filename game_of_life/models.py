import functools

from game_of_life.simple_bitarray import BitArray64

BLOCK_SIZE = 32


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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.rows})"


class Field:
    __slots__ = ("blocks",)
    blocks: dict[tuple[int, int], Block]

    def __init__(self) -> None:
        self.blocks = {}

    @staticmethod
    @functools.cache
    def _convert_to_block_coords(x: int, y: int) -> tuple[tuple[int, int], tuple[int, int]]:
        """
        Convert a field coordinates to block coordinates
        """
        block_x, local_x = divmod(x, BLOCK_SIZE)
        block_y, local_y = divmod(y, BLOCK_SIZE)
        return (block_x, block_y), (local_x, local_y)

    def __setitem__(self, coords: tuple[int, int], value: int) -> None:
        block_coords, local_coords = self._convert_to_block_coords(*coords)

        block = self.blocks.get(block_coords)
        if not block:
            if not value:
                return  # Don't create a new block, if the value is empty

            block = Block()
            self.blocks[block_coords] = block

        block[local_coords] = value

    def __getitem__(self, coords: tuple[int, int]) -> int:
        block_coords, local_coords = self._convert_to_block_coords(*coords)

        block = self.blocks.get(block_coords)
        if not block:
            return 0

        return block[local_coords]

    def clear(self) -> None:
        self.blocks = {}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.blocks})"
