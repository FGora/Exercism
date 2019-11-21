def distance(strand_a, strand_b):
    if not len(strand_a)== len(strand_b):
        raise ValueError("DNA strands not the same length!")
    HammingDistance = 0
    for i in range(len(strand_a)):
        if not strand_a[i]==strand_b[i]:
           HammingDistance += 1
    return HammingDistance        