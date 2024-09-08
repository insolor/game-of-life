from collections.abc import Iterator

BIT_MASKS = []
INVERTED_MASKS = []

_bit_mask = 1
for _ in range(64):
    BIT_MASKS.append(_bit_mask)
    INVERTED_MASKS.append(~_bit_mask)
    _bit_mask <<= 1


class BitArray64:
    __slots__ = ("value",)

    value: int

    def __init__(self, value: int = 0) -> None:
        self.value = value

    def __getitem__(self, index: int) -> int:
        return (self.value & BIT_MASKS[index]) and 1

    def __setitem__(self, index: int, value: int) -> None:
        if value:
            self.value |= 1 << index
        else:
            self.value &= INVERTED_MASKS[index]

    def __iter__(self) -> Iterator[int]:
        value = self.value
        for _ in range(64):
            yield value & 1
            value >>= 1

    def __index__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({hex(self.value)})"
