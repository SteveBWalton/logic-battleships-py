#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Module to define BattleShip problems from the Logic Problems game.
Exports the GetGame() function.
'''

import battleships


def GetGame(index, oArgs):
    ''' Return a game object for the specified game. '''
    if index == 1:
        oGame = battleships.CBattleships(10, 4, 'Logic Problems Battleships Number 1', oArgs)

        oGame.horizontal[0] = 1
        oGame.horizontal[1] = 1
        oGame.horizontal[2] = 3
        oGame.horizontal[3] = 1
        oGame.horizontal[4] = 4
        oGame.horizontal[5] = 0
        oGame.horizontal[6] = 0
        oGame.horizontal[7] = 8
        oGame.horizontal[8] = 1
        oGame.horizontal[9] = 1
        oGame.vertical[0] = 2
        oGame.vertical[1] = 1
        oGame.vertical[2] = 3
        oGame.vertical[3] = 1
        oGame.vertical[4] = 1
        oGame.vertical[5] = 1
        oGame.vertical[6] = 3
        oGame.vertical[7] = 1
        oGame.vertical[8] = 5
        oGame.vertical[9] = 2

        oGame.mask[1] = 4
        oGame.mask[4] = 2
        oGame.mask[7] = 16

        oGame.mask[0] = 2 ** 8
        oGame.negative_mask[2] = 1 + 2 + 8 + 16 + 32 + 128
        oGame.mask[3] = 64
        oGame.mask[4] = 2 + 64 + 256 + 512

        oGame.solve_game = True
    elif index == 2:
        oGame = battleships.CBattleships(10, 4, 'Logic Problems Battleships Number 2', oArgs)

        oGame.horizontal[0] = 1
        oGame.horizontal[1] = 2
        oGame.horizontal[2] = 3
        oGame.horizontal[3] = 2
        oGame.horizontal[4] = 3
        oGame.horizontal[5] = 3
        oGame.horizontal[6] = 2
        oGame.horizontal[7] = 1
        oGame.horizontal[8] = 3
        oGame.horizontal[9] = 0
        oGame.vertical[0] = 1
        oGame.vertical[1] = 4
        oGame.vertical[2] = 2
        oGame.vertical[3] = 2
        oGame.vertical[4] = 3
        oGame.vertical[5] = 0
        oGame.vertical[6] = 1
        oGame.vertical[7] = 3
        oGame.vertical[8] = 2
        oGame.vertical[9] = 2

        oGame.mask[2] = 4 + 8 + 16
        oGame.mask[3] = 128
        oGame.mask[4] = 2
        oGame.mask[5] = 2 + 256
        oGame.mask[6] = 2
        oGame.mask[7] = 2

        oGame.negative_mask[0] = 2
        oGame.negative_mask[1] = 2 + 4 + 8 + 16 + 32
        oGame.negative_mask[2] = 2 + 32 + 128 + 256
        oGame.negative_mask[3] = 2 + 4 + 8 + 16 + 32 + 256
        oGame.negative_mask[4] = 128 + 256
        oGame.negative_mask[5] = 128
        oGame.negative_mask[6] = 128 + 256
        oGame.negative_mask[8] = 2
        oGame.negative_mask[9] = 2

        oGame.solve_game = True
    elif index == 3:
        oGame = battleships.CBattleships(10, 4, 'Logic Problems Battleships Number 3', oArgs)

        oGame.horizontal[0] = 4
        oGame.horizontal[1] = 0
        oGame.horizontal[2] = 3
        oGame.horizontal[3] = 5
        oGame.horizontal[4] = 2
        oGame.horizontal[5] = 0
        oGame.horizontal[6] = 0
        oGame.horizontal[7] = 2
        oGame.horizontal[8] = 2
        oGame.horizontal[9] = 2
        oGame.vertical[0] = 3
        oGame.vertical[1] = 0
        oGame.vertical[2] = 1
        oGame.vertical[3] = 4
        oGame.vertical[4] = 1
        oGame.vertical[5] = 6
        oGame.vertical[6] = 0
        oGame.vertical[7] = 3
        oGame.vertical[8] = 0
        oGame.vertical[9] = 2

        oGame.mask[7] = 128
        oGame.mask[8] = 1
        oGame.mask[9] = 512

        oGame.negative_mask[6] = 64 + 128 + 256
        oGame.negative_mask[7] = 2 + 64 + 256
        oGame.negative_mask[8] = 2 + 64 + 128 + 256 + 512
        oGame.negative_mask[9] = 1 + 2 + 256

        oGame.solve_game = True
    elif index == 24:
        oGame = battleships.CBattleships(8, 5, 'Logic Problems Battleships Number 24', oArgs)

        oGame.horizontal[0] = 4
        oGame.horizontal[1] = 3
        oGame.horizontal[2] = 4
        oGame.horizontal[3] = 2
        oGame.horizontal[4] = 1
        oGame.horizontal[5] = 6
        oGame.horizontal[6] = 0
        oGame.horizontal[7] = 5
        oGame.vertical[0] = 4
        oGame.vertical[1] = 1
        oGame.vertical[2] = 5
        oGame.vertical[3] = 1
        oGame.vertical[4] = 6
        oGame.vertical[5] = 1
        oGame.vertical[6] = 3
        oGame.vertical[7] = 4

        oGame.negative_mask[0] = 2
        oGame.mask[1] = 1
        oGame.negative_mask[1] = 2
        oGame.mask[2] = 1
        oGame.negative_mask[2] = 2
        oGame.negative_mask[3] = 1+2

        # oGame.mask[5] = 2+4+8+16+32+128

        # oGame.mask[7] = 1+4+16+64+128
        oGame.solve_game = True
    elif index == 26:
        oGame = battleships.CBattleships(8, 5, 'Logic Problems Battleships Number 26', oArgs)

        oGame.horizontal[0] = 5
        oGame.horizontal[1] = 2
        oGame.horizontal[2] = 1
        oGame.horizontal[3] = 5
        oGame.horizontal[4] = 2
        oGame.horizontal[5] = 3
        oGame.horizontal[6] = 1
        oGame.horizontal[7] = 6
        oGame.vertical[0] = 5
        oGame.vertical[1] = 2
        oGame.vertical[2] = 3
        oGame.vertical[3] = 3
        oGame.vertical[4] = 2
        oGame.vertical[5] = 3
        oGame.vertical[6] = 1
        oGame.vertical[7] = 6

        oGame.negative_mask[5] = 64 + 128
        oGame.mask[6] = 128
        oGame.negative_mask[6] = 64
        oGame.mask[7] = 128
        oGame.negative_mask[7] = 64

        oGame.mask[0] = 128
        oGame.negative_mask[1] = 64
        oGame.mask[2] = 128
        oGame.negative_mask[3] = 64
        oGame.mask[4] = 128
        oGame.solve_game = True
    elif index == 27:
        oGame = battleships.CBattleships(8, 5, 'Logic Problems Battleships Number 27', oArgs)

        oGame.horizontal[0] = 5
        oGame.horizontal[1] = 1
        oGame.horizontal[2] = 5
        oGame.horizontal[3] = 2
        oGame.horizontal[4] = 2
        oGame.horizontal[5] = 4
        oGame.horizontal[6] = 2
        oGame.horizontal[7] = 4
        oGame.vertical[0] = 3
        oGame.vertical[1] = 3
        oGame.vertical[2] = 1
        oGame.vertical[3] = 6
        oGame.vertical[4] = 2
        oGame.vertical[5] = 4
        oGame.vertical[6] = 2
        oGame.vertical[7] = 4

        oGame.negative_mask[4] = 64 + 128
        oGame.mask[5] = 128
        oGame.negative_mask[5] = 64
        oGame.mask[6] = 128
        oGame.negative_mask[6] = 64
        oGame.negative_mask[7] = 64

        oGame.solve_game = True
    elif index == 28:
        oGame = battleships.CBattleships(8, 5, 'Logic Problems Battleships Number 28', oArgs)

        oGame.horizontal[0] = 5
        oGame.horizontal[1] = 1
        oGame.horizontal[2] = 3
        oGame.horizontal[3] = 5
        oGame.horizontal[4] = 1
        oGame.horizontal[5] = 5
        oGame.horizontal[6] = 1
        oGame.horizontal[7] = 4
        oGame.vertical[0] = 4
        oGame.vertical[1] = 1
        oGame.vertical[2] = 6
        oGame.vertical[3] = 2
        oGame.vertical[4] = 3
        oGame.vertical[5] = 3
        oGame.vertical[6] = 0
        oGame.vertical[7] = 6

        oGame.mask[7] = 1
        oGame.negative_mask[6] = 1 + 2
        oGame.negative_mask[7] = 2

        oGame.solve_game = True
    elif index == 29:
        oGame = battleships.CBattleships(8, 5, 'Logic Problems Battleships Number 29', oArgs)

        oGame.horizontal[0] = 4
        oGame.horizontal[1] = 4
        oGame.horizontal[2] = 2
        oGame.horizontal[3] = 4
        oGame.horizontal[4] = 2
        oGame.horizontal[5] = 3
        oGame.horizontal[6] = 2
        oGame.horizontal[7] = 4
        oGame.vertical[0] = 7
        oGame.vertical[1] = 0
        oGame.vertical[2] = 6
        oGame.vertical[3] = 0
        oGame.vertical[4] = 5
        oGame.vertical[5] = 1
        oGame.vertical[6] = 5
        oGame.vertical[7] = 1

        oGame.negative_mask[1] = 8 + 32
        oGame.mask[2] = 16
        oGame.negative_mask[3] = 8 + 32

        oGame.solve_game = True
    elif index == 30:
        oGame = battleships.CBattleships(8, 5, 'Logic Problems Battleships Number 30', oArgs)

        oGame.horizontal[0] = 5
        oGame.horizontal[1] = 3
        oGame.horizontal[2] = 4
        oGame.horizontal[3] = 3
        oGame.horizontal[4] = 3
        oGame.horizontal[5] = 1
        oGame.horizontal[6] = 3
        oGame.horizontal[7] = 3
        oGame.vertical[0] = 6
        oGame.vertical[1] = 0
        oGame.vertical[2] = 5
        oGame.vertical[3] = 1
        oGame.vertical[4] = 1
        oGame.vertical[5] = 5
        oGame.vertical[6] = 1
        oGame.vertical[7] = 6

        oGame.solve_game = True
    elif index == 31:
        oGame = battleships.CBattleships(8, 5, 'Logic Problems Battleships Number 31', oArgs)

        oGame.horizontal[0] = 5
        oGame.horizontal[1] = 1
        oGame.horizontal[2] = 5
        oGame.horizontal[3] = 1
        oGame.horizontal[4] = 3
        oGame.horizontal[5] = 2
        oGame.horizontal[6] = 6
        oGame.horizontal[7] = 2
        oGame.vertical[0] = 3
        oGame.vertical[1] = 2
        oGame.vertical[2] = 4
        oGame.vertical[3] = 3
        oGame.vertical[4] = 2
        oGame.vertical[5] = 5
        oGame.vertical[6] = 0
        oGame.vertical[7] = 6

        oGame.solve_game = True
    elif index == 32:
        oGame = battleships.CBattleships(8, 5, 'Logic Problems Battleships Number 32', oArgs)

        oGame.horizontal[0] = 4
        oGame.horizontal[1] = 2
        oGame.horizontal[2] = 4
        oGame.horizontal[3] = 4
        oGame.horizontal[4] = 2
        oGame.horizontal[5] = 3
        oGame.horizontal[6] = 1
        oGame.horizontal[7] = 5
        oGame.vertical[0] = 5
        oGame.vertical[1] = 0
        oGame.vertical[2] = 6
        oGame.vertical[3] = 2
        oGame.vertical[4] = 1
        oGame.vertical[5] = 5
        oGame.vertical[6] = 1
        oGame.vertical[7] = 5

        oGame.solve_game = True
    elif index == 33:
        oGame = battleships.CBattleships(8, 5, 'Logic Problems Battleships Number 33', oArgs)

        oGame.horizontal[0] = 5
        oGame.horizontal[1] = 2
        oGame.horizontal[2] = 3
        oGame.horizontal[3] = 3
        oGame.horizontal[4] = 1
        oGame.horizontal[5] = 5
        oGame.horizontal[6] = 1
        oGame.horizontal[7] = 5
        oGame.vertical[0] = 6
        oGame.vertical[1] = 1
        oGame.vertical[2] = 4
        oGame.vertical[3] = 1
        oGame.vertical[4] = 6
        oGame.vertical[5] = 2
        oGame.vertical[6] = 3
        oGame.vertical[7] = 2

        oGame.solve_game = True
    elif index == 34:
        oGame = battleships.CBattleships(8, 5, 'Logic Problems Battleships Number 34', oArgs)

        oGame.horizontal[0] = 4
        oGame.horizontal[1] = 1
        oGame.horizontal[2] = 3
        oGame.horizontal[3] = 2
        oGame.horizontal[4] = 4
        oGame.horizontal[5] = 3
        oGame.horizontal[6] = 3
        oGame.horizontal[7] = 5
        oGame.vertical[0] = 5
        oGame.vertical[1] = 1
        oGame.vertical[2] = 5
        oGame.vertical[3] = 1
        oGame.vertical[4] = 5
        oGame.vertical[5] = 1
        oGame.vertical[6] = 4
        oGame.vertical[7] = 3

        oGame.solve_game = True
    else:
        oGame = battleships.CBattleships(9, 5, 'Logic Problems Battleships Number 35', oArgs)

        oGame.horizontal[0] = 2
        oGame.horizontal[1] = 1
        oGame.horizontal[2] = 3
        oGame.horizontal[3] = 5
        oGame.horizontal[4] = 1
        oGame.horizontal[5] = 4
        oGame.horizontal[6] = 2
        oGame.horizontal[7] = 3
        oGame.horizontal[8] = 4
        oGame.vertical[0] = 5
        oGame.vertical[1] = 2
        oGame.vertical[2] = 1
        oGame.vertical[3] = 4
        oGame.vertical[4] = 1
        oGame.vertical[5] = 6
        oGame.vertical[6] = 2
        oGame.vertical[7] = 1
        oGame.vertical[8] = 3

        oGame.mask[4] = 1
        oGame.mask[7] = 1
        oGame.mask[8] = 1

        oGame.negative_mask[3] = 1 + 2
        oGame.negative_mask[4] = 2
        oGame.negative_mask[5] = 1 + 2
        oGame.negative_mask[6] = 2
        oGame.negative_mask[7] = 2
        oGame.negative_mask[8] = 2



        oGame.solve_game = True

    return oGame
