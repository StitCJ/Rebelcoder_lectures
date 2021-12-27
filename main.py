from dna_toolkit import*
from utilities import*
from structure import*
import random


# Creating a random DNA seqeunce for testing
rndDNAstr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])
DNAseq = validateSeq(rndDNAstr)

print("sequence : ", colored(DNAseq))
print("Sequence length :", len(DNAseq))
print("reverse sequence length :", len(reverse_complement(DNAseq)))
print("Nucleotide frequency :", countNucFrequency(DNAseq))
print("Transcription :", colored(transcription(DNAseq)))
print("DNA reverse complement :", reverse_complement(DNAseq))
print("5\'  ", colored(DNAseq), "  3\'")
print("    ", ''.join(["|" for c in range(len(DNAseq))]))
print("3\'  ", colored(reverse_complement(DNAseq)), "  5\'")
print(f"[5] + GC Content : {gc_content(DNAseq)}%\n")
print(f"[6] + GC content in subsection k=5 : {gc_content_subsec(DNAseq, k=5)}%\n")