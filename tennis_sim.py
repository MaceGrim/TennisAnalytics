# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:27:01 2016

@author: Mason
"""

# Not quite done yet, but hopefully I end up with a modular tennis simulation that can be given different parameters

import random as rand

def winning_by_two(p1_score, p2_score):
    if (abs(player1_score - player2_score) >= 2):
        return True
    else:
        return False

def game_over(p1_score, p2_score):
    if (p1_score > 3 and p1_score > p2_score and winning_by_two(p1_score, p2_score)):
        return True
    if (p2_score > 3 and p2_score > p1_score and winning_by_two(p1_score, p2_score)):
        return True
    else:
        return False

def play_point(playerHS):
    randNum = rand.uniform(0, 1)
    if (randNum <= playerHS):
        return 1
    else:
        return 0

def generate_game(player1HS, player2HS):
    p1_points = 0
    p2_points = 0
    player_serving = 1
    serverHS = 0
    
    while (~game_over):
        if player_serving % 2 == 1:
            p1_points += play_point(player1HS)
        else:
            p2_points += play_point(player2HS)
        
    

def set_simulator(player1HS, player2HS):
    