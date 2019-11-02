#!/usr/bin/env pypy3
"""
genDifDistTable.py - Generate the difference distribution tables
                for the FlexAESBoxes
Usage:
  genDifDistTable.py
Options:
  no options
"""
__author__      = 'Eduardo Marsola do Nascimento'
__copyright__   = 'Copyright 2018-11-18'
__credits__     = ''
__license__     = 'MIT'
__version__     = '0.01'
__maintainer__  = ''
__email__       = ''
__status__      = 'Development'


def genSBoxDifDistTable( SBox ):
    """
    genSBoxDifDistTable - generate the difference distribution table for a SBox
    Args:
        SBox: the SBox that will be used to generate the difference distribution table.
    Returns:
        the difference distribution table for the SBox.
    """
    deltaX = deltaY = 0;
    difTable= [[0] * len(SBox) for i in range(len(SBox))]
    for X0 in range(len(SBox)):
        for X1 in range(len(SBox)):
            deltaX = X0^X1
            deltaY = SBox[X0]^SBox[X1]
            difTable[deltaX][deltaY] += 1
    return difTable

def printDifTable( difTable ):
    """
    printLinearTable - prints the linear expression aproximation table
    Args:
        difTable: The difference distribution tableto be printed.
        printFullTable:
            True => print full table.
    Returns:
        none
    """
    print('')
    print('Difference Distribution Table for {}'.format(name))
    for deltaX, row in enumerate(difTable):
        s = '{}'.format(deltaX)
        for n in row:
            s += ',{}'.format(n)
        print(s)


if __name__ == "__main__":
    from FlexAESBox import FlexAESBox
    # track execution time
    from datetime import datetime
    startTime=datetime.now()
    #
    SBoxDict={
        'dirSBox0': FlexAESBox.dirSBox0,
        }
    difTableDict = {}
    for name, SBox in SBoxDict.items():
        print('')
        print('Linear Approximation Table for {}'.format(name))
        difTableDict[ name ] = genSBoxDifDistTable( SBox )
        printDifTable( difTableDict[ name ] )
    
    # track execution time
    finishTime=datetime.now()
    print( '\nStart: {}, Finish:{}, Running Time: {}'
           ''.format(startTime.replace(microsecond=0),
                     finishTime.replace(microsecond=0),
                     finishTime-startTime))
    ################### END #################
    
