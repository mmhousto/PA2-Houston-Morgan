# cspExamples.py - Example CSPs
# AIFCA Python3 code Version 0.8.2 Documentation at http://aipython.org

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

from cspProblem import CSP, Constraint        
from operator import lt,ne,eq,gt

def ne_(val):
    """not equal value"""
    # nev = lambda x: x != val   # alternative definition
    # nev = partial(neq,val)     # another alternative definition
    def nev(x):
        return val != x
    nev.__name__ = str(val)+"!="      # name of the function 
    return nev

def is_(val):
    """is a value"""
    # isv = lambda x: x == val   # alternative definition
    # isv = partial(eq,val)      # another alternative definition
    def isv(x):
        return val == x
    isv.__name__ = str(val)+"=="
    return isv

csp0 = CSP({'X':{1,2,3}, 'Y':{1,2,3}, 'Z':{1,2,3}},
           [ Constraint(('X','Y'),lt),
             Constraint(('Y','Z'),lt)])

C0 = Constraint(('A','B'), lt, "A < B")
C1 = Constraint(('B',), ne_(2), "B != 2")
C2 = Constraint(('B','C'), lt, "B < C")
csp1 = CSP({'A':{1,2,3,4}, 'B':{1,2,3,4}, 'C':{1,2,3,4}},
           [C0, C1, C2],
           positions={"A": (1, 0),
                      "B": (3, 0),
                      "C": (5, 0),
                      "A < B": (2, 1),
                      "B < C": (4, 1),
                      "B != 2": (3, 2)})

csp2 = CSP({'A':{1,2,3,4}, 'B':{1,2,3,4}, 'C':{1,2,3,4}, 
            'D':{1,2,3,4}, 'E':{1,2,3,4}},
           [ Constraint(('B',), ne_(3), "B != 3"),
            Constraint(('C',), ne_(2), "C != 2"),
            Constraint(('A','B'), ne, "A != B"),
            Constraint(('B','C'), ne, "A != C"),
            Constraint(('C','D'), lt, "C < D"),
            Constraint(('A','D'), eq, "A = D"),
            Constraint(('A','E'), gt, "A > E"),
            Constraint(('B','E'), gt, "B > E"),
            Constraint(('C','E'), gt, "C > E"),
            Constraint(('D','E'), gt, "D > E"),
            Constraint(('B','D'), ne, "B != D")])

csp3 = CSP({'A':{1,2,3,4}, 'B':{1,2,3,4}, 'C':{1,2,3,4}, 
            'D':{1,2,3,4}, 'E':{1,2,3,4}},
           [Constraint(('A','B'), ne, "A != B"),
            Constraint(('A','D'), lt, "A < D"),
            Constraint(('A','E'), lambda a,e: (a-e)%2 == 1, "A-E is odd"), # A-E is odd
            Constraint(('B','E'), lt, "B < E"),
            Constraint(('D','C'), lt, "D < C"),
            Constraint(('C','E'), ne, "C != E"),
            Constraint(('D','E'), ne, "D != E")])

def adjacent(x,y):
   """True when x and y are adjacent numbers"""
   return abs(x-y) == 1

csp4 = CSP({'A':{1,2,3,4,5}, 'B':{1,2,3,4,5}, 'C':{1,2,3,4,5}, 
            'D':{1,2,3,4,5}, 'E':{1,2,3,4,5}},
           [Constraint(('A','B'), adjacent, "adjacent(A,B)"),
            Constraint(('B','C'), adjacent, "adjacent(B,C)"),
            Constraint(('C','D'), adjacent, "adjacent(C,D)"),
            Constraint(('D','E'), adjacent, "adjacent(D,E)"),
            Constraint(('A','C'), ne, "A != C"),
            Constraint(('B','D'), ne, "A != D"),
            Constraint(('C','E'), ne, "C != E")])

def meet_at(p1,p2):
    """returns a function of two words that is true when the words intersect at postions p1, p2.
    The positions are relative to the words; starting at position 0.
    meet_at(p1,p2)(w1,w2) is true if the same letter is at position p1 of word w1 
         and at position p2 of word w2.
    """
    def meets(w1,w2):
        return w1[p1] == w2[p2]
    meets.__name__ = "meet_at("+str(p1)+','+str(p2)+')'
    return meets

crossword1 = CSP({'one_across':{'ant', 'big', 'bus', 'car', 'has'},
                  'one_down':{'book', 'buys', 'hold', 'lane', 'year'},
                  'two_down':{'ginger', 'search', 'symbol', 'syntax'},
                  'three_across':{'book', 'buys', 'hold', 'land', 'year'},
                  'four_across':{'ant', 'big', 'bus', 'car', 'has'}},
                  [Constraint(('one_across','one_down'), meet_at(0,0)),
                   Constraint(('one_across','two_down'), meet_at(2,0)),
                   Constraint(('three_across','two_down'), meet_at(2,2)),
                   Constraint(('three_across','one_down'), meet_at(0,2)),
                   Constraint(('four_across','two_down'), meet_at(0,4))])

words = {'at', 'eta', 'be', 'hat', 'he', 'her', 'it', 'him', 'on', 'one', 'desk', 'dance', 'usage',
 'easy', 'dove', 'first', 'else', 'loses', 'fuels', 'help', 'haste', 'given', 'kind', 'sense', 'soon', 'sound', 'this', 'think'}
           
def is_word(*letters, words=words):
    """is true if the letters concatenated form a word in words"""
    return "".join(letters) in words

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
  "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
  "z"]

crossword1d = CSP({'p00':letters, 'p10':letters, 'p20':letters, # first row
                   'p01':letters, 'p21':letters,  # second row
                   'p02':letters, 'p12':letters, 'p22':letters, 'p32':letters, # third row
                   'p03':letters, 'p23':letters, #fourth row
                   'p24':letters, 'p34':letters, 'p44':letters, # fifth row
                   'p25':letters # sixth row
                   },
                  [Constraint(('p00', 'p10', 'p20'), is_word), #1-across
                   Constraint(('p00', 'p01', 'p02', 'p03'), is_word), # 1-down
                   Constraint(('p02', 'p12', 'p22', 'p32'), is_word), # 3-across
                   Constraint(('p20', 'p21', 'p22', 'p23', 'p24', 'p25'), is_word), # 2-down
                   Constraint(('p24', 'p34', 'p44'), is_word) # 4-across
                   ])

#THIS IS FOR PA2 Excercise 3(b)
crossword1b = CSP({'p10':letters, 'p20':letters, 'p30':letters, 'p40':letters, # first row
                   'p11':letters, 'p21':letters,  # second row
                   'p02':letters, 'p12':letters, 'p22':letters, 'p32':letters, 'p42':letters, # third row
                   'p13':letters, 'p33':letters, #fourth row
                   'p14':letters, 'p24':letters, 'p34':letters, 'p44':letters, # fifth row
                   'p35':letters, # sixth row
                   'p36':letters # seventh row
                   },
                  [Constraint(('p10', 'p20', 'p30', 'p40'), is_word), #1-across
                   Constraint(('p10', 'p11', 'p12', 'p13', 'p14'), is_word), # 1-down
                   Constraint(('p11', 'p21'), is_word), # 3-across
                   Constraint(('p20', 'p21', 'p22'), is_word), # 2-down
                   Constraint(('p02', 'p12', 'p22', 'p32', 'p42'), is_word), # 4-across
                   Constraint(('p32', 'p33', 'p34', 'p35', 'p36'), is_word), # 5-down
                   Constraint(('p14', 'p24', 'p34', 'p44'), is_word) # 6-across
                   ])
               
               #Tests csp with solutions I have found and AI searched for
def test(CSP_solver, csp=crossword1b,
             solutions=[{'p10': "s", 'p20': "o", 'p30': "o", 'p40': "n", #1-across
                   'p10': "s", 'p11': "o", 'p12': "u", 'p13': "n", 'p14': "d", # 1-down
                   'p11': "o", 'p21': "n", # 3-across
                   'p20': "o", 'p21': "n", 'p22': "e", # 2-down
                   'p02': "f", 'p12': "u", 'p22': "e", 'p32': "l", 'p42': "s", # 4-across
                   'p32': "l", 'p33': "o", 'p34': "s", 'p35': "e", 'p36': "s", # 5-down
                   'p14': "d", 'p24': "e", 'p34': "s", 'p44': "k"}, # 6-across
                   {'p10': 't', 'p20': 'h', 'p30': 'i', 'p40': 's',
                    'p11': 'h', 'p21': 'e', 'p02': 'f', 'p12': 'i',
                     'p22': 'r', 'p32': 's', 'p42': 't', 'p13': 'n',
                      'p33': 'e', 'p14': 'k', 'p24': 'i', 'p34': 'n',
                       'p44': 'd', 'p35': 's', 'p36': 'e'}]):
    """CSP_solver is a solver that takes a csp and returns a solution
    csp is a constraint satisfaction problem
    solutions is the list of all solutions to csp
    This tests whether the solution returned by CSP_solver is a solution.
    """
    print("Testing csp with",CSP_solver.__doc__)
    sol0 = CSP_solver(csp)
    print("Solution found:",sol0)
    assert sol0 in solutions, "Solution not correct for "+str(csp)
    print("Passed unit test")

