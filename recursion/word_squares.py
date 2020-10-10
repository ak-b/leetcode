'''
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Algorithm: Backtracking
Given a list of words, we are asked to find a combination of words upon with we could construct a word square. 
The backbone of the algorithm to solve the above problem could be surprisingly simple.
The idea is that we construct the word square row by row from top to down. At each row, we simply do trial and error, i.e. we try with one word, 
if it does not meet the constraint then we try another one.
As one might notice, the above idea of the algorithm is actually known as backtracking, which is often associated with recursion and DFS (Depth-First Search) as well.
'''
#Approach 1: Backtracking with HashTable
'''
Intuition

As one might notice in the above backtracking algorithm, the bottleneck lies in the function getWordsWithPrefix() which is to
find all words with the given prefix. At each invocation of the function, we were iterating through the entire input list of words, which is of linear time complexity O(N).
One of the ideas to optimize the getWordsWithPrefix() function would be to process the words beforehand and to build a data structure that could speed up the lookup procedure later.
As one might recall, one of the data structures that provide a fast lookup operation is called hashtable or dictionary. We could simply build a hashtable with all 
possible prefixes as keys and the words that are associated with the prefix as the values in the table. Later, given the prefix, we should be able to list all the words with the given prefix in constant time \mathcal{O}(1)O(1).

Algorithm

We build upon the backtracking algorithm that we listed above, and tweak two parts.
In the first part, we add a new function buildPrefixHashTable(words) to build a hashtable out of the input words.
Then in the second part, in the function getWordsWithPrefix() we simply query the hashtable to retrieve all the words that possess the given prefix.
'''
class Solution:

    def wordSquares(self, words: List[str]) -> List[List[str]]:

        self.words = words
        self.N = len(words[0])
        self.buildPrefixHashTable(self.words)

        results = []
        word_squares = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def buildPrefixHashTable(self, words):
        self.prefixHashTable = {}
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                self.prefixHashTable.setdefault(prefix, set()).add(word)

    def getWordsWithPrefix(self, prefix):
        if prefix in self.prefixHashTable:
            return self.prefixHashTable[prefix]
        else:
            return set([])
          
#Approach 2: Backtracking with Trie
'''
Intuition
Speaking about prefix, there is another data structure called Trie (also known as prefix tree), which could find its use in this problem.
In the above approach, we have reduce the time complexity of retrieving a list of words with a given prefix from the linear O(N) to the constant time O(1). 
In exchange, we have to spend some extra space to store all the prefixes of each words.
The Trie data structure provides a compact and yet still fast way to retrieve words with a given prefix.
'''
class Solution:

    def wordSquares(self, words: List[str]) -> List[List[str]]:

        self.words = words
        self.N = len(words[0])
        self.buildTrie(self.words)

        results = []
        word_squares = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def buildTrie(self, words):
        self.trie = {}

        for wordIndex, word in enumerate(words):
            node = self.trie
            for char in word:
                if char in node:
                    node = node[char]
                else:
                    newNode = {}
                    newNode['#'] = []
                    node[char] = newNode
                    node = newNode
                node['#'].append(wordIndex)

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return [self.words[wordIndex] for wordIndex in node['#']]
