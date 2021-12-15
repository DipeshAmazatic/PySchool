# Pairwise comparision of DNA sequences is a popular technique used in Bioinformatics. It usually involves 
# some scoring scheme to express the degree of similarity. Write a function that compares two DNA 
# sequences based on the following scoring scheme: +1 for a match, +3 for each consecutive match and -1 
# for each mismatch.

def pairwiseScore(seqA, seqB):
    count=0
    flg=0
    if(len(seqA)==len(seqB)):
        for i,j in enumerate(seqA):
            if(j==seqB[i]):
                count+=1
                if(flg==0):
                    index=i
                    flg=1
                if((index+1)==i):
                    count+=2
                    index=i
                    flg=1
            else:
                count-=1
                flg=0
        return count
    else:
        return "Length of string are not same"



print(pairwiseScore("ATTCGT", "ATCTAT"))
print(pairwiseScore("GATAAATCTGGTCT", "CATTCATCATGCAA"))