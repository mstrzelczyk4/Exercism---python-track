def to_rna(dna_strand):
    rna_dict = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    rna = ""
    for x in dna_strand:
        rna += rna_dict[x]
    return rna
