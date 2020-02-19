def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Lengths are not equal")
    return sum([strand_a[i] != strand_b[i] for i in range(len(strand_a))])
