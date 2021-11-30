# In a competition, the average score of a contestant is computed after discarding the best
# and worst scores. Write a function that returns the average scores of the gold medalist. 
# The raw scores of each contestant is stored in a file in the following format:
# Li Ning, 9.8 9.7 9.6 9.3 9.4, 9.8
# Millman, 9.8 9.2 9.1 9.0 9.4, 9.5 9.1
#

def getWinner(filename):
    # read file using readlines() 
    results = open(filename).readlines()       

    # initialize variables
    winner = 0  
    max_score = 0

    # process results
    for line in results:
        tokens = line.split(" ")    # split line using ',' separator   
        name = tokens[0]                  # get the name
        scores = map(float, tokens[1].split()) # get scores
        # sort scores
        
        # compute average, throwing the worst and best scores.
        ave =   sum(scores)//len(scores)                  
        if ave > max_score:
           winner =  name            # save name of highest score so far
           max_score =  ave         # save highest score

    return "%s [%.1f]" % (winner,  ave     ) 

print(getWinner(filename))