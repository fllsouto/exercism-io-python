from itertools import starmap
from functools import reduce

def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError("Strands should have equal size")

    zipped_strands = zip(strand_a, strand_b)
    bitmap_distance = starmap(lambda a, b: a != b, zipped_strands)
    return reduce(lambda a, b: a + b, bitmap_distance, 0)