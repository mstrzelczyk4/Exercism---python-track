def proteins(strand):
    protein_dict = {
        'AUG':  'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP'
    }
    i = 0
    result = []
    while i < len(strand):
        if protein_dict[strand[i:i+3]] != 'STOP':
            result.append(protein_dict[strand[i:i+3]])
        else:
            return result
        i += 3
    return result
