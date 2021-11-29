# In gene expression, mRNA is transcribed from a DNA template. The 4 nucleotide bases of A, T, C, G corresponds 
# to the U, A, G, C bases of the mRNA. Write a function that returns the mRNA transcript given the sequence of a 
# DNA strand.

def mRNAtranscription(dna_template):
    dna2rna = {'A':'U','T':'A','C':'G','G':'C' }
    mRNA = ''
    for base in dna_template:    
        if(base in dna2rna):
            mRNA+=dna2rna[base]

    return mRNA

print(mRNAtranscription("ATCGATTG"))