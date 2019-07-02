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
import modGetGame




def Write(sText : str):
    ''' Write the text to the output without a linefeed. '''
    print(sText, end='')
    oFile = open('results.txt', 'a')
    oFile.write(sText)
    oFile.close()



def WriteLine(sText: str):
    ''' Write the text to the output and add a linefeed. '''
    print(sText)
    oFile = open('results.txt', 'a')
    oFile.write(sText)
    oFile.write("\n")
    oFile.close()



def DisplayLine(nNumPositions, nLine):
    ''' Function to display a horizontal line in a Battleship problem '''
    nMask = 1
    for nPos in range(0, nNumPositions):
        if nLine & nMask == nMask:
            Write(u"\u2588")
        else:
            Write(u"\u00B7")
        nMask *= 2



def CountSolids(nLine):
    ''' Returns the number of solids in the specified line position. '''
    sBinary = '{0:b}'.format(nLine)
    nCount = 0
    for nPos in range (0, len(sBinary)):
        if sBinary[nPos] == '1':
            nCount = nCount + 1
    return nCount



def GetLongestShip(nLine):
    ''' Returns the size of the longest ship on the line. '''
    sBinary = '{0:b}'.format(nLine)
    nMaximum = 0
    nCurrent = 0
    for nPos in range (0, len(sBinary)):
        if sBinary[nPos] == '1':
            nCurrent = nCurrent + 1
            if nCurrent > nMaximum:
                nMaximum = nCurrent
        else:
            nCurrent = 0
    return nMaximum



def CountShipsOnLine(nLine, Ships):
    ''' Counts the number and size of ships on the line. '''
    sBinary = '{0:b}'.format(nLine)
    nCurrent = 0
    for nPos in range (0, len(sBinary)):
        if sBinary[nPos] == '1':
            nCurrent = nCurrent + 1
        else:
            if nCurrent > 1:
                Ships[nCurrent] = Ships[nCurrent]+1
            nCurrent = 0
    if nCurrent > 1:
        Ships[nCurrent] = Ships[nCurrent]+1
    return True



def GetPossibleLines(nNumPositions, nNumSolid, nMaxShip, nMask, nNegativeMask):
    ''' Returns the set of possible lines that have the specified number of solid positions. '''
    # print('GetPossibleLines({}, {}, {}, {}, {})'.format(nNumPositions, nNumSolid, nMaxShip, nMask, nNegativeMask))
    listResult = []
    nMaximum = (2 ** nNumPositions)-1
    for nPos in range(0, nMaximum):
        if CountSolids(nPos) == nNumSolid:
            if nPos & nMask == nMask:
                if (~nPos) & nNegativeMask == nNegativeMask:
                    if GetLongestShip(nPos) <= nMaxShip:
                        listResult.append(nPos)
    return listResult



def AnyThreadRunning(Threads):
    ''' Returns True if any of the specified threads are running. '''
    bRunning = False
    for Thread in Threads:
        if Thread.poll() is None:
            bRunning = True
    return bRunning



class CBattleships():
    ''' Class to represent a game of Battleships. '''



    def __init__(self, nGrid, nMaxShip, sLabel, oArgs):
        ''''
        Class Constructor.

        :ivar int nGrid: Specifies the grid size for the game of battleships.
        :ivar int nMaxShip: Specifies the size of the largest battleship.  Expected 4 or 5.
        :ivar string sLabel: Specifies a label for the problem.
        '''
        self.grid = nGrid
        self.max_ship = nMaxShip
        self.horizontal = []
        self.vertical = []
        self.mask = []
        self.negative_mask = []
        self.line = []
        self.check_ships = True
        self.start_search = 0
        self.finish_search = 100
        self.indent = 2
        self.label = sLabel
        self.transpose = False
        self.solve_game = True
        self.show_remain_time = False
        for nRow in range(0, self.grid):
            self.horizontal.append(1)
            self.vertical.append(1)
            self.line.append(0)
            self.mask.append(0)
            self.negative_mask.append(0)
        if oArgs != None:
            self.ApplyParameters(oArgs)



    def VerticalLine(self, nIndex):
        ''' Calculates the score for the vertical line. '''
        nMask = 2 ** nIndex
        nLine = 0
        for nRow in range(self.grid):
            if self.line[nRow] & nMask == nMask:
                nLine = nLine + 2**nRow
        return nLine



    def IsShip(self, X, Y):
        ''' Returns true if the specified position is ship in the current position. '''
        # Allow questions outside the grid.  The answer is false.
        if X < 0 or X >= self.grid or Y < 0 or Y >= self.grid:
            return False

        # Search on the board.
        nMask = 2 ** X
        return self.line[Y] & nMask == nMask



    def GetShips(self):
        ''' Returns the number and size of the ships. '''
        Ships = []
        for nSize in range(0, self.max_ship+1):
            Ships.append(0)
        for nRow in range(0, self.grid):
            CountShipsOnLine(self.line[nRow], Ships)
            CountShipsOnLine(self.VerticalLine(nRow), Ships)
        ShipsOne = self.total_ships
        for nSize in range(0, self.max_ship+1):
            ShipsOne = ShipsOne - nSize * Ships[nSize]
        Ships[1] = ShipsOne

        return Ships



    def Print(self):
        ''' Print the current game position. '''
        # Get the number and size of ships.
        Ships = self.GetShips()

        # Display the game position.
        print('\033[K', end='')
        Write(u"\u250F")
        for Y in range(0, self.grid):
            Write(u"\u2501")
        Write(u"\u2513")
        if self.transpose:
            Write('\033[40`')
            Write(u"\u250F")
            for Y in range(0, self.grid):
                Write(u"\u2501")
            Write(u"\u2513")
        WriteLine('')

        for nRow in range(0, self.grid):
            print('\033[K', end='')
            Write(u"\u2503")
            DisplayLine(self.grid, self.line[nRow])
            Write(u"\u2503")
            Write('{}'.format(self.horizontal[nRow]))

            if nRow <= self.max_ship and nRow >= 1:
                Write('  {} x {} '.format(Ships[nRow], nRow))
                for nSize in range(0, nRow):
                    Write(u"\u2588")

            if self.transpose:
                Write('\033[40`')
                Write(u"\u2503")
                nMask = 2**nRow
                for nPos in range(0, self.grid):
                    if self.line[nPos] & nMask == nMask:
                        Write(u"\u2588")
                    else:
                        Write(u"\u00B7")
                Write(u"\u2503")
            WriteLine('')

            # print(self.horizontal[nRow], end='')
            # print('{}, {}'.format(self.line[nRow], self.VerticalLine(nRow)))

        Write(u"\u2517")
        for Y in range(0, self.grid):
            Write(u"\u2501")
        Write(u"\u251B")
        if self.transpose:
            Write('\033[40`')
            Write(u"\u2517")
            for Y in range(0, self.grid):
                Write(u"\u2501")
            Write(u"\u251B")
        WriteLine('')

        Write(' ')
        for nRow in range(0, self.grid):
            Write('{}'.format(self.vertical[nRow]))
        WriteLine('')

        #for X in range(0, self.grid):
        #    for Y in range(0, self.grid):
        #        if self.IsShip(X, Y):
        #            print('({},{}) '.format(X, Y), end='')
        #print()



    def IsValidSolution(self):
        ''' Returns true if the current position is valid solution to the problem. '''

        for nRow in range(0, self.grid):
            nLine = self.VerticalLine(nRow)

            # Check that the vertical lines match the conditions
            if CountSolids(nLine) != self.vertical[nRow]:
                return False

            # Check the length of the battle ships.
            if GetLongestShip(nLine) > self.max_ship:
                return False

        # Check the ships are not touching.
        for X in range(0, self.grid):
            for Y in range(0, self.grid):
                if self.IsShip(X, Y):
                    # Check the diaoctals.
                    if self.IsShip(X-1, Y-1):
                        return False
                    if self.IsShip(X+1, Y-1):
                        return False
                    if self.IsShip(X-1, Y+1):
                        return False
                    if self.IsShip(X+1, Y+1):
                        return False

        # Optionally check for the correct number of ships.
        if self.check_ships:
            Ships = self.GetShips()
            if Ships[1] != 4:
                return False
            if Ships[2] != 3:
                return False
            if Ships[3] != 2:
                return False
            if Ships[4] != 1:
                return False

        # Looks good!!
        return True



    def CheckTouching(self):
        ''' Report the touching status of the solution. '''
        for X in range(0, self.grid):
            for Y in range(0, self.grid):
                if self.IsShip(X, Y):
                    # Check the diaoctals.
                    if self.IsShip(X-1, Y-1):
                        print('Touching at ({},{}) and ({},{})'.format(X, Y, X-1, Y-1))
                    if self.IsShip(X+1, Y-1):
                        print('Touching at ({},{}) and ({},{})'.format(X, Y, X+1, Y-1))
                    if self.IsShip(X-1, Y+1):
                        print('Touching at ({},{}) and ({},{})'.format(X, Y, X-1, Y+1))
                    if self.IsShip(X+1, Y+1):
                        print('Touching at ({},{}) and ({},{})'.format(X, Y, X+1, Y+1))



    def GetNumPossible(self, nLevel):
        nAnswer = 1
        for index in range(nLevel, self.grid):
            nAnswer = nAnswer * len(self.posibilities[index])
        return nAnswer



    def Search(self, nLevel):
        ''' Search for a solution at the specified level. '''
        percentage = 100 * self.count / self.number
        if percentage < self.start_search:
            nStep = self.GetNumPossible(nLevel)
            # print('Level = {} Step = {}'.format(nLevel, nStep))
            step_percentage = 100 * ( self.count + nStep ) / self.number
            # print('\tPercentage = {}'.format(step_percentage))
            if step_percentage < self.start_search:
                self.count = self.count + nStep
                return
            else:
                pass
                #print('GO')
        if percentage <= self.finish_search:
            for Possible in self.posibilities[nLevel]:
                self.line[nLevel] = Possible
                if nLevel == self.grid - 1:
                    if percentage >= self.start_search: # and percentage <= self.finish_search:
                        if self.IsValidSolution():
                            WriteLine('\033[K{}'.format(datetime.datetime.now()))
                            self.Print()
                    self.count = self.count + 1
                    # Display the progress on this thread.
                    # if self.count % 100000 == 0:
                    if self.count % 1000000 == 0:
                        # These write an extra space into the next progress box.
                        if self.show_remain_time:
                            # Display estimated time remaining.
                            elapsed_time = time.time() - self.start_time
                            completed = (percentage - self.start_search) / (self.finish_search - self.start_search)
                            total_time = 60 + elapsed_time / completed
                            estimated_time = (1 - completed) * total_time
                            if self.indent > 0:
                                print('\033[{}C {:03.0f}:{:02.0f} '.format(self.indent, estimated_time // 3600, estimated_time % 3600 // 60))
                                print('\033[{}C {:03.0f}:{:02.0f} '.format(self.indent, elapsed_time // 3600, elapsed_time % 3600 // 60))
                                print('\033[{}C {:03.0f}:{:02.0f} '.format(self.indent, total_time // 3600, total_time % 3600 // 60), end='\r\033[2A', flush=True)
                            else:
                                # print('{:>7.3f} '.format(completed), end='\r', flush=True)
                                print(' {:03.0f}:{:02.0f} '.format(estimated_time // 3600, estimated_time % 3600 // 60))
                                print(' {:03.0f}:{:02.0f} '.format(elapsed_time // 3600, elapsed_time % 3600 // 60))
                                print(' {:03.0f}:{:02.0f} '.format(total_time // 3600, total_time % 3600 // 60), end='\r\033[2A', flush=True)
                        else:
                            # Display progress percentage.
                            if self.indent > 0:
                                print('\033[{}C{:>7.3f} '.format(self.indent, percentage), end='\r', flush=True)
                            else:
                                print('{:>7.3f} '.format(percentage), end='\r', flush=True)
                else:
                    self.Search(nLevel+1)



    def ShowInitialPosition(self):
        ''' Returns true if the inital position should be shown. '''
        # if self.start_search == 0: # and self.finish_search == 100:
        #    return True
        return False



    def Solve(self):
        ''' Solve the game of battleships '''
        self.start_time = time.time()
        self.count = 0
        self.number = 1
        self.posibilities = []
        nTotalShipsHorizontal = 0
        nTotalShipsVertical = 0
        if self.ShowInitialPosition():
            WriteLine(self.label)
            Write(u"\u250F")
            for Y in range(0, self.grid):
                Write(u"\u2501")
            WriteLine(u"\u2513")
        for X in range(0, self.grid):
            if self.ShowInitialPosition():
                Write(u"\u2503")
                for Y in range(0, self.grid):
                    nMask = 2 ** Y
                    if self.mask[X] & nMask == nMask:
                        Write(u"\u2588")
                    elif self.negative_mask[X] & nMask == nMask:
                        Write(u"\u00B7")
                    else:
                        Write(' ')
                Write(u"\u2503")
            # print('{} {} {}'.format(self.horizontal[X], self.mask[X], self.negative_mask[X]))
            PossibleLines = GetPossibleLines(self.grid, self.horizontal[X], self.max_ship, self.mask[X], self.negative_mask[X])
            self.posibilities.append(PossibleLines)
            self.number = self.number * len(PossibleLines)
            if self.ShowInitialPosition():
                WriteLine('{}    There are {} possible lines.'.format(self.horizontal[X], len(PossibleLines)))

            nTotalShipsHorizontal = nTotalShipsHorizontal + self.horizontal[X]
            nTotalShipsVertical = nTotalShipsVertical + self.vertical[X]

        if self.ShowInitialPosition():
            Write(u"\u2517")
            for Y in range(0, self.grid):
                Write(u"\u2501")
            WriteLine(u"\u251B")

            Write(' ')
            for nRow in range(0, self.grid):
                Write('{}'.format(self.vertical[nRow]))
            WriteLine('')

            WriteLine('Search space is {:,}'.format(self.number))

        if nTotalShipsHorizontal == nTotalShipsVertical:
            self.total_ships = nTotalShipsHorizontal
            if self.number > 0:
                if self.solve_game:
                    self.Search(0)
                    # These write an extra space into the next progress box.
                    if self.indent > 0:
                        print('\033[{}C ------ '.format(self.indent), end='\r', flush=True)
                    else:
                        print(' ------ ', end='\r', flush=True)
            # print('Search Space  {:,}'.format(self.number))
            # print('Actual Search {:,}'.format(self.count))
        else:
            print('Total ships horizontal != ships vertical. {} != {}'.format(nTotalShipsHorizontal, nTotalShipsVertical))
        # print('Finished')



    def ApplyParameters(self, oArgs):
        ''' Apply the parameters to the game object. '''
        if oArgs.start != None:
            self.start_search = float(oArgs.start)
        if oArgs.finish != None:
            self.finish_search = float(oArgs.finish)
        if oArgs.indent != None:
            self.indent = int(oArgs.indent)
        if oArgs.threads != None:
            self.solve_game = False
        if oArgs.transpose:
            self.transpose = True
        if oArgs.remain:
            self.show_remain_time = True



    def Transpose(self):
        ''' Switch the game on it's side. '''
        for X in range(0, self.grid):
            nTemp = self.horizontal[X]
            self.horizontal[X] = self.vertical[X]
            self.vertical[X] = nTemp

        TransposedMask = []
        nMask = 1
        for X in range(0, self.grid):
            nAdd = 1
            nWork = 0
            for Y in range(0, self.grid):
                # print('{} {}'.format(self.mask[Y], nMask))
                if self.mask[Y] & nMask == nMask:
                    nWork |= nAdd
                nAdd *= 2
            TransposedMask.append(nWork)
            nMask *= 2

        for X in range(0, self.grid):
            self.mask[X] = TransposedMask[X]


        TransposedMask = []
        nMask = 1
        for X in range(0, self.grid):
            nAdd = 1
            nWork = 0
            for Y in range(0, self.grid):
                # print('{} {}'.format(self.mask[Y], nMask))
                if self.negative_mask[Y] & nMask == nMask:
                    nWork |= nAdd
                nAdd *= 2
            TransposedMask.append(nWork)
            nMask *= 2

        for X in range(0, self.grid):
            self.negative_mask[X] = TransposedMask[X]



def Main():
    # Process the command line arguments.
    # This might end the program (--help).
    oParse = argparse.ArgumentParser(prog='battleships', description='Solver for Battleships.')
    oParse.add_argument('-g', '--game', help='The index of the game to solve.', action='store')
    oParse.add_argument('-s', '--start', help='The starting percentage.', action='store')
    oParse.add_argument('-f', '--finish', help='The finish percentage.', action='store')
    oParse.add_argument('-i', '--indent', help='The indent for the progress percentage.', action='store')
    oParse.add_argument('-t', '--threads', help='Split the program into threads.', action='store')
    oParse.add_argument('-p', '--transpose', help='Switch the problem 90 degrees.', action='store_true')
    oParse.add_argument('-r', '--remain', help='Display estimated time remaining not progress.', action='store_true')
    oParse.add_argument('-v', '--verbose', help='Increase the output level.', action='store_true')

    oArgs = oParse.parse_args()

    # Display the parameters.
    if oArgs.verbose:
        print(sys.argv)

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

    oGame = modGetGame.GetGame(nGame, oArgs)

    if oGame.transpose:
        oGame.Transpose()

    if oArgs.threads == None:
        bShowGame = True
    else:
        nThreads = int(oArgs.threads)
        if nThreads > 1:
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

        WriteLine('Search space is {:,}.  log = {:0.2f}'.format(nNumber, math.log10(nNumber)))

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
            nIndent = 0
            Threads = []
            for nIndex in range(0, nSplit-1):
                if oArgs.verbose:
                    print('Thread({}) --game={} --start={} --finish={} --indent={} --threads={}'.format(nIndex, nGame, fStart, fStart + fAmount, nIndent, 1))
                oCommand = [__file__, '--game', '{}'.format(nGame) , '--start', '{}'.format(fStart), '--finish', '{}'.format(fStart + fAmount), '--indent', '{}'.format(nIndent), '--threads', '1']
                if oGame.transpose:
                    oCommand.append('-p')
                if oGame.show_remain_time:
                    oCommand.append('-r')
                if oArgs.verbose:
                    oCommand.append('-v')
                Threads.append(subprocess.Popen(oCommand))
                fStart = fStart + fAmount
                nIndent = nIndent + 7
            if oGame.finish_search >= 100:
                if oArgs.verbose:
                    print('Thread({}) --game={} --start={} --indent={} --threads={}'.format(nSplit-1, nGame, fStart, nIndent, 1))
                oCommand = [__file__, '--game', '{}'.format(nGame), '--start', '{}'.format(fStart), '--indent', '{}'.format(nIndent), '--threads', '1']
                if oGame.transpose:
                    oCommand.append('-p')
                if oGame.show_remain_time:
                    oCommand.append('-r')
                if oArgs.verbose:
                    oCommand.append('-v')
                Threads.append(subprocess.Popen(oCommand))
            else:
                if oArgs.verbose:
                    print('Thread({}) --game={} --start={} --finish={} --indent={} --threads={}'.format(nSplit-1, nGame, fStart, oGame.finish_search, nIndent, 1))
                oCommand = [__file__, '--game', '{}'.format(nGame), '--start', '{}'.format(fStart), '--finish', '{}'.format(oGame.finish_search), '--indent', '{}'.format(nIndent), '--threads', '1']
                if oGame.transpose:
                    oCommand.append('-p')
                if oGame.show_remain_time:
                    oCommand.append('-r')
                if oArgs.verbose:
                    oCommand.append('-v')
                Threads.append(subprocess.Popen(oCommand))

            while AnyThreadRunning(Threads):
                time.sleep(10)
            if oArgs.remain:
                print()
                print()
            print()
            print('\033[KFinished.')

        # Exit this script.
        # quit()



if __name__ == '__main__':
    Main()
