# A DNA strand consisting of the 4 nucleotide bases is usually represented with a string of letters: A,T, C, G. 
# Write a function that computes the base composition of a given DNA sequence.

def baseComposition(dna_seq):
    dict_count={'A':0,'C':0,'T':0,'G':0}
    for i in dna_seq:
        if(i in dict_count):
            dict_count[i]+=1
    return dict_count

print(baseComposition("CTATCGGCACCCTTTCAGCA"))
print(baseComposition("AGT"))