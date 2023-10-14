def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if get_length(dna1) >= get_length(dna2):
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    x = 0
    for i in dna:
        if i in nucleotide:
            x = x + 1
    return x


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.find(dna2) >= 1:
        return True
    else:
        return False


def is_valid_sequence(dna):
    """ (str) -> bool



    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGS')
    False
    >>> is_valid_sequence('ATcGGC')
    False

    the parameter is a potential DNA sequence. Return True if and only if the DNA sequence is valid"""
    n = "ATCGTTTTTT"
    if count_nucleotides(dna, n) == get_length(dna):
        return True
    else:
        return False


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index

    >>> insert_sequence('CCGG', 'AT',2)
    "CCATGG"
    """
    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.

    >>> get_complement("A")
    "T"
    """
    ans = ""
    complements = {"A": "T",
                   "G": "C",
                   "T": "A",
                   "C": "G"}
    for i in nucleotide:
        if i in complements:
            ans = ans + complements[i]
    return ans


def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence("AT")
    "TA"
    """
    return get_complement(dna)
