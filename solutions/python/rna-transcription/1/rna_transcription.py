def to_rna(dna_strand):
    rna_dna_mapping = {
        'G':'C',
        'C':'G',
        'T':'A',
        'A':'U'
    }

    rna_strand = []

    for char in dna_strand:
        rna_strand.append(rna_dna_mapping[char])

    return ''.join(char for char in rna_strand)