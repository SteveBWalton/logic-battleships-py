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
        self.solve_game = True
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
        Write(u"\u250F")
        for Y in range(0, self.grid):
            Write(u"\u2501")
        WriteLine(u"\u2513")
        for nRow in range(0, self.grid):
            Write(u"\u2503")
            DisplayLine(self.grid, self.line[nRow])
            Write(u"\u2503")
            Write('{}'.format(self.horizontal[nRow]))

            if nRow <= self.max_ship and nRow >= 1:
                Write('  {} x {} '.format(Ships[nRow], nRow))
                for nSize in range(0, nRow):
                    Write(u"\u2588")
            WriteLine('')

            # print(self.horizontal[nRow], end='')
            # print('{}, {}'.format(self.line[nRow], self.VerticalLine(nRow)))
        Write(u"\u2517")
        for Y in range(0, self.grid):
            Write(u"\u2501")
        WriteLine(u"\u251B")

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
                if nLevel == self.grid-1:
                    if percentage >= self.start_search: # and percentage <= self.finish_search:
                        if self.IsValidSolution():
                            WriteLine('\033[K{}'.format(datetime.datetime.now()))
                            self.Print()
                    self.count = self.count + 1
                    # Display the progress on this thread.
                    if self.count % 100000 == 0:
                        print('\033[{}C{:.3f}'.format(self.indent, percentage), end='\r', flush=True)
                else:
                    self.Search(nLevel+1)



    def ShowInitialPosition(self):
        ''' Returns true if the inital position should be shown. '''
        if self.start_search == 0: # and self.finish_search == 100:
            return True
        return False



    def Solve(self):
        ''' Solve the game of battleships '''
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
                    print('\033[{}C------'.format(self.indent), end='\r', flush=True)
            # print('Search Space  {:,}'.format(self.number))
            # print('Actual Search {:,}'.format(self.count))
        else:
            print('Total ships horizontal != ships vertical. {} != {}'.format(nTotalShipsHorizontal, nTotalShipsVertical))
        # print('Finished')



    def ApplyParameters(self, oArgs):
        ''' Apply the parameters to the game object. '''
        if oArgs.start != None:
            self.start_search = int(oArgs.start)
        if oArgs.finish != None:
            self.finish_search = int(oArgs.finish)
        if oArgs.indent != None:
            self.indent = int(oArgs.indent)
        if oArgs.threads != None:
            self.solve_game = False



def GetGame(index, oArgs):
    ''' Return a game object for the specified game. '''
    if index == 1:
        oGame = CBattleships(10, 4, 'Logic Problems Battleships Number 1', oArgs)

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
        oGame = CBattleships(10, 4, 'Logic Problems Battleships Number 2', oArgs)

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
        oGame = CBattleships(10, 4, 'Logic Problems Battleships Number 3', oArgs)

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
        oGame.negative_mask[7] = 64 + 256
        oGame.negative_mask[8] = 2 + 64 + 128 + 256 + 512
        oGame.negative_mask[9] = 1 + 2 + 256

        oGame.solve_game = True
    elif index == 24:
        oGame = CBattleships(8, 5, 'Logic Problems Battleships Number 24', oArgs)

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
        oGame = CBattleships(8, 5, 'Logic Problems Battleships Number 26', oArgs)

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
    else:
        oGame = CBattleships(8, 5, 'Logic Problems Battleships Number 27', oArgs)

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
        oGame.negative_mask[6] = 64

        #oGame.mask[0] = 4 + 8 + 16 + 32
        #oGame.negative_mask[0] = 1 + 2
        #oGame.mask[1] = 1
        #oGame.negative_mask[1] = 2 + 4 + 8 + 16 + 32 + 64 + 128
        #oGame.mask[2] = 8 + 32 + 64 +128
        #oGame.negative_mask[2] = 4 + 16
        #oGame.mask[3] = 8
        #oGame.negative_mask[3] = 4 + 16 + 32 + 64 + 128
        #oGame.mask[4] = 8
        #oGame.negative_mask[4] = 4 + 16 + 64 + 128
        #oGame.mask[5] = 8 + 128
        #oGame.negative_mask[5] = 4 + 32 + 64
        #oGame.mask[6] = 128
        #oGame.negative_mask[6] = 4 + 8 + 16 + 32 + 64
        #oGame.mask[7] = 8 + 16
        #oGame.negative_mask[7] = 4 + 64

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
            # print('oArgs.threads = {}.'.format(nThreads))
            # Solve the specified game.
            oGame.Solve()
            pass
        else:
            # print('oArgs.threads = {}.'.format(nThreads))
            import subprocess
            import time
            nSplit = nThreads
            if nSplit > 20:
                nSplit = 20
            elif nSplit < 2:
                nSplit = 2

            nAmount = int(100 / nSplit)
            nStart = 0
            nIndent = 2
            Threads = []
            for nIndex in range(0, nSplit-1):
                # print('Thread --game={} --start={} --finish={} --indent={} --threads={}'.format(nGame, nStart, nStart+nAmount, nIndent, 1))
                Threads.append(subprocess.Popen([__file__, '--game', '{}'.format(nGame) , '--start', '{}'.format(nStart), '--finish', '{}'.format(nStart+nAmount), '--indent', '{}'.format(nIndent), '--threads', '1']))
                nStart = nStart + nAmount
                nIndent = nIndent + 7
            # print('Thread --game={} --start={} --indent={} --threads={}'.format(nGame, nStart, nIndent, 1))
            Threads.append(subprocess.Popen([__file__, '--game', '{}'.format(nGame), '--start', '{}'.format(nStart), '--indent', '{}'.format(nIndent), '--threads', '1']))

            while AnyThreadRunning(Threads):
                time.sleep(10)
            print('\033[KFinished.')

        # Exit this script.
        # quit()
