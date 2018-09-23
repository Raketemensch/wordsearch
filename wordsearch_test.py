#!/usr/bin/env python
import unittest
from word_search import generateList
from word_search import generateBoard


class generateListTest(unittest.TestCase):
    def test(self):
        # Verify that def returns a list
        wordFile = ['some', 'words', 'for', 'testing']
        wordList = generateList(wordFile)
        self.assertIsInstance(wordList, list)


class generateBoardTest(unittest.TestCase):
    def test(self):
        # Verify that def returns rows/columns of the correct size
        x = 15
        y = 15
        wordSearch = generateBoard(x, y)
        # Verify that def returns rows of the correct size
        self.assertTrue(x, len(wordSearch))
        # Verify that def returns columns of the correct size
        self.assertTrue(x, len(wordSearch[0]))


if __name__ == '__main__':
    unittest.main()
