from game_of_life.simple_bitarray import BitArray64


def test_bitarray_to_int():
    assert int(BitArray64(123)) == 123


def test_bitarray_repr():
    value = 123
    assert str(BitArray64(value)) == f"BitArray64({hex(value)})"


def test_bitarray_set():
    bitarray = BitArray64()
    bitarray[0] = 1
    assert int(bitarray) == 1
    bitarray[1] = 1
    assert int(bitarray) == 3
    bitarray[2] = 0
    assert int(bitarray) == 3
    bitarray[1] = 0
    assert int(bitarray) == 1


def test_bitarray_get():
    source_bits = "10110101"
    bitarray = BitArray64(int(source_bits, 2))

    for i, (source_bit_str, bit) in enumerate(zip(reversed(source_bits), bitarray, strict=False)):
        source_bit = int(source_bit_str)
        assert bitarray[i] == source_bit
        assert bit == source_bit
