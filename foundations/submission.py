import collections
import math

############################################################
# Problem 3a

def findAlphabeticallyLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return max(sorted(text.split()))
    # END_YOUR_CODE

############################################################
# Problem 3b

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    # d = sqrt[(x2-x1)**2+(y2,y1)**2]
    return math.sqrt(math.pow(loc1[0]-loc2[0],2) + math.pow(loc1[1]-loc2[1],2))
    # END_YOUR_CODE

############################################################
# Problem 3c

def mutateSentences(sentence):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the orignal sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """
    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    l = sentence.split()
    if len(l) == 1:
        return sentence
    else:
        ret = set()
        d = {x: set() for x in l}

        for i in range(len(l)-1):
                d[l[i]].add(l[i+1])
        if d[l[-1]] == set():
            del d[l[-1]]
        print(d)

        def nextWord(k, d):
            p = d[k].pop()
            d[k].add(p)
            return p

        # construct new sentences
        for k,v in d.items():
            # new sentence needs to be the same len
            curr = k
            s = curr
            for i in range(len(l)-1):
                s += ' '
                n = nextWord(curr, d)
                while n not in d:
                    n = nextWord(curr,d)
                s += n
                curr = n
            ret.add(s)
        return ret
    # END_YOUR_CODE

############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    sum = 0.0
    for k in v1:
        sum += v1[k] * v2[k]
    return sum
    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    # Needs simplification
    for k in v1:
        v1[k] += scale * v2[k]

    for v in v2:
        if v not in v1:
            v1[v] += scale * v2[v]

    return v1
    # END_YOUR_CODE

############################################################
# Problem 3f

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    d = collections.defaultdict(int)
    for i in text.split():
        d[i]+=1
    return {x for x in d if d[x]==1}
    # END_YOUR_CODE

############################################################
# Problem 3g

def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (our solution is 19 lines of code, but don't worry if you deviate from this)

    # Pali chars
    c = []
    def findPali(text):
        if len(text) == 1 or len(text) == 0:
            return len(text)
        # if len(text) == 0:
            # return 0
        elif text.find(text[0],1) > -1:
            c.append(text[0])
            return 1 + findPali(text[1:])
        # elif len(c) > 0 and text[0] == c[-1]:
            # c.remove(c[-1])
            # return 1 + findPali(text[1:])
        # if the next char is the current opening
        elif text[1] in c:
            return 1 + findPali(text[1:])
        else:
            return findPali(text[1:])

    return findPali(text)
    # END_YOUR_CODE
