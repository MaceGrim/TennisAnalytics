import numpy as np

def MatchWinner(server1p, server2p, GS):
    winner = 'Player 0'
    if(GS == 1):
        n = 60
        n1 = 30
        w = 3
    if(GS == 0):
        n = 36
        n1 = 18
        w = 2
    matchstring = list(range(n))
    for i in range(n1):
        matchstring[2*i] = np.random.binomial(1, server1p)
        matchstring[2*i+1] =  np.random.binomial(1, 1-server2p)
    matchscore = [0,0]
    tempscore = [0,0]
    for i in range(n):
        if(matchstring[i] == 1):
            tempscore[0] += 1
        if(matchstring[i] == 0):
            tempscore[1] += 1
        if(tempscore[0] == 6):
            if(tempscore[1] < 5):
                matchscore[0] += 1
                tempscore = [0,0]
        if(tempscore[1] == 6):
            if(tempscore[0] < 5):
                matchscore[1] += 1
                tempscore = [0,0]
        if(tempscore[0] == 7):
            matchscore[0] += 1
            tempscore = [0,0]
        if(tempscore[1] == 7):
            matchscore[1] += 1
            tempscore = [0,0]
        if((tempscore[0] == 6) &  (tempscore[1] == 6)):
            tiebraker = np.random.binomial(1, .5)
            matchscore[tiebraker] += 1
            tempscore = [0,0]
        if(matchscore[0] == w):
            winner = 0
            matchscore = [-10,-10]
        if(matchscore[1] == w):
            winner = 1
            matchscore = [-10,-10] 
    return winner 

def MonteCarlo(server1p, server2p, GS, matches_to_sim):
    sum = 0.0
    for i in range(matches_to_sim):
        sum = sum + MatchWinner(server1p,server2p, GS)
    player1win = (matches_to_sim-sum)/float(matches_to_sim)
    return player1win