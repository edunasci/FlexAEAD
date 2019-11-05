#!/usr/bin/env python3
"""
genDifDistTable.py - Generate the difference distribution tables
                for the FlexAEADv11SBoxes
Usage:
  genDifDistTable.py
Options:
  no options
"""
__author__      = 'Eduardo Marsola do Nascimento'
__copyright__   = 'Copyright 2019-10-27'
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
    print('Difference Distribution Table for {}'.format(name))
    for deltaX, row in enumerate(difTable):
        s = '{}'.format(deltaX)
        for n in row:
            s += ',{}'.format(n)
        print(s)


if __name__ == "__main__":
    from FlexAEADv11SBox import FlexAEADv11SBox
    # track execution time
    from datetime import datetime
    startTime=datetime.now()
    #
    SBoxDict={
        'dirSBox0': FlexAEADv11SBox.dirSBox0,
        'invSBox0': FlexAEADv11SBox.invSBox0,
        'dirSBox1': FlexAEADv11SBox.dirSBox1,
        'invSBox1': FlexAEADv11SBox.invSBox1,
        'dirSBox2': FlexAEADv11SBox.dirSBox2,
        'invSBox2': FlexAEADv11SBox.invSBox2,
        'dirSBox3': FlexAEADv11SBox.dirSBox3,
        'invSBox3': FlexAEADv11SBox.invSBox3,
        }
    difTableDict = {}
    for name, SBox in SBoxDict.items():
        print('')
        print('')
        print('SBox -> {}'.format(name))
        difTableDict[ name ] = genSBoxDifDistTable( SBox )
        printDifTable( difTableDict[ name ] )
    
    # track execution time
    finishTime=datetime.now()
    print( '\nStart: {}, Finish:{}, Running Time: {}'
           ''.format(startTime.replace(microsecond=0),
                     finishTime.replace(microsecond=0),
                     finishTime-startTime))
    ################### END #################
    
