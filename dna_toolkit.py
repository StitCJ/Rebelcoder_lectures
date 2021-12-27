import collections
from structure import*
import random

# Check the sequence to make sure it is a DNA string
def validateSeq(dna_seq) :
    """Check the sequence to make sure it is valid DNA string."""
    
    tmpseq = dna_seq.upper()
    for nuc in tmpseq :
        if nuc not in Nucleotides :
            return False
        return tmpseq
    
def countNucFrequency(seq) :
    """Count nucleodite frequency"""
    
    #tmpFreDict = { "A" : 0, "C" : 0, "G" : 0, "T" : 0}
    #for nuc in seq :
    #    tmpFreDict[nuc] += 1
    #return tmpFreDict
    return dict(collections.Counter(seq))
 
def transcription(seq) :
    """DNA -> RNA Transcription. Replace Thymine with Uracil"""
    return seq.replace("T", "U")
 
def reverse_complement(seq) :
    """A<->T, G<->C. Reversing newly generated string"""
    # return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[ : : -1]

def gc_content(seq) :
    """GC content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count("G")) / len(seq) * 100)

def gc_content_subsec(seq, k=20) :
    """GC content in a DNA/RNA sub-sequence length k, k = 20 by default"""
    res = []
    for i in range(0, len(seq) -k + 1, k) :
        subseq = seq[i: i + k]
        res.append(gc_content(subseq))
    return res
    
def read_file(filepath) :
    """Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
# FasFile = read_file(filepath)
# FasDic = {}
# Faslabel = ""
# for line in FasFile :
#     if '>' in line :
#         Faslabel = line
#         FasDic[Faslabel] = ""
#     else :
#         FasDic[Faslabel] += line