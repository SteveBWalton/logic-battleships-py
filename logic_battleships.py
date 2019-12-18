#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Module to solve BattleShip problems from the Logic Problems game.
'''

# System libraries for the initial phase.
import sys
import os
import argparse
import datetime
import time
import math

# Application libraries.
from battleships import Battleships, write, writeLine, getPossibleLines, isAnyThreadRunning
from getgame import getGame



def main():
    # Process the command line arguments.
    # This might end the program (--help).
    argParse = argparse.ArgumentParser(prog='battleships', description='Solver for Battleships.')
    argParse.add_argument('-g', '--game', help='The index of the game to solve.', action='store')
    argParse.add_argument('-s', '--start', help='The starting percentage.', action='store')
    argParse.add_argument('-f', '--finish', help='The finish percentage.', action='store')
    argParse.add_argument('-i', '--indent', help='The indent for the progress percentage.', action='store')
    argParse.add_argument('-t', '--threads', help='Split the program into threads.', action='store')
    argParse.add_argument('-p', '--transpose', help='Switch the problem 90 degrees.', action='store_true')
    argParse.add_argument('-r', '--remain', help='Display estimated time remaining not progress.', action='store_true')
    argParse.add_argument('-k', '--keep', help='Keep the existing log file.', action='store_true')
    argParse.add_argument('-l', '--large', help='Guess the positions of the 4 and 5 ships.', action='store_true')
    argParse.add_argument('-m', '--mask', help='Specify additional information.', metavar='N', type=int, nargs='+')
    argParse.add_argument('-v', '--verbose', help='Increase the output level.', action='store_true')

    args = argParse.parse_args()

    # Display the parameters.
    if args.verbose:
        print(sys.argv)

    # Reset the output file.
    if args.keep:
        pass
    else:
        if args.threads == None:
            oFile = open('results.txt', 'w')
            oFile.close()
        else:
            numThreads = int(args.threads)
            if numThreads > 1:
                oFile = open('results.txt', 'w')
                oFile.close()

    # Indentify the game to solve.
    isShowGame = False
    gameNumber = 0
    if args.game != None:
        try:
            gameNumber = int(args.game)
        except:
            pass
    while gameNumber == 0:
        isShowGame = True
        print('Please enter the game number.')
        gameNumber = input()
        try:
            gameNumber = int(gameNumber)
        except:
            print('I do not understand')
            gameNumber = 0
    # print('Game = {}'.format(gameNumber))

    game = getGame(gameNumber, args)

    if args.mask:
        for i in range(0, len(args.mask)):
            game.mask[i] |= args.mask[i]

    if game.isTranspose:
        game.transpose()

    if args.threads == None:
        isShowGame = True
    else:
        numThreads = int(args.threads)
        if numThreads > 1:
            isShowGame = True

    if isShowGame:
        writeLine(game.label)
        write(u"\u250F")
        for y in range(0, game.grid):
            write(u"\u2501")
        writeLine(u"\u2513")
        nNumber = 1
        for x in range(0, game.grid):
            possibleLines = getPossibleLines(game.grid, game.horizontal[x], game.maxShip, game.mask[x], game.negativeMask[x])
            nNumber *= len(possibleLines)

            write(u"\u2503")
            for y in range(0, game.grid):
                mask = 2 ** y
                if game.mask[x] & mask == mask:
                    write(u"\u2588")
                elif game.negativeMask[x] & mask == mask:
                    write(u"\u00B7")
                else:
                    write(' ')
            write(u"\u2503")
            writeLine('{}     {:4n} {:4n}    There are {} possible lines.'.format(game.horizontal[x], game.mask[x], game.negativeMask[x], len(possibleLines)))

        write(u"\u2517")
        for y in range(0, game.grid):
            write(u"\u2501")
        writeLine(u"\u251B")

        write(' ')
        for row in range(0, game.grid):
            write('{}'.format(game.vertical[row]))
        writeLine('')

        if nNumber > 0:
            logNumber = math.log10(nNumber)
        else:
            logNumber = 0
        writeLine('Search space is {:,}.  log = {:0.2f}'.format(nNumber, logNumber))

    if args.threads != None:
        numThreads = int(args.threads)
        if numThreads <= 1:
            # Give the other threads time to output initial status.
            time.sleep(1)

            # print('args.threads = {}.'.format(numThreads))
            # Solve the specified game.
            game.solve()
        else:
            if args.large:
                game.guessLargeShips()
            else:
                # print('args.threads = {}.'.format(numThreads))
                import subprocess
                nSplit = numThreads
                if nSplit > 20:
                    nSplit = 20
                elif nSplit < 2:
                    nSplit = 2

                fAmount = float((game.finishSearch - game.startSearch) / nSplit)
                fStart = game.startSearch
                indent = 0
                threads = []
                for i in range(0, nSplit-1):
                    if args.verbose:
                        print('Thread({}) --game={} --start={} --finish={} --indent={} --threads={}'.format(i, gameNumber, fStart, fStart + fAmount, indent, 1))
                    command = [__file__, '--game', '{}'.format(gameNumber) , '--start', '{}'.format(fStart), '--finish', '{}'.format(fStart + fAmount), '--indent', '{}'.format(indent), '--threads', '1']
                    if game.isTranspose:
                        command.append('-p')
                    if args.verbose:
                        command.append('-v')
                    if args.mask:
                        command.append('--mask')
                        for i in range(0, len(args.mask)):
                            command.append('{}'.format(args.mask[i]))
                    threads.append(subprocess.Popen(command))
                    fStart += fAmount
                    indent += 7
                if game.finishSearch >= 100:
                    if args.verbose:
                        print('Thread({}) --game={} --start={} --indent={} --threads={}'.format(nSplit-1, gameNumber, fStart, indent, 1))
                    command = [__file__, '--game', '{}'.format(gameNumber), '--start', '{}'.format(fStart), '--indent', '{}'.format(indent), '--threads', '1']
                    if game.isTranspose:
                        command.append('-p')
                    if args.verbose:
                        command.append('-v')
                    if args.mask:
                        command.append('--mask')
                        for i in range(0, len(args.mask)):
                            command.append('{}'.format(args.mask[i]))
                    threads.append(subprocess.Popen(command))
                else:
                    if args.verbose:
                        print('Thread({}) --game={} --start={} --finish={} --indent={} --threads={}'.format(nSplit-1, gameNumber, fStart, game.finishSearch, indent, 1))
                    command = [__file__, '--game', '{}'.format(gameNumber), '--start', '{}'.format(fStart), '--finish', '{}'.format(game.finishSearch), '--indent', '{}'.format(indent), '--threads', '1']
                    if game.isTranspose:
                        command.append('-p')
                    if args.verbose:
                        command.append('-v')
                    threads.append(subprocess.Popen(command))

                while isAnyThreadRunning(threads):
                    time.sleep(10)
                print()
                print()
                print()
                print()
            if args.keep:
                pass
            else:
                print('\033[KFinished.')

        # Exit this script.
        # quit()



if __name__ == '__main__':
    main()
