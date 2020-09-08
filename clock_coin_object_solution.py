#!/usr/bin/env python3
# Another solution to https://github.com/atsepkov/puzzles/blob/master/interviews/easy/coins-on-clock/README.md

class SlotOccupied(Exception):
    def __init__(self):
        self.message = 'Invalid placement'

class Clock:
    def __init__( self, clock = None, coin = None ):
        if not clock:
            self.coins = [ 0,0,0,0,0,0,0,0,0,0,0,0 ]
            self.sequence = []
            self.idx = 0
        else:
            if clock.occupied():
                raise SlotOccupied()
            idx = clock.idx
            self.coins = list( clock.coins )
            self.sequence = list( clock.sequence )
            self.coins[idx] = coin
            self.sequence.append( coin )
            self.idx = ( idx + coin ) % 12


    def occupied( self ):
        return self.coins[ self.idx ]

    def full(self):
        return 64 == sum( self.coins )

    def __str__(self):
        coins = []
        for coin in self.coins:
            coins.append(
               coin == 0 and '_' or
               coin == 1 and 'P' or
               coin == 5 and 'N' or
               coin == 10 and 'D' 
            )
        return ''.join( coins )

    def validate(self):

        hours = set()
        idx = 0
        for coin in self.sequence:
            hours.add( idx )
            idx = ( idx + coin ) % 12

        return len(hours) == 12

def doit( clock, pennies, nickels, dimes ):

    if clock.full(): # alternatively: pennies + nickels + dimes == 0
        print('valid:', clock.validate(), clock )
        return

    if pennies > 0:
        try:
            doit( Clock( clock, 1 ), pennies - 1, nickels, dimes )
        except SlotOccupied:
            pass
    if nickels > 0:
        try:
            doit( Clock( clock, 5 ), pennies, nickels-1, dimes )
        except SlotOccupied:
            pass
    if dimes > 0:
        try:
            doit( Clock( clock, 10 ), pennies, nickels, dimes-1, )
        except SlotOccupied:
            pass

doit(Clock(), 4, 4, 4 )
