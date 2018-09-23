#!/usr/bin/env python
# This code will:
#   Generate a board of random letters.
#   Identify all valid words (contained in the attached word list)
#       in the board.
#   Display results to the user.

import random
import argparse
import os
import sys


def main():
    """
    Load the passed-in word list
    Generate a 15x15 grid of random letters
    Search that grid for words in the word list
    """
    wordFile = parseArgs
    print('Generating word list from file...')
    wordList = generateList(wordFile)
    print('Generating board...')
    # Generate a list of x rows, of y columns
    wordSearch = generateBoard(15, 15)
    print('Checking for words...')
    foundWords = searchForWords(wordList, wordSearch)
    print('The following words were found:')
    for word in foundWords:
        print(word)


def parseArgs():
    """
    Make sure that we received a valid file name.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Please pass in a text file of words')
    args = parser.parse_args()

    wordFile = args.filename

    # If the file doesn't exist, exit and tell user
    if not os.path.exists(wordFile):
        print('The file ' + wordFile + ' cannot be found.')
        sys.exit()

    return wordFile


def generateList(wordFile):
    """
    Open a list of words and put them in a list.
    """
    wordFile = open('words.txt', 'r')
    wordList = []
    for line in wordFile:
        wordList.append(line.rstrip())
    wordFile.close()
    return wordList


def generateBoard(x, y):
    """
    Generate a grid of letters, sizes x by y.
    """
    wordSearch = []
    letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for row in range(x):
        column = []
        for col in range(y):
            column.append(random.choice(letterList))
        wordSearch.append(column)

    return wordSearch


def searchForWords(wordList, wordSearch):
    """
    Search through the grid for words in the list,
    horizontally, then vertically, then diagonally.
    """
    # Generate a word list to avoid duplicates
    foundWords = []

    # Search horizontally
    for row in wordSearch:
        rowString = ''.join(row)
        for word in wordList:
            if word in rowString:
                if word not in foundWords:
                    foundWords.append(word)

    # Search Vertically
    # THIS DOES NOT WORK CURRENTLY
    colList = []
    columnLetters = []
    for row in wordSearch:
        for i in range(0, len(row)):
            columnLetters.append(row[i])
            i = i + 1
        colList.append(columnLetters)

    # Search diagonally
    return foundWords


if __name__ == '__main__':
    # unittest.main()
    main()
