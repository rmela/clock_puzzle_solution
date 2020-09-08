#!/usr/bin/env python3
# A more OO solution to https://github.com/atsepkov/puzzles/blob/master/interviews/easy/coins-on-clock/README.md

class SlotOccupied(Exception):

    def __init__(self):
        self.message = 'Invalid placement'

CHAR_MAPPINGS = {
   0: '_',
   1: 'P',
   5: 'N',
  10: 'D'
}

class Clock:

    def __init__( self, parent = None, coin = None ):
        if not parent:
            self.sequence = []
            self.hour = 0
            # array for the follow-on, "most profitable" part of the puzzle, i.e., clock with
            # highest summation of hour * coin
            self.hours = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
        else:
            self.hour = ( parent.hour + coin ) % 12
            if parent.hours[ self.hour ]:
                raise SlotOccupied()
            self.hours = list( parent.hours )
            self.hours[ self.hour ] = coin
            self.sequence = list( parent.sequence )
            self.sequence.append( coin )


    def full(self):
        return len(self.sequence) == 12

    def __str__(self):
        return ''.join( map( lambda coin: CHAR_MAPPINGS[coin], self.sequence ) )

    def validate(self):

        """Replay coin placement by iterating through sequence of placed coins.
           Ensure that iteration results in 12 unique hours, one coin per hour"""

        hours = set()
        idx = 0
        for coin in self.sequence:
            idx = ( idx + coin ) % 12
            hours.add( idx )

        return len(hours) == 12

def doit( parent, pennies, nickels, dimes ):

    if parent.full():
        print('valid:', parent.validate(), parent, parent.sequence )
        return

    if pennies > 0:
        try:
            doit( Clock( parent, 1 ), pennies - 1, nickels, dimes )
        except SlotOccupied:
            pass
    if nickels > 0:
        try:
            doit( Clock( parent, 5 ), pennies, nickels-1, dimes )
        except SlotOccupied:
            pass
    if dimes > 0:
        try:
            doit( Clock( parent, 10 ), pennies, nickels, dimes-1, )
        except SlotOccupied:
            pass

doit(Clock(), 4, 4, 4 )
#
# doit(Clock(), 3, 5, 4 ) # Example of varying coin counts
