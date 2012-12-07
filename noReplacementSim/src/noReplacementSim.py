import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    count = 0.0
    for i in range(numTrials):
        bucket = ['R', 'R', 'R', 'G', 'G', 'G']
        draw = ''
        for i in range(3):
            ball = random.choice(bucket)
            bucket.pop(bucket.index(ball))
            draw += ball
        if draw == 'RRR' or draw == 'GGG':
            count += 1
    return count/numTrials

for i in range(10):        
    print noReplacementSimulation(100000)

    