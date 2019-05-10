#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Module to define BattleShip problems from the Logic Problems game.
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
    else:
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

    return oGame




if __name__ == '__main__':
    # Process the command line arguments.
    # This might end the program (--help).
    oParse = argparse.ArgumentParser(prog='battleships', description='Solver for Battleships.')
    oParse.add_argument('-g', '--game', help='The index of the game to solve.', action='store')
    oParse.add_argument('-s', '--start', help='The starting percentage.', action='store')
    oParse.add_argument('-f', '--finish', help='The finish percentage.', action='store')
    oParse.add_argument('-i', '--indent', help='The indent for the progress percentage.', action='store')
    oParse.add_argument('-t', '--threads', help='Split the program into threads.', action='store')
    oParse.add_argument('-v', '--verbose', help='Increase the output level.', action='store_true')

    oArgs = oParse.parse_args()

    # Reset the output file.
    if oArgs.threads == None:
        oFile = open('results.txt', 'w')
        oFile.close()
    else:
        nThreads = int(oArgs.threads)
        if nThreads > 1:
            oFile = open('results.txt', 'w')
            oFile.close()

    # Indentify the game to solve.
    bShowGame = False
    nGame = 0
    if oArgs.game != None:
        try:
            nGame = int(oArgs.game)
        except:
            pass
    while nGame == 0:
        bShowGame = True
        print('Please enter the game number.')
        nGame = input()
        try:
            nGame = int(nGame)
        except:
            print('I do not understand')
            nGame = 0
    # print('Game = {}'.format(nGame))

    oGame = GetGame(nGame, oArgs)

    if oArgs.threads == None:
        bShowGame = True

    if bShowGame:
        WriteLine(oGame.label)
        Write(u"\u250F")
        for Y in range(0, oGame.grid):
            Write(u"\u2501")
        WriteLine(u"\u2513")
        nNumber = 1
        for X in range(0, oGame.grid):
            PossibleLines = GetPossibleLines(oGame.grid, oGame.horizontal[X], oGame.max_ship, oGame.mask[X], oGame.negative_mask[X])
            nNumber = nNumber * len(PossibleLines)

            Write(u"\u2503")
            for Y in range(0, oGame.grid):
                nMask = 2 ** Y
                if oGame.mask[X] & nMask == nMask:
                    Write(u"\u2588")
                elif oGame.negative_mask[X] & nMask == nMask:
                    Write(u"\u00B7")
                else:
                    Write(' ')
            Write(u"\u2503")
            WriteLine('{}     {:4n} {:4n}    There are {} possible lines.'.format(oGame.horizontal[X], oGame.mask[X], oGame.negative_mask[X], len(PossibleLines)))

        Write(u"\u2517")
        for Y in range(0, oGame.grid):
            Write(u"\u2501")
        WriteLine(u"\u251B")

        Write(' ')
        for nRow in range(0, oGame.grid):
            Write('{}'.format(oGame.vertical[nRow]))
        WriteLine('')

        WriteLine('Search space is {:,}'.format(nNumber))

    if oArgs.threads != None:
        nThreads = int(oArgs.threads)
        if nThreads <= 1:
            # Give the other threads time to output initial status.
            time.sleep(1)

            # print('oArgs.threads = {}.'.format(nThreads))
            # Solve the specified game.
            oGame.Solve()
        else:
            # print('oArgs.threads = {}.'.format(nThreads))
            import subprocess
            nSplit = nThreads
            if nSplit > 20:
                nSplit = 20
            elif nSplit < 2:
                nSplit = 2

            fAmount = float((oGame.finish_search - oGame.start_search) / nSplit)
            fStart = oGame.start_search
            nIndent = 2
            Threads = []
            for nIndex in range(0, nSplit-1):
                if oArgs.verbose:
                    print('Thread({}) --game {} --start={} --finish={} --indent={} --threads={}'.format(nIndex, nGame, fStart, fStart + fAmount, nIndent, 1))
                Threads.append(subprocess.Popen([__file__, '--game', '{}'.format(nGame) , '--start', '{}'.format(fStart), '--finish', '{}'.format(fStart + fAmount), '--indent', '{}'.format(nIndent), '--threads', '1']))
                fStart = fStart + fAmount
                nIndent = nIndent + 7
            if oGame.finish_search >= 100:
                if oArgs.verbose:
                    print('Thread({}) --game={} --start={} --indent={} --threads={}'.format(nSplit-1, nGame, fStart, nIndent, 1))
                Threads.append(subprocess.Popen([__file__, '--game', '{}'.format(nGame), '--start', '{}'.format(fStart), '--indent', '{}'.format(nIndent), '--threads', '1']))
            else:
                if oArgs.verbose:
                    print('Thread({}) --game={} --start={} --finish={} --indent={} --threads={}'.format(nSplit-1, nGame, fStart, oGame.finish_search, nIndent, 1))
                Threads.append(subprocess.Popen([__file__, '--game', '{}'.format(nGame), '--start', '{}'.format(fStart), '--finish', '{}'.format(oGame.finish_search), '--indent', '{}'.format(nIndent), '--threads', '1']))

            while AnyThreadRunning(Threads):
                time.sleep(10)
            print('\033[KFinished.')

        # Exit this script.
        # quit()
