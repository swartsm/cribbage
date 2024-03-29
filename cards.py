import random
import sys
import os
from enum import Enum
from itertools import combinations

# author:  margaret swarts
# date:    8/20/19
# description: This file is an implementation of a deck of cards


class Suit(Enum):
    HEART = 1
    DIAMOND = 2
    SPADE = 3
    CLUB = 4


class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
    
    def show(self):
        print("{} of {}, value {}".format(self.rank, self.suit, self.value))


# create deck
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in Suit:
            for v in range(1, 14):
                if v < 11:
                    self.cards.append(Card(v, s, v))
                elif v == 11:
                    self.cards.append(Card(v, s, 10))
                elif v == 12:
                    self.cards.append(Card(v, s, 10))
                elif v == 13:
                    self.cards.append(Card(v, s, 10))
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def drawCard(self):
        return self.cards.pop()
   
        
deck = Deck()
#deck.show() 


deck.shuffle()
#deck.show()
card = deck.drawCard()
card.show()
# test
             
"""
# this isn't right. Size is 676? 
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
"""

#print(len(deck))

def print_card(deck, x):
    if(deck[x].suit ==1):
        if(deck[x].rank == 11):
            print('Jack of Hearts')
        elif(deck[x].rank == 12):
            print('Queen of Hearts')
        elif(deck[x].rank == 13):
            print('King of Hearts')
        else:
            print(deck[x].rank, 'of Hearts')
    elif(deck[x].suit == 2):
        if(deck[x].rank == 11):
            print('Jack of Diamonds')
        elif(deck[x].rank == 12):
            print('Queen of Diamonds')
        elif(deck[x].rank == 13):
            print('King of Diamonds')
        else:
            print(deck[x].rank, 'of Diamonds')
    elif(deck[x].suit == 3):
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
#test_hand = [card(5, 1, 5), card(5, 2, 5), card(12, 1, 10), card(13, 1, 10), card(3, 4, 3), card(3, 2, 3)]
#test_hand2 = [card(6, 1, 6), card(6, 2, 6), card(6, 4, 6), card(3, 1, 3), card(3, 3, 3), card(1, 1, 1)]
#test_hand3 = [card(1, 1, 1), card(2, 1, 2), card(3, 1, 3), card(10, 1, 10), card(11, 2, 10), card(12, 3, 10)]



#test_hand combos
"""
hand1 = [test_hand[0], test_hand[1], test_hand[2], test_hand[3]]
hand2 = [test_hand[0], test_hand[1], test_hand[2], test_hand[4]]
hand3 = [test_hand[0], test_hand[1], test_hand[2], test_hand[5]]
hand4 = [test_hand[0], test_hand[1], test_hand[3], test_hand[4]]
hand5 = [test_hand[0], test_hand[1], test_hand[3], test_hand[5]]
hand6 = [test_hand[0], test_hand[1], test_hand[4], test_hand[5]]
hand7 = [test_hand[0], test_hand[2], test_hand[3], test_hand[4]]
hand8 = [test_hand[0], test_hand[2], test_hand[3], test_hand[5]]
"""
#for x in range(6):
#my_hand = combinations([0, 1, 2, 3, 4, 5], 4)
#combos = []

"""
#print(combos)
for x in range(len(combos)):
    sublist = combos[x]
    hand = []
    print("sublist", sublist)
    for y in range(4):
        #hand1= [test_hand[0]]
        hand.append([test_hand[sublist[y]]])
        #print(hand1)
    for v in range(len(hand)):
        print_card(hand, v)

#print(list(my_hand[0]))
"""
#for v in range(0, 6):
    #print_card(test_hand, v)

#random.shuffle(deck)

"""

for x in range(1, 7):
    x = deck.pop()
    my_hand.append(x)

print('player hand: ')
for y in range(0, 6):
    print_card(my_hand, y)


for z in range(1, 7):
    z = deck.pop()
    pc_hand.append(z)

print('computer hand: ')
for a in range(0, 6):
    print_card(pc_hand, a)

"""

#pc_hand_points = 0
#player_hand_points = 0

#pc_hand.sort(key= lambda x: x.rank)
#my_hand.sort(key= lambda x: x.rank)
"""

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
    """

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

def check_fifteens(hand, hand_size):
    points = 0
    #running_total = 0
    fullsum = 0
    for x in range(hand_size):
        fullsum += hand[x].value
    # if all cards add up to 15, we are done
    if fullsum == 15:
        points += 2
    else:
        #if all but one card adds up to 15:
        for y in range(hand_size):
            if fullsum - hand[y].value == 15:
                points+=2
        for i in range(hand_size -1):
            running_total = hand[i].value
            for j in range(i+1, hand_size):
                sum = hand[i].value + hand[j].value
                if sum == 15:
                    points+=2
                """
                elif sum < 15:
                    running_total+=hand[j].value
                if running_total == 15:
                    points+=2
                    running_total = 0
                elif running_total > 15:
                    running_total -= hand[j].value
                """
                    
    return points

def check_ofakinds(hand, hand_size):
    points = 0
    for i in range(hand_size-1):
        for j in range(i+1, hand_size):
            #print("hjand i rank", hand[i].rank)
            #print("hand[j].rank", hand[j].rank)
            if hand[i].rank == hand[j].rank:
                points += 2
    return points

def check_flush(hand, hand_size):
    points = 0
    card_suit = hand[0].suit
    for i in range(1, hand_size):
        if hand[i].suit != card_suit:
            return points
    return 4

def check_run(hand, hand_size):
    points = 1
    #first = hand[0].rank
    for i in range(hand_size-1):
        if hand[i+1].rank - hand[i].rank == 1:
            if i < 2:
                points+=1
            elif hand[i+1].rank - hand[i-1].rank == 2:
                points+=1
        #print("diff", hand[i+1].rank - hand[i].rank)
        #print("points", points)
    if points >=3:
        return points
    else:
        return 0 

total_points = 0
max_points_four = 0
combos = []

"""

#Evaluate all combinations of 4 in the given hand
for combination in combinations([0, 1, 2, 3, 4, 5], 4):
    #varr is each combination
    varr = list(combination)
    #combos is a list of the combinations
    combos.append(varr)
    #create hand for each combination
    hand = [my_hand[varr[0]], my_hand[varr[1]], my_hand[varr[2]], my_hand[varr[3]]]
    #print hand
    #for x in range(4):
        #print_card(hand, x)
    #evaluate the hand and print
    #points = evaluate_hand(hand, crib, 0, 3)
    #print(check_fifteens(hand, 4))
    #print(check_ofakinds(hand, 4))
    #print(check_flush(hand, 4))
    #print(check_run(hand, 4))
    total_points = check_fifteens(hand, 4) + check_ofakinds(hand, 4) + check_flush(hand, 4) + check_run(hand, 4)
    #print(total_points)
    max_points_four = max(total_points, max_points_four)
    #print("max points", max_points_four)

    
"""