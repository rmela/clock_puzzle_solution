#! /usr/bin/env python3
# Solution to interview question at https://github.com/atsepkov/puzzles/blob/master/interviews/easy/coins-on-clock/README.md

from collections import namedtuple

Clock = namedtuple( 'Clock', ['idx', 'coins', 'sequence' ] )

def clock_to_string( clock ):
    coins = []
    for coin in clock.sequence:
        coins.append(
           coin == 0 and '_' or
           coin == 1 and 'P' or
           coin == 5 and 'N' or
           coin == 10 and 'D' 
        )
    return ''.join( coins )

def clock_is_full( clock ):
    return 64 == sum( clock.coins )

def place_coin( clock, coin ):
    newidx = ( clock.idx + coin ) % 12
    if not clock.coins[newidx]:
        coins = list(clock.coins )
        sequence = list( clock.sequence )
        sequence.append( coin )
        coins[newidx] = coin
        return Clock( newidx, coins, sequence )

def validate( clock ):
    idx = 0

    hours = set()
    for coin in clock.sequence:
        idx = ( idx + coin ) % 12
        hours.add( idx )

    return len(hours) == 12

def doit( clock, pennies, nickels, dimes, result ):

    if clock_is_full(clock): # alternatively: pennies + nickels + dimes == 0
        result.append( clock )
        return

    if pennies > 0:
        newclock = place_coin( clock, 1 )
        if newclock: doit( newclock, pennies - 1, nickels, dimes, result )
    if nickels > 0:
        newclock = place_coin( clock, 5 )
        if newclock: doit( newclock, pennies, nickels - 1, dimes , result)
    if dimes > 0:
        newclock = place_coin( clock, 10 )
        if newclock: doit( newclock, pennies, nickels, dimes - 1 , result)

result = []
doit( Clock( 0, [0,0,0,0,0,0,0,0,0,0,0,0], []), 4, 4, 4, result )

for clock in result:
    print( 'valid:', validate( clock ), clock_to_string( clock ), clock.sequence )

