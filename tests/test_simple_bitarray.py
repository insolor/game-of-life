from game_of_life.simple_bitarray import BitArray64


def test_bitarray_to_int():
    assert int(BitArray64(123)) == 123


def test_bitarray_repr():
    assert str(BitArray64(123)) == "BitArray64(123)"


def test_bitarray_set():
    bitarray = BitArray64()
    bitarray[0] = 1
    assert int(bitarray) == 1
    bitarray[1] = 1
    assert int(bitarray) == 3


def test_bitarray_get():
    source_bits = "10110101"
    bitarray = BitArray64(int(source_bits, 2))
    
    for i, (source_bit, bit) in enumerate(zip(reversed(source_bits), bitarray)):
        source_bit = int(source_bit)
        assert bitarray[i] == source_bit
        assert bit == source_bit
