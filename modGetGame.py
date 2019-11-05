#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Module to define BattleShip problems from the Logic Problems game.
Exports the getGame() function.
'''

# Application libraries.
import battleships



def getGame(index, args):
    ''' Return a game object for the specified game. '''
    if index == 1:
        game = battleships.Battleships(10, 4, 'Logic Problems Battleships Number 1', args)

        game.horizontal[0] = 1
        game.horizontal[1] = 1
        game.horizontal[2] = 3
        game.horizontal[3] = 1
        game.horizontal[4] = 4
        game.horizontal[5] = 0
        game.horizontal[6] = 0
        game.horizontal[7] = 8
        game.horizontal[8] = 1
        game.horizontal[9] = 1
        game.vertical[0] = 2
        game.vertical[1] = 1
        game.vertical[2] = 3
        game.vertical[3] = 1
        game.vertical[4] = 1
        game.vertical[5] = 1
        game.vertical[6] = 3
        game.vertical[7] = 1
        game.vertical[8] = 5
        game.vertical[9] = 2

        game.mask[1] = 4
        game.mask[4] = 2
        game.mask[7] = 16

        game.mask[0] = 2 ** 8
        game.negativeMask[2] = 1 + 2 + 8 + 16 + 32 + 128
        game.mask[3] = 64
        game.mask[4] = 2 + 64 + 256 + 512

    elif index == 2:
        game = battleships.Battleships(10, 4, 'Logic Problems Battleships Number 2', args)

        game.horizontal[0] = 1
        game.horizontal[1] = 2
        game.horizontal[2] = 3
        game.horizontal[3] = 2
        game.horizontal[4] = 3
        game.horizontal[5] = 3
        game.horizontal[6] = 2
        game.horizontal[7] = 1
        game.horizontal[8] = 3
        game.horizontal[9] = 0
        game.vertical[0] = 1
        game.vertical[1] = 4
        game.vertical[2] = 2
        game.vertical[3] = 2
        game.vertical[4] = 3
        game.vertical[5] = 0
        game.vertical[6] = 1
        game.vertical[7] = 3
        game.vertical[8] = 2
        game.vertical[9] = 2

        game.mask[2] = 4 + 8 + 16
        game.mask[3] = 128
        game.mask[4] = 2
        game.mask[5] = 2 + 256
        game.mask[6] = 2
        game.mask[7] = 2

        game.negativeMask[0] = 2
        game.negativeMask[1] = 2 + 4 + 8 + 16 + 32
        game.negativeMask[2] = 2 + 32 + 128 + 256
        game.negativeMask[3] = 2 + 4 + 8 + 16 + 32 + 256
        game.negativeMask[4] = 128 + 256
        game.negativeMask[5] = 128
        game.negativeMask[6] = 128 + 256
        game.negativeMask[8] = 2
        game.negativeMask[9] = 2

    elif index == 3:
        game = battleships.Battleships(10, 4, 'Logic Problems Battleships Number 3', args)

        game.horizontal[0] = 4
        game.horizontal[1] = 0
        game.horizontal[2] = 3
        game.horizontal[3] = 5
        game.horizontal[4] = 2
        game.horizontal[5] = 0
        game.horizontal[6] = 0
        game.horizontal[7] = 2
        game.horizontal[8] = 2
        game.horizontal[9] = 2
        game.vertical[0] = 3
        game.vertical[1] = 0
        game.vertical[2] = 1
        game.vertical[3] = 4
        game.vertical[4] = 1
        game.vertical[5] = 6
        game.vertical[6] = 0
        game.vertical[7] = 3
        game.vertical[8] = 0
        game.vertical[9] = 2

        game.mask[7] = 128
        game.mask[8] = 1
        game.mask[9] = 512

        game.negativeMask[6] = 64 + 128 + 256
        game.negativeMask[7] = 2 + 64 + 256
        game.negativeMask[8] = 2 + 64 + 128 + 256 + 512
        game.negativeMask[9] = 1 + 2 + 256

    elif index == 24:
        game = battleships.Battleships(8, 5, 'Logic Problems Battleships Number 24', args)

        game.horizontal[0] = 4
        game.horizontal[1] = 3
        game.horizontal[2] = 4
        game.horizontal[3] = 2
        game.horizontal[4] = 1
        game.horizontal[5] = 6
        game.horizontal[6] = 0
        game.horizontal[7] = 5
        game.vertical[0] = 4
        game.vertical[1] = 1
        game.vertical[2] = 5
        game.vertical[3] = 1
        game.vertical[4] = 6
        game.vertical[5] = 1
        game.vertical[6] = 3
        game.vertical[7] = 4

        game.negativeMask[0] = 2
        game.mask[1] = 1
        game.negativeMask[1] = 2
        game.mask[2] = 1
        game.negativeMask[2] = 2
        game.negativeMask[3] = 1+2

        # game.mask[5] = 2+4+8+16+32+128

        # game.mask[7] = 1+4+16+64+128

    elif index == 26:
        game = battleships.Battleships(8, 5, 'Logic Problems Battleships Number 26', args)

        game.horizontal[0] = 5
        game.horizontal[1] = 2
        game.horizontal[2] = 1
        game.horizontal[3] = 5
        game.horizontal[4] = 2
        game.horizontal[5] = 3
        game.horizontal[6] = 1
        game.horizontal[7] = 6
        game.vertical[0] = 5
        game.vertical[1] = 2
        game.vertical[2] = 3
        game.vertical[3] = 3
        game.vertical[4] = 2
        game.vertical[5] = 3
        game.vertical[6] = 1
        game.vertical[7] = 6

        game.negativeMask[5] = 64 + 128
        game.mask[6] = 128
        game.negativeMask[6] = 64
        game.mask[7] = 128
        game.negativeMask[7] = 64

        game.mask[0] = 128
        game.negativeMask[1] = 64
        game.mask[2] = 128
        game.negativeMask[3] = 64
        game.mask[4] = 128

    elif index == 27:
        game = battleships.Battleships(8, 5, 'Logic Problems Battleships Number 27', args)

        game.horizontal[0] = 5
        game.horizontal[1] = 1
        game.horizontal[2] = 5
        game.horizontal[3] = 2
        game.horizontal[4] = 2
        game.horizontal[5] = 4
        game.horizontal[6] = 2
        game.horizontal[7] = 4
        game.vertical[0] = 3
        game.vertical[1] = 3
        game.vertical[2] = 1
        game.vertical[3] = 6
        game.vertical[4] = 2
        game.vertical[5] = 4
        game.vertical[6] = 2
        game.vertical[7] = 4

        game.negativeMask[4] = 64 + 128
        game.mask[5] = 128
        game.negativeMask[5] = 64
        game.mask[6] = 128
        game.negativeMask[6] = 64
        game.negativeMask[7] = 64

    elif index == 28:
        game = battleships.Battleships(8, 5, 'Logic Problems Battleships Number 28', args)

        game.horizontal[0] = 5
        game.horizontal[1] = 1
        game.horizontal[2] = 3
        game.horizontal[3] = 5
        game.horizontal[4] = 1
        game.horizontal[5] = 5
        game.horizontal[6] = 1
        game.horizontal[7] = 4
        game.vertical[0] = 4
        game.vertical[1] = 1
        game.vertical[2] = 6
        game.vertical[3] = 2
        game.vertical[4] = 3
        game.vertical[5] = 3
        game.vertical[6] = 0
        game.vertical[7] = 6

        game.mask[7] = 1
        game.negativeMask[6] = 1 + 2
        game.negativeMask[7] = 2

    elif index == 29:
        game = battleships.Battleships(8, 5, 'Logic Problems Battleships Number 29', args)

        game.horizontal[0] = 4
        game.horizontal[1] = 4
        game.horizontal[2] = 2
        game.horizontal[3] = 4
        game.horizontal[4] = 2
        game.horizontal[5] = 3
        game.horizontal[6] = 2
        game.horizontal[7] = 4
        game.vertical[0] = 7
        game.vertical[1] = 0
        game.vertical[2] = 6
        game.vertical[3] = 0
        game.vertical[4] = 5
        game.vertical[5] = 1
        game.vertical[6] = 5
        game.vertical[7] = 1

        game.negativeMask[1] = 8 + 32
        game.mask[2] = 16
        game.negativeMask[3] = 8 + 32

    elif index == 30:
        game = battleships.Battleships(8, 5, 'Logic Problems Battleships Number 30', args)

        game.horizontal[0] = 5
        game.horizontal[1] = 3
        game.horizontal[2] = 4
        game.horizontal[3] = 3
        game.horizontal[4] = 3
        game.horizontal[5] = 1
        game.horizontal[6] = 3
        game.horizontal[7] = 3
        game.vertical[0] = 6
        game.vertical[1] = 0
        game.vertical[2] = 5
        game.vertical[3] = 1
        game.vertical[4] = 1
        game.vertical[5] = 5
        game.vertical[6] = 1
        game.vertical[7] = 6

    elif index == 31:
        game = battleships.Battleships(8, 5, 'Logic Problems Battleships Number 31', args)

        game.horizontal[0] = 5
        game.horizontal[1] = 1
        game.horizontal[2] = 5
        game.horizontal[3] = 1
        game.horizontal[4] = 3
        game.horizontal[5] = 2
        game.horizontal[6] = 6
        game.horizontal[7] = 2
        game.vertical[0] = 3
        game.vertical[1] = 2
        game.vertical[2] = 4
        game.vertical[3] = 3
        game.vertical[4] = 2
        game.vertical[5] = 5
        game.vertical[6] = 0
        game.vertical[7] = 6

    elif index == 32:
        game = battleships.Battleships(8, 5, 'Logic Problems Battleships Number 32', args)

        game.horizontal[0] = 4
        game.horizontal[1] = 2
        game.horizontal[2] = 4
        game.horizontal[3] = 4
        game.horizontal[4] = 2
        game.horizontal[5] = 3
        game.horizontal[6] = 1
        game.horizontal[7] = 5
        game.vertical[0] = 5
        game.vertical[1] = 0
        game.vertical[2] = 6
        game.vertical[3] = 2
        game.vertical[4] = 1
        game.vertical[5] = 5
        game.vertical[6] = 1
        game.vertical[7] = 5

    elif index == 33:
        game = battleships.Battleships(8, 5, 'Logic Problems Battleships Number 33', args)

        game.horizontal[0] = 5
        game.horizontal[1] = 2
        game.horizontal[2] = 3
        game.horizontal[3] = 3
        game.horizontal[4] = 1
        game.horizontal[5] = 5
        game.horizontal[6] = 1
        game.horizontal[7] = 5
        game.vertical[0] = 6
        game.vertical[1] = 1
        game.vertical[2] = 4
        game.vertical[3] = 1
        game.vertical[4] = 6
        game.vertical[5] = 2
        game.vertical[6] = 3
        game.vertical[7] = 2

    elif index == 34:
        game = battleships.Battleships(8, 5, 'Logic Problems Battleships Number 34', args)

        game.horizontal[0] = 4
        game.horizontal[1] = 1
        game.horizontal[2] = 3
        game.horizontal[3] = 2
        game.horizontal[4] = 4
        game.horizontal[5] = 3
        game.horizontal[6] = 3
        game.horizontal[7] = 5
        game.vertical[0] = 5
        game.vertical[1] = 1
        game.vertical[2] = 5
        game.vertical[3] = 1
        game.vertical[4] = 5
        game.vertical[5] = 1
        game.vertical[6] = 4
        game.vertical[7] = 3

    elif index == 35:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 35', args)

        game.horizontal[0] = 2
        game.horizontal[1] = 1
        game.horizontal[2] = 3
        game.horizontal[3] = 5
        game.horizontal[4] = 1
        game.horizontal[5] = 4
        game.horizontal[6] = 2
        game.horizontal[7] = 3
        game.horizontal[8] = 4
        game.vertical[0] = 5
        game.vertical[1] = 2
        game.vertical[2] = 1
        game.vertical[3] = 4
        game.vertical[4] = 1
        game.vertical[5] = 6
        game.vertical[6] = 2
        game.vertical[7] = 1
        game.vertical[8] = 3

        game.mask[4] = 1
        game.mask[7] = 1
        game.mask[8] = 1

        game.negativeMask[3] = 1 + 2
        game.negativeMask[4] = 2
        game.negativeMask[5] = 1 + 2
        game.negativeMask[6] = 2
        game.negativeMask[7] = 2
        game.negativeMask[8] = 2

    elif index == 36:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 36', args)
        game.horizontal[0] = 4
        game.horizontal[1] = 1
        game.horizontal[2] = 4
        game.horizontal[3] = 3
        game.horizontal[4] = 4
        game.horizontal[5] = 3
        game.horizontal[6] = 0
        game.horizontal[7] = 4
        game.horizontal[8] = 2
        game.vertical[0] = 3
        game.vertical[1] = 2
        game.vertical[2] = 6
        game.vertical[3] = 1
        game.vertical[4] = 1
        game.vertical[5] = 6
        game.vertical[6] = 1
        game.vertical[7] = 2
        game.vertical[8] = 3

        game.mask[2] = 128
        game.mask[4] = 4
        game.mask[5] = 4

        game.negativeMask[1] = 64 + 128 + 256
        game.negativeMask[2] = 64 + 256
        game.negativeMask[3] = 2 + 8 + 64 + 128 + 256
        game.negativeMask[4] = 2 + 8
        game.negativeMask[5] = 2 + 8
        game.negativeMask[6] = 2 + 4 + 8

    elif index == 37:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 37', args)
        game.horizontal[0] = 3
        game.horizontal[1] = 2
        game.horizontal[2] = 7
        game.horizontal[3] = 1
        game.horizontal[4] = 5
        game.horizontal[5] = 1
        game.horizontal[6] = 2
        game.horizontal[7] = 4
        game.horizontal[8] = 0
        game.vertical[0] = 4
        game.vertical[1] = 1
        game.vertical[2] = 5
        game.vertical[3] = 0
        game.vertical[4] = 4
        game.vertical[5] = 3
        game.vertical[6] = 2
        game.vertical[7] = 4
        game.vertical[8] = 2

        game.mask[0] = 16
        game.mask[2] = 4
        game.mask[3] = 4
        game.mask[4] = 4

        game.negativeMask[0] = 8 + 32
        game.negativeMask[1] = 2 + 8 + 16 + 32
        game.negativeMask[2] = 2 + 8
        game.negativeMask[3] = 2 + 8
        game.negativeMask[4] = 2 + 8
        game.negativeMask[5] = 2 + 8

    elif index == 38:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 38', args)
        game.horizontal[0] = 4
        game.horizontal[1] = 3
        game.horizontal[2] = 4
        game.horizontal[3] = 2
        game.horizontal[4] = 2
        game.horizontal[5] = 2
        game.horizontal[6] = 3
        game.horizontal[7] = 2
        game.horizontal[8] = 3
        game.vertical[0] = 3
        game.vertical[1] = 0
        game.vertical[2] = 6
        game.vertical[3] = 0
        game.vertical[4] = 2
        game.vertical[5] = 6
        game.vertical[6] = 2
        game.vertical[7] = 0
        game.vertical[8] = 6

        game.mask[7] = 4
        game.mask[8] = 4 +16

        game.negativeMask[6] = 2 + 4 + 8
        game.negativeMask[7] = 2 + 8 + 16 + 32
        game.negativeMask[8] = 2 + 8 + 32

    elif index == 39:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 39', args)
        game.horizontal[0] = 1
        game.horizontal[1] = 3
        game.horizontal[2] = 1
        game.horizontal[3] = 6
        game.horizontal[4] = 3
        game.horizontal[5] = 3
        game.horizontal[6] = 2
        game.horizontal[7] = 3
        game.horizontal[8] = 3
        game.vertical[0] = 6
        game.vertical[1] = 1
        game.vertical[2] = 5
        game.vertical[3] = 0
        game.vertical[4] = 3
        game.vertical[5] = 3
        game.vertical[6] = 1
        game.vertical[7] = 2
        game.vertical[8] = 4

        game.mask[3] = 1
        game.mask[4] = 1
        game.mask[5] = 1
        game.mask[8] = 16

        game.negativeMask[2] = 2
        game.negativeMask[3] = 2
        game.negativeMask[4] = 2
        game.negativeMask[5] = 2
        game.negativeMask[6] = 2
        game.negativeMask[7] =  8 + 16 + 32
        game.negativeMask[8] =  8 + 32

    elif index == 40:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 40', args)
        game.horizontal[0] = 1
        game.horizontal[1] = 5
        game.horizontal[2] = 1
        game.horizontal[3] = 5
        game.horizontal[4] = 1
        game.horizontal[5] = 3
        game.horizontal[6] = 4
        game.horizontal[7] = 3
        game.horizontal[8] = 2
        game.vertical[0] = 0
        game.vertical[1] = 5
        game.vertical[2] = 2
        game.vertical[3] = 3
        game.vertical[4] = 2
        game.vertical[5] = 6
        game.vertical[6] = 0
        game.vertical[7] = 4
        game.vertical[8] = 3

        game.mask[1] = 2 + 4

        game.negativeMask[0] = 1 + 2 + 4 + 8 + 64
        game.negativeMask[1] = 1 + 8 + 64
        game.negativeMask[2] = 1 + 2 + 4 + 8 + 64
        game.negativeMask[3] = 1 + 64
        game.negativeMask[4] = 1 + 64
        game.negativeMask[5] = 1 + 64
        game.negativeMask[6] = 1 + 64
        game.negativeMask[7] = 1 + 64
        game.negativeMask[8] = 1 + 64

    elif index == 41:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 41', args)
        game.horizontal[0] = 3
        game.horizontal[1] = 4
        game.horizontal[2] = 2
        game.horizontal[3] = 4
        game.horizontal[4] = 0
        game.horizontal[5] = 5
        game.horizontal[6] = 1
        game.horizontal[7] = 6
        game.horizontal[8] = 0
        game.vertical[0] = 1
        game.vertical[1] = 4
        game.vertical[2] = 2
        game.vertical[3] = 2
        game.vertical[4] = 3
        game.vertical[5] = 4
        game.vertical[6] = 4
        game.vertical[7] = 2
        game.vertical[8] = 3

        game.mask[0] = 4

        game.negativeMask[0] = 2 + 8
        game.negativeMask[1] = 2 + 4 + 8

    elif index == 42:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 42', args)
        game.horizontal[0] = 3
        game.horizontal[1] = 2
        game.horizontal[2] = 3
        game.horizontal[3] = 3
        game.horizontal[4] = 2
        game.horizontal[5] = 2
        game.horizontal[6] = 4
        game.horizontal[7] = 0
        game.horizontal[8] = 6
        game.vertical[0] = 0
        game.vertical[1] = 7
        game.vertical[2] = 1
        game.vertical[3] = 0
        game.vertical[4] = 7
        game.vertical[5] = 1
        game.vertical[6] = 3
        game.vertical[7] = 2
        game.vertical[8] = 4

        game.mask[4] = 64

        game.negativeMask[0] = 1 + 8
        game.negativeMask[1] = 1 + 8
        game.negativeMask[2] = 1 + 8
        game.negativeMask[3] = 1 + 8 + 32 + 64 + 128
        game.negativeMask[4] = 1 + 8 + 32 + 128
        game.negativeMask[5] = 1 + 8 + 32 + 64 + 128
        game.negativeMask[6] = 1 + 8
        game.negativeMask[7] = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 + 256
        game.negativeMask[8] = 1 + 8

    elif index == 43:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 43', args)
        game.horizontal[0] = 5
        game.horizontal[1] = 3
        game.horizontal[2] = 2
        game.horizontal[3] = 0
        game.horizontal[4] = 6
        game.horizontal[5] = 1
        game.horizontal[6] = 1
        game.horizontal[7] = 2
        game.horizontal[8] = 5
        game.vertical[0] = 6
        game.vertical[1] = 2
        game.vertical[2] = 1
        game.vertical[3] = 5
        game.vertical[4] = 2
        game.vertical[5] = 1
        game.vertical[6] = 4
        game.vertical[7] = 1
        game.vertical[8] = 3

        game.mask[4] = 8 + 16

        game.negativeMask[3] = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 + 256
        game.negativeMask[4] = 4
        game.negativeMask[5] = 4 + 8 + 16 + 32

    elif index == 44:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 44', args)
        game.horizontal[0] = 5
        game.horizontal[1] = 0
        game.horizontal[2] = 5
        game.horizontal[3] = 1
        game.horizontal[4] = 0
        game.horizontal[5] = 7
        game.horizontal[6] = 2
        game.horizontal[7] = 3
        game.horizontal[8] = 2
        game.vertical[0] = 3
        game.vertical[1] = 1
        game.vertical[2] = 3
        game.vertical[3] = 4
        game.vertical[4] = 3
        game.vertical[5] = 2
        game.vertical[6] = 2
        game.vertical[7] = 4
        game.vertical[8] = 3

        game.mask[2] = 8 + 16

        game.negativeMask[1] = 4 + 8 + 16 + 32
        game.negativeMask[2] = 32
        game.negativeMask[3] = 4 + 8 + 16 + 32

    elif index == 45:
        game = battleships.Battleships(9, 5, 'Logic Problems Battleships Number 45', args)
        game.horizontal[0] = 1
        game.horizontal[1] = 4
        game.horizontal[2] = 2
        game.horizontal[3] = 5
        game.horizontal[4] = 2
        game.horizontal[5] = 3
        game.horizontal[6] = 3
        game.horizontal[7] = 1
        game.horizontal[8] = 4
        game.vertical[0] = 0
        game.vertical[1] = 6
        game.vertical[2] = 2
        game.vertical[3] = 2
        game.vertical[4] = 3
        game.vertical[5] = 2
        game.vertical[6] = 3
        game.vertical[7] = 2
        game.vertical[8] = 5

        # Try the super tanker in row 4, attempt 1. No Match.
        # Try the super tanker in row 4, attempt 2. Not possible.
        # Try the super tanker in row 4, attempt 3. Not possible.
        # Try the super tanker in row 4, attempt 4. No Match.

        # Try the super tanker in column 2, attempt 1 (top). No Match.
        # Try the super tanker in column 2, attempt 2 (bottom). No Match.

        # Try the super tanker in column 9, attempt 1 (top).

        game.mask[0] = 256
        game.mask[1] = 256
        game.mask[2] = 256
        game.mask[3] = 256
        game.mask[4] = 256
        game.mask[5] = 0
        game.mask[6] = 0
        game.mask[7] = 0
        game.mask[8] = 0

        game.negativeMask[0] = 128
        game.negativeMask[1] = 128
        game.negativeMask[2] = 128
        game.negativeMask[3] = 128
        game.negativeMask[4] = 128
        game.negativeMask[5] = 128 + 256
        game.negativeMask[6] = 0
        game.negativeMask[7] = 0
        game.negativeMask[8] = 0

    game.solve_game = True

    return game
