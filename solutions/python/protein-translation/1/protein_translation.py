def proteins(strand):
    STOP = ['UAA', 'UAG', 'UGA']
    mapping = {
        'AUG':'Methionine',
        'UUU':'Phenylalanine',
        'UUC':'Phenylalanine',
        'UUA':'Leucine',
        'UUG':'Leucine',
        'UCU':'Serine',
        'UCC':'Serine',
        'UCA':'Serine',
        'UCG':'Serine',
        'UAU':'Tyrosine',
        'UAC':'Tyrosine',
        'UGU':'Cysteine',
        'UGC':'Cysteine',
        'UGG':'Tryptophan'
    }

    result = []
    start = 0

    while start+3 <= len(strand):
        codon = strand[start:start+3]
        if codon in STOP:
            return result
        result.append(mapping[codon])
        start += 3

    return result
