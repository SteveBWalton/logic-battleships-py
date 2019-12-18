#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Module to implement the BattleShips class.
'''

# System libraries for the initial phase.
import sys
import os
import argparse
import datetime
import time
import math
import copy
import subprocess

# Application libraries.



class Battleships():
    ''' Class to represent a game of Battleships. '''



    def __init__(self, gameNumber, grid, maxShip, label, args):
        ''''
        Class Constructor.

        :ivar int grid: Specifies the grid size for the game of battleships.
        :ivar int maxShip: Specifies the size of the largest battleship.  Expected 4 or 5.
        :ivar string label: Specifies a label for the problem.
        '''
        self.gameNumber = gameNumber
        self.grid = grid
        self.maxShip = maxShip
        self.horizontal = []
        self.vertical = []
        self.mask = []
        self.negativeMask = []
        self.line = []
        self.isCheckShips = True
        self.startSearch = 0
        self.finishSearch = 100
        self.indent = 2
        self.label = label
        self.isTranspose = False
        self.isSolveGame = True
        for row in range(0, self.grid):
            self.horizontal.append(1)
            self.vertical.append(1)
            self.line.append(0)
            self.mask.append(0)
            self.negativeMask.append(0)
        if args != None:
            self.applyParameters(args)



    def verticalLine(self, index):
        ''' Calculates the score for the vertical line. '''
        mask = 2 ** index
        line = 0
        for row in range(self.grid):
            if self.line[row] & mask == mask:
                line = line + 2**row
        return line



    def isShip(self, x, y):
        ''' Returns true if the specified position is ship in the current position. '''
        # Allow questions outside the grid.  The answer is false.
        if x < 0 or x >= self.grid or y < 0 or y >= self.grid:
            return False

        # Search on the board.
        mask = 2 ** x
        return self.line[y] & mask == mask



    def getShips(self):
        ''' Returns the number and size of the ships on the grid. '''
        ships = []
        for shipSize in range(0, self.maxShip + 1):
            ships.append(0)
        for row in range(0, self.grid):
            countShipsOnLine(self.line[row], ships)
            countShipsOnLine(self.verticalLine(row), ships)
        shipsOne = self.totalShips
        for shipSize in range(0, self.maxShip+1):
            shipsOne -= shipSize * ships[shipSize]
        ships[1] = shipsOne

        return ships



    def write(self):
        ''' Print the current game position. '''
        # Get the number and size of ships.
        ships = self.getShips()

        # Display the game position.
        print('\033[K', end='')
        write(u"\u250F")
        for y in range(0, self.grid):
            write(u"\u2501")
        write(u"\u2513")
        if self.isTranspose:
            write('\033[40`')
            write(u"\u250F")
            for y in range(0, self.grid):
                write(u"\u2501")
            write(u"\u2513")
        writeLine('')

        for row in range(0, self.grid):
            print('\033[K', end='')
            write(u"\u2503")
            displayLine(self.grid, self.line[row])
            write(u"\u2503")
            write('{}'.format(self.horizontal[row]))

            if row <= self.maxShip and row >= 1:
                write('  {} x {} '.format(ships[row], row))
                for nSize in range(0, row):
                    write(u"\u2588")

            if self.isTranspose:
                write('\033[40`')
                write(u"\u2503")
                mask = 2**row
                for pos in range(0, self.grid):
                    if self.line[pos] & mask == mask:
                        write(u"\u2588")
                    else:
                        write(u"\u00B7")
                write(u"\u2503")
            writeLine('')

            # print(self.horizontal[row], end='')
            # print('{}, {}'.format(self.line[row], self.verticalLine(row)))

        print('\033[K', end='')
        write(u"\u2517")
        for y in range(0, self.grid):
            write(u"\u2501")
        write(u"\u251B")
        if self.isTranspose:
            write('\033[40`')
            write(u"\u2517")
            for y in range(0, self.grid):
                write(u"\u2501")
            write(u"\u251B")
        writeLine('')

        print('\033[K', end='')
        write(' ')
        for row in range(0, self.grid):
            write('{}'.format(self.vertical[row]))
        writeLine('')

        #for x in range(0, self.grid):
        #    for y in range(0, self.grid):
        #        if self.isShip(x, y):
        #            print('({},{}) '.format(x, y), end='')
        #print()



    def isPartialSolution(self, shipSize):
        ''' Returns true if the current position does not exceed the boundary conditions and could lead to a valid solultion. '''
        for row in range(0, self.grid):
            # Check the number of blocks.
            if countSolids(self.line[row]) > self.horizontal[row]:
                # print('Too many blocks in row {}. ({}, {})'.format(row+1, countSolids(self.line[row]), self.horizontal[row]))
                return False

            # Check the length of the battle ships.
            if getLongestShip(self.line[row]) > self.maxShip:
                # print('Ship too long in row {}'.format(row+1))
                return False

            # Check the columns.
            line = self.verticalLine(row)
            if countSolids(line) > self.vertical[row]:
                # print('Too many blocks in column {}'.format(row+1))
                return False

            # Check the length of the battle ships.
            if getLongestShip(line) > self.maxShip:
                # print('Ship too long in column {}'.format(row+1))
                return False

        # Check the ships are not touching.
        for x in range(0, self.grid):
            for y in range(0, self.grid):
                if self.isShip(x, y):
                    # Check the diagonals.
                    if self.isShip(x-1, y-1):
                        return False
                    if self.isShip(x+1, y-1):
                        return False
                    if self.isShip(x-1, y+1):
                        return False
                    if self.isShip(x+1, y+1):
                        return False

        ships = self.getShips()

        # Check the maximum size for a 4 this will not work.
        if shipSize == 5:
            if ships[5] != 1:
                # print(ships)
                return False
        if shipSize == 4:
            if ships[5] != 1 or ships[4] != 1:
                # print(ships)
                return False

        # Looks good!!
        return True




    def isValidSolution(self):
        ''' Returns true if the current position is valid solution to the problem. '''

        for row in range(0, self.grid):
            line = self.verticalLine(row)

            # Check that the vertical lines match the conditions
            if countSolids(line) != self.vertical[row]:
                return False

            # Check the length of the battle ships.
            if getLongestShip(line) > self.maxShip:
                return False

        # Check the ships are not touching.
        for x in range(0, self.grid):
            for y in range(0, self.grid):
                if self.isShip(x, y):
                    # Check the diagonals.
                    if self.isShip(x-1, y-1):
                        return False
                    if self.isShip(x+1, y-1):
                        return False
                    if self.isShip(x-1, y+1):
                        return False
                    if self.isShip(x+1, y+1):
                        return False

        # Optionally check for the correct number of ships.
        if self.isCheckShips:
            ships = self.getShips()
            if ships[1] != 4:
                return False
            if ships[2] != 3:
                return False
            if ships[3] != 2:
                return False
            if ships[4] != 1:
                return False

        # Looks good!!
        return True



    def checkTouching(self):
        ''' Report the touching status of the solution. '''
        for x in range(0, self.grid):
            for y in range(0, self.grid):
                if self.isShip(x, y):
                    # Check the diaoctals.
                    if self.isShip(x-1, y-1):
                        print('Touching at ({},{}) and ({},{})'.format(x, y, x-1, y-1))
                    if self.isShip(x+1, y-1):
                        print('Touching at ({},{}) and ({},{})'.format(x, y, x+1, y-1))
                    if self.isShip(x-1, y+1):
                        print('Touching at ({},{}) and ({},{})'.format(x, y, x-1, y+1))
                    if self.isShip(x+1, y+1):
                        print('Touching at ({},{}) and ({},{})'.format(x, y, x+1, y+1))



    def getNumPossible(self, level):
        answer = 1
        for index in range(level, self.grid):
            answer *= len(self.posibilities[index])
        return answer



    def search(self, level):
        ''' Search for a solution at the specified level. '''
        percentage = 100 * self.count / self.number
        if percentage < self.startSearch:
            numSteps = self.getNumPossible(level)
            stepPercentage = 100 * ( self.count + numSteps ) / self.number
            if stepPercentage < self.startSearch:
                self.count += numSteps
                return
            else:
                pass
                #print('GO')
        if percentage <= self.finishSearch:
            for possible in self.posibilities[level]:
                self.line[level] = possible
                if level == self.grid - 1:
                    if percentage >= self.startSearch: # and percentage <= self.finishSearch:
                        if self.isValidSolution():
                            writeLine('\033[K{}'.format(datetime.datetime.now()))
                            self.write()
                    self.count += 1
                    # Display the progress on this thread.
                    # if self.count % 100000 == 0:
                    if self.count % 10000000 == 0:
                        # These write an extra space into the next progress box.
                        elapsedTime = time.time() - self.startTime
                        completed = (percentage - self.startSearch) / (self.finishSearch - self.startSearch)
                        totalTime = elapsedTime / completed
                        estimatedTime = 30 + (1 - completed) * totalTime
                        if self.indent > 0:
                            print('\033[{}C{:>7.3f} '.format(self.indent, percentage))
                            print('\033[{}C {:03.0f}:{:02.0f} '.format(self.indent, estimatedTime // 3600, estimatedTime % 3600 // 60))
                            print('\033[{}C {:03.0f}:{:02.0f} '.format(self.indent, elapsedTime // 3600, elapsedTime % 3600 // 60))
                            print('\033[{}C {:03.0f}:{:02.0f} '.format(self.indent, totalTime // 3600, totalTime % 3600 // 60), end='\r\033[3A', flush=True)
                        else:
                            print('{:>7.3f} '.format(percentage))
                            print(' {:03.0f}:{:02.0f} '.format(estimatedTime // 3600, estimatedTime % 3600 // 60))
                            print(' {:03.0f}:{:02.0f} '.format(elapsedTime // 3600, elapsedTime % 3600 // 60))
                            print(' {:03.0f}:{:02.0f} '.format(totalTime // 3600, totalTime % 3600 // 60), end='\r\033[3A', flush=True)
                else:
                    self.search(level+1)



    def isShowInitialPosition(self):
        ''' Returns true if the inital position should be shown. '''
        # if self.startSearch == 0: # and self.finishSearch == 100:
        #    return True
        return False



    def initialiseGame(self):
        ''' Calculate the totalShips etc. '''
        self.startTime = time.time()
        self.count = 0
        self.number = 1
        self.posibilities = []
        totalShipsHorizontal = 0
        totalShipsVertical = 0
        if self.isShowInitialPosition():
            writeLine(self.label)
            write(u"\u250F")
            for y in range(0, self.grid):
                write(u"\u2501")
            writeLine(u"\u2513")
        for x in range(0, self.grid):
            if self.isShowInitialPosition():
                write(u"\u2503")
                for y in range(0, self.grid):
                    mask = 2 ** y
                    if self.mask[x] & mask == mask:
                        write(u"\u2588")
                    elif self.negativeMask[x] & mask == mask:
                        write(u"\u00B7")
                    else:
                        write(' ')
                write(u"\u2503")
            # print('{} {} {}'.format(self.horizontal[x], self.mask[x], self.negativeMask[x]))
            possibleLines = getPossibleLines(self.grid, self.horizontal[x], self.maxShip, self.mask[x], self.negativeMask[x])
            self.posibilities.append(possibleLines)
            self.number = self.number * len(possibleLines)
            if self.isShowInitialPosition():
                writeLine('{}    There are {} possible lines.'.format(self.horizontal[x], len(possibleLines)))

            totalShipsHorizontal += self.horizontal[x]
            totalShipsVertical += self.vertical[x]

        if self.isShowInitialPosition():
            write(u"\u2517")
            for y in range(0, self.grid):
                write(u"\u2501")
            writeLine(u"\u251B")

            write(' ')
            for row in range(0, self.grid):
                write('{}'.format(self.vertical[row]))
            writeLine('')

            writeLine('Search space is {:,}'.format(self.number))

        if totalShipsHorizontal == totalShipsVertical:
            self.totalShips = totalShipsHorizontal
            return True
        else:
            print('Total ships horizontal != ships vertical. {} != {}'.format(totalShipsHorizontal, totalShipsVertical))
        return False



    def solve(self):
        ''' Solve the game of battleships '''
        if not self.initialiseGame():
            return

        if self.number > 0:
            if self.isSolveGame:
                self.search(0)
                # These write an extra space into the next progress box.
                if self.indent > 0:
                    print('\033[{}C ------ '.format(self.indent), end='\r', flush=True)
                else:
                    print(' ------ ', end='\r', flush=True)



    def applyParameters(self, args):
        ''' Apply the parameters to the game object. '''
        if args.start != None:
            self.startSearch = float(args.start)
        if args.finish != None:
            self.finishSearch = float(args.finish)
        if args.indent != None:
            self.indent = int(args.indent)
        if args.threads != None:
            self.isSolveGame = False
        if args.transpose:
            self.isTranspose = True
        self.numThreads = 1
        if args.threads != None:
            self.numThreads = int(args.threads)



    def transpose(self):
        ''' Switch the game on it's side. '''
        for x in range(0, self.grid):
            temporary = self.horizontal[x]
            self.horizontal[x] = self.vertical[x]
            self.vertical[x] = temporary

        transposedMask = []
        mask = 1
        for x in range(0, self.grid):
            add = 1
            work = 0
            for y in range(0, self.grid):
                # print('{} {}'.format(self.mask[y], mask))
                if self.mask[y] & mask == mask:
                    work |= add
                add *= 2
            transposedMask.append(work)
            mask *= 2

        for x in range(0, self.grid):
            self.mask[x] = transposedMask[x]


        transposedMask = []
        mask = 1
        for x in range(0, self.grid):
            add = 1
            work = 0
            for y in range(0, self.grid):
                # print('{} {}'.format(self.mask[y], mask))
                if self.negativeMask[y] & mask == mask:
                    work |= add
                add *= 2
            transposedMask.append(work)
            mask *= 2

        for x in range(0, self.grid):
            self.negativeMask[x] = transposedMask[x]



    def applyMask(self):
        ''' Set the position to the position defined by the mask. '''
        for x in range(0, self.grid):
            self.line[x] = self.mask[x]




    def guessLargeShips(self):
        ''' Loop through all the possible positions for the large ships. '''
        # print('Loop through all the possible positions for the large ships. ')

        if not self.initialiseGame():
            return

        # Build the initial positions.
        self.applyMask()
        ships = self.getShips()

        shipSize = 0
        if self.maxShip >= 4:
            # print('There should be 1 size 4 ship.')
            # print('There are {} size 4 ships.'.format(ships[4]))
            if ships[4] < 1:
                shipSize = 4
        if self.maxShip >= 5:
            #print('There should be 1 size 5 ship.')
            #print('There are {} size 5 ships.'.format(ships[5]))
            if ships[5] < 1:
                shipSize = 5

        if shipSize > 0:
            # Try to fit a ship of size shipSize onto the grid.
            # Add the ship horizontally.
            for x in range(0, self.grid - shipSize + 1):
                for y in range(0, self.grid):
                    self.applyMask()
                    for ship in range(x, x+shipSize):
                        self.line[y] |= 2 ** ship
                    if self.isPartialSolution(shipSize):
                        if shipSize == 5:
                            newGame = copy.deepcopy(self)
                            for i in range(0, self.grid):
                                newGame.mask[i] = newGame.line[i]
                            newGame.guessLargeShips()
                        else:
                            # self.write()
                            self.launch()

            # Add the ship vertically.
            for x in range(0, self.grid):
                for y in range(0, self.grid - shipSize + 1):
                    self.applyMask()
                    for ship in range(y, y+shipSize):
                        self.line[ship] |= 2 ** x
                    if self.isPartialSolution(shipSize):
                        if shipSize == 5:
                            newGame = copy.deepcopy(self)
                            for i in range(0, self.grid):
                                newGame.mask[i] = newGame.line[i]
                            newGame.guessLargeShips()
                        else:
                            # self.write()
                            self.launch()

    def launch(self):
        ''' Launch a command line to solve the specified position. '''
        start = 0
        amount = 100.0 / self.numThreads
        indent = 0
        command = ['./logic_battleships.py', '--game', '{}'.format(self.gameNumber) , '--keep', '--threads', '{}'.format(self.numThreads), '--mask']
        for x in range(0, len(self.line)):
            command.append('{}'.format(self.line[x]))
        print(command)
        subprocess.call(command)




def write(sText : str):
    ''' write the text to the output without a linefeed. '''
    print(sText, end='')
    oFile = open('results.txt', 'a')
    oFile.write(sText)
    oFile.close()



def writeLine(sText: str):
    ''' write the text to the output and add a linefeed. '''
    print(sText)
    oFile = open('results.txt', 'a')
    oFile.write(sText)
    oFile.write("\n")
    oFile.close()



def displayLine(numPositions, line):
    ''' Function to display a horizontal line in a Battleship problem '''
    mask = 1
    for pos in range(0, numPositions):
        if line & mask == mask:
            write(u"\u2588")
        else:
            write(u"\u00B7")
        mask *= 2



def countSolids(line):
    ''' Returns the number of solids in the specified line position. '''
    binaryLine = '{0:b}'.format(line)
    count = 0
    for pos in range (0, len(binaryLine)):
        if binaryLine[pos] == '1':
            count += 1
    return count



def getLongestShip(line):
    ''' Returns the size of the longest ship on the line. '''
    binaryLine = '{0:b}'.format(line)
    maximumShip = 0
    current = 0
    for pos in range (0, len(binaryLine)):
        if binaryLine[pos] == '1':
            current += 1
            if current > maximumShip:
                maximumShip = current
        else:
            current = 0
    return maximumShip



def countShipsOnLine(line, ships):
    ''' Counts the number and size of ships on the line. '''
    binaryLine = '{0:b}'.format(line)
    current = 0
    for pos in range (0, len(binaryLine)):
        if binaryLine[pos] == '1':
            current += 1
        else:
            if current > 1:
                ships[current] += 1
            current = 0
    if current > 1:
        ships[current] += 1
    return True







def isAnyThreadRunning(threads):
    ''' Returns True if any of the specified threads are running. '''
    isRunning = False
    for thread in threads:
        if thread.poll() is None:
            isRunning = True
    return isRunning



def getPossibleLines(numPositions, numSolid, maxShip, mask, negativeMask):
    ''' Returns the set of possible lines that have the specified number of solid positions. '''
    # print('getPossibleLines({}, {}, {}, {}, {})'.format(numPositions, numSolid, maxShip, mask, negativeMask))
    listResult = []
    maximumLines = (2 ** numPositions) - 1
    for pos in range(0, maximumLines):
        if countSolids(pos) == numSolid:
            if pos & mask == mask:
                if (~pos) & negativeMask == negativeMask:
                    if getLongestShip(pos) <= maxShip:
                        listResult.append(pos)
    return listResult
