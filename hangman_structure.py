"""
File for hangman structure
"""


def parts(x):
    """
    This fuction prints out a hangman when enters the wrong input.
    After every wrong/incorrect input the hangman will displayed
    """
    if x == 0:
        print('   ',   '------')
        print('   ',   '|    |')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('------------')
    if x == 1:
        print('   ',   '------')
        print('   ',   '|    |')
        print('   ',   '|    o')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('------------')
    if x == 2:
        print('   ',   '------')
        print('   ',   '|    |')
        print('   ',   '|    o')
        print('   ',   '|   -|-')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('------------')
    if x == 3:
        print('   ',   '------')
        print('   ',   '|    |')
        print('   ',   '|    o')
        print('   ',   '|   -|-')
        print('   ',   '|    | ')
        print('   ',   '|     ')
        print('------------')
    if x == 4:
        print('   ',   '------')
        print('   ',   '|    |')
        print('   ',   '|    o')
        print('   ',   '|   -|-')
        print('   ',   '|    | ')
        print('   ',   '|   / \\')
        print('------------')
