#!/usr/bin/env pypy3
"""
genLinearTable.py - Generate the Linear Expression Approximations for the FlexAESBoxes
Usage:
  genLinearTable.py
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

def parityOf( n ):
    """
    parityOf - determine if the number of bits is odd or even
    Args:
        n: the number to be tested.
    Returns:
        o - if the number has even bits.
        1 - if the number has odd  bits.
    """
    parity = 0
    while( n ):
        parity ^= (n&1)
        n >>= 1
    return parity
    
    

def genSBoxLinearTable( SBox ):
    """
    genSBoxLinearTable - generate the linear distribution table for a SBox
    Args:
        SBox: the SBox that will be used to generate the difference distribution table.
    Returns:
        the linear expression aproximation table.
    """
    lenSBox = len(SBox)
    linTable= [[int(-lenSBox/2)] * lenSBox for i in range(lenSBox)]
    parityAX = [0]*lenSBox
    parityBY = [0]*lenSBox
    for x in range(lenSBox):
        y = SBox[x]
        for a in range(lenSBox):
            ax = a&x
            parityAX[a]=parityOf(ax)
        for b in range(lenSBox):
            by = b&y
            parityBY[b] = parityOf(by)
        for a in range(lenSBox):
            for b in range(lenSBox):
                linTable[a][b] += (parityAX[a]==parityBY[b])
        #if((x%16)==0 ):
        #    print( 'x = 0x{:02X}'.format(x))
    return linTable


def printLinearTable( linTable, printFullTable = True ):
    """
    printLinearTable - prints the linear expression aproximation table
    Args:
        linTable: The linear approximation table to be printed.
        printFullTable:
            True => print full table.
            False => print only expresions bias summary.
    Returns:
        none
    """
    nExpBias = [0] * 2 * len(SBox)
    maxBias = minBias = 0
    s = 'a,minBias,maxBias'
    for i in range(len(SBox)):
        s += ',x{:02X}'.format(i)
    if( printFullTable ):
        print(s)
    for a in range(1,len(SBox)):
        maxBias = max(linTable[a][:])
        minBias = min(linTable[a][:])
        s = 'x{:02X} , {:+f}({:+d})'.format(a,minBias/len(SBox),minBias)
        s += ' , {:+f}({:+d})'.format(maxBias/len(SBox),maxBias)
        for b in range(1,len(SBox)):
            nExpBias[ linTable[a][b]+len(SBox) ] += 1
            s += ' , {:+d}'.format(linTable[a][b])
        if( printFullTable ):
            print(s)
    print('')
    print('Bias, Number of Expressions')
    for i in range( 2*len(SBox) ):
        if( nExpBias[i] != 0):
            s = '{:+d}/{:d} , {:d}'.format(i-len(SBox),len(SBox),nExpBias[i])
            print(s)


if __name__ == "__main__":
    from FlexAESBox import FlexAESBox
    # track execution time
    from datetime import datetime
    startTime=datetime.now()
    #
    SBoxDict={
        'dirSBox0': FlexAESBox.dirSBox0,
        'invSBox0': FlexAESBox.invSBox0,
        'dirSBox1': FlexAESBox.dirSBox1,
        'invSBox1': FlexAESBox.invSBox1,
        'dirSBox2': FlexAESBox.dirSBox2,
        'invSBox2': FlexAESBox.invSBox2,
        'dirTweakSBox0': FlexAESBox.dirTweakSBox0,
        'invTweakSBox0': FlexAESBox.invTweakSBox0,
        }
    linTableDict = {}
    for name, SBox in SBoxDict.items():
        print('')
        print('Linear Approximation Table for {}'.format(name))
        linTableDict[ name ] = genSBoxLinearTable(SBox)
        printLinearTable( linTableDict[ name ] )
    
    # track execution time
    finishTime=datetime.now()
    print( '\nStart: {}, Finish:{}, Running Time: {}'
           ''.format(startTime.replace(microsecond=0),
                     finishTime.replace(microsecond=0),
                     finishTime-startTime))
    ################### END #################

