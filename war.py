import random
import copy
import math

gen = lambda: range(2,15)

enemies = [list(gen()), list(reversed(gen()))]

def shuffled(iterable):
    temp = copy.copy(iterable)
    random.shuffle(temp)
    return temp

def sign(x):
    return cmp(x, 0)

def unfair_sign(x):
    return -1 if sign(x) == 0 else sign(x)

def second(x):
    return x[1]

def seconds(x,y):
    return cmp(second(x), second(y))

def advantage(me, you, unfair):
    if unfair:
        return unfair_sign(me - you)
    return sign(me - you)

def war(deck, opponent, unfair=False):
    return sum(advantage(deck[i], opponent[i], unfair) for i in range(len(opponent)))

def is_winner(deck, opponent, unfair=False):
    return war(deck, opponent, unfair) > 0

storage = {}
i=0
while(i < 100):
    x = tuple(shuffled(gen()))
    y = map(lambda l: is_winner(x, l, unfair=True), enemies)
    if all(y):
        print x
        i+=1
        storage[x] = storage.get(x, 0)+1
        
i=0
score = {}
for k in storage.keys():
    score[k] = sum(map(lambda l: is_winner(k, l), storage.keys()))

print sorted(score.items(), seconds)
