import random
import sys
import os
from enum import Enum

# author:  margaret swarts
# date:    8/20/19
# description: This file is an implementation of a deck of cards


class Suit(Enum):
    HEART = 1
    DIAMOND = 2
    SPADE = 3
    CLUB = 4


class card:
    def __init__(self, rank, Suit, value):
        self.rank = rank
        self.Suit = Suit
        self.value = value


# create deck
deck = []

for count1 in range(1, 5):
    for count2 in range(1, 14):
        for count3 in range(1, 14):
                i = card(None, None, None)
                i.rank = count2
                i.Suit = count1
                if(count3 < 11):
                    i.value = count3
                else:
                    i.value = 10
                deck.append(i)


def print_card(deck, x):
    if(deck[x].Suit ==1):
        if(deck[x].rank == 11):
            print('Jack of Hearts')
        elif(deck[x].rank == 12):
            print('Queen of Hearts')
        elif(deck[x].rank == 13):
            print('King of Hearts')
        else:
            print(deck[x].rank, 'of Hearts')
    elif(deck[x].Suit == 2):
        if(deck[x].rank == 11):
            print('Jack of Diamonds')
        elif(deck[x].rank == 12):
            print('Queen of Diamonds')
        elif(deck[x].rank == 13):
            print('King of Diamonds')
        else:
            print(deck[x].rank, 'of Diamonds')
    elif(deck[x].Suit == 3):
        if(deck[x].rank == 11):
            print('Jack of Spades')
        elif(deck[x].rank == 12):
            print('Queen of Spades')
        elif(deck[x].rank == 13):
            print('King of Spades')
        else:
            print(deck[x].rank, 'of Spades')
    else:
        if(deck[x].rank == 11):
            print('Jack of Clubs')
        elif(deck[x].rank == 12):
            print('Queen of Clubs')
        elif(deck[x].rank == 13):
            print('King of Clubs')
        else:
            print(deck[x].rank, 'of Clubs')

#create random hands
pc_hand = []
my_hand = []
crib = []
test_hand = [card(5, 1, 5), card(5, 2, 5), card(12, 1, 10), card(13, 1, 10), card(3, 4, 3), card(3, 2, 3)]

#test_hand combos
hand1 = [test_hand[0], test_hand[1], test_hand[2], test_hand[3]]
hand2 = [test_hand[0], test_hand[1], test_hand[2], test_hand[4]]
hand3 = [test_hand[0], test_hand[1], test_hand[2], test_hand[5]]
hand4 = [test_hand[0], test_hand[1], test_hand[3], test_hand[4]]
hand5 = [test_hand[0], test_hand[1], test_hand[3], test_hand[5]]
hand6 = [test_hand[0], test_hand[1], test_hand[4], test_hand[5]]
hand7 = [test_hand[0], test_hand[2], test_hand[3], test_hand[4]]
hand8 = [test_hand[0], test_hand[2], test_hand[3], test_hand[5]]

for v in range(0, 6):
    print_card(test_hand, v)

#random.shuffle(deck)

#for x in range(1, 7):
#    x = deck.pop()
#    my_hand.append(x)

#print('player hand: ')
#for y in range(0, 6):
#    print_card(my_hand, y)


#for z in range(1, 7):
#    z = deck.pop()
#    pc_hand.append(z)

#print('computer hand: ')
#for a in range(0, 6):
#    print_card(pc_hand, a)

pc_hand_points = 0
player_hand_points = 0;

#pc_hand.sort(key= lambda x: x.rank)
#my_hand.sort(key= lambda x: x.rank)

def evaluate_hand(hand, crib, low, high):
    points = 0

    #check for fifteens with a combo of 2 cards
    if(hand[low].value + hand[low+1].value == 15):
        points += 2
    if(hand[low].value + hand[low+2].value == 15):
        points += 2
    if(hand[low].value + hand[high].value == 15):
        points += 2
    #check for fifteens with a combo of 3 cards
    if(hand[low].value + hand[low+1].value + hand[low+2].value == 15):
        points += 2
    if(hand[low].value + hand[low+1].value + hand[high].value == 15):
        points += 2
    if(hand[low].value + hand[low+2].value +hand[high].value == 15):
        points += 2
    if(hand[low+1].value + hand[low+2].value + hand[high].value == 15):
        points += 2
    #check for fifteens with a combo of 4 cards
    if(hand[low].value + hand[low+1].value + hand[low+2].value + hand[high].value == 15):
        points += 2

    #check for of-a-kinds
    if(hand[low].rank == hand[low+1].rank):
        points += 2
        if(hand[low].rank == hand[low+2].rank):
            points += 4
            if(hand[low].rank == hand[high].rank):
                points += 6
    if(hand[low].rank == hand[low+2].rank):
        points += 2
        if(hand[low].rank == hand[high].rank):
            points += 4
    if(hand[low]. rank == hand[high].rank):
        points += 2
    if(hand[low+1].rank == hand[low+2].rank):
        points += 2
        if(hand[low+1].rank == hand[high].rank):
            points += 4
    if(hand[low+1].rank == hand[high].rank):
        points += 2
    if(hand[low+2].rank == hand[high].rank):
        points += 2

    #check for runs
    #sort cards by rank
    #hand.sort(key= lambda x: x.rank)
    #if(hand[low].rank + 1 == hand[low+1].rank and hand[low].rank + 2 == hand[low+2].rank):
    #    points += 3
    #    if(hand[low].rank + 3 == hand[high].rank):
    #        points += 1
    #if(hand[low+1].rank + 1 == hand[low+2].rank and hand[low+1].rank + 2 == hand[high].rank):
    #    points += 3

    #check for flush
    #if(hand[low].Suit == hand[low+1].Suit):
    #    print("suits are equal")
    #    if(hand[low].Suit == hand[low+2].Suit):
    #        print("suits are still equal")
    #        if(hand[low].Suit == hand[high].Suit):
    #            print("still equal")
    #            points += 4

    return points

#lowNum = 0
#highNum = 3
#highNum += 5
#print('highnum is now' , highNum)
#testNum = my_hand[0].rank + my_hand[1].rank

#print('testNum: ', testNum)
#print("points in my hand[0,3]: ")
#print(evaluate_hand(my_hand, crib, 0, 3))
#print("points in my hand[1,4]: ")
#print(evaluate_hand(my_hand, crib, 1, 4))
#print("points in my hand[2,5]: ")
#print(evaluate_hand(my_hand, crib, 2, 5))
print("points in my hand[0, 1, 2, 3]: ")
print(evaluate_hand(hand1, crib, 0, 3))
print("points in my hand[0, 1, 2, 4]: ")
print(evaluate_hand(hand2, crib, 0, 3))
print("points in my hand[0, 1, 4, 5]: ")
print(evaluate_hand(hand6, crib, 0, 3))
