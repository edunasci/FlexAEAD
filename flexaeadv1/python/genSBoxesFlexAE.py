#!/usr/bin/env pypy3
"""
genSBoxesFlexAE.py - module to generate FlexAE SBoxes.
Usage:
  genSBoxesFlexAE.py
Options:
  no options
"""
__author__      = 'Eduardo Marsola do Nascimento'
__copyright__   = 'Copyright 2019'
__credits__     = ''
__license__     = 'MIT'
__version__     = '0.01'
__maintainer__  = ''
__email__       = ''
__status__      = 'Development'


def multiGF8( input1, input2, modP8):
    """
    multiGF8 - multiply 2 number on a Galois Field defined by a polynomial.
    Args:
        input1: first number to multiply.
        input2: second number to multiply.
        modP8: polynomial defining the Galos Field.
    Returns:
        the multiplication result.
    """
    state1 = 0x0
    for i in range(8):
        #print( 'i: {:2x}, input1: {:4x}, input2: {:4x}, state1: {:4x}'
        #       ''.format(i,input1,input2,state1))
        if input2&0x1:
            state1 ^= input1
        input2 >>= 1
        input1 <<= 1
        if input1&0x100:
            input1 ^= modP8
    return state1

    
def invMultiGF8( input1, modP8):
    """
    invMultiGF8 - calculate the inverse multiplicative of a number
                    on a Galois Field defined by a polynomial.
    Args:
        input1: number to find the inverse multiplicative.
        modP8: polynomial defining the Galos Field.
    Returns:
        the inverse multiplicative.
    """
    invmulti=1
    while invmulti<0x100:
        state1=multiGF8(invmulti,input1,modP8);
        if state1==1:
            return invmulti
        invmulti = invmulti + 1
    return invmulti

def affTransf( input1, addConst, multConst ):
    """
    affTransf - performs an affine transformation using an additive and
                    an multiplicative constants.
    Args:
        input1: number to transform.
        addConst: the additive constant to be used.
        multConst: the multiplicative constant to be used.
    Returns:
        the transformed number.
    """
    state1 = multiGF8(multConst, input1, 0x101)
    return state1^addConst

    
def genSBox( IP, MC, AC ):
    """
    genSBox - generates a SBox using the same method as proposed on AES
                definition but can use other parameters.
    Args:
        IP: Irreducible Polynomial to define the Galois Field.
        MC: Multiplicative Constant to be used on the affine transformation.
        AC: Additive Constant to be used on the affine transformation.
    Returns:
        a SBox define buy the parameters.
    """
    SBox = [0]*0x100
    SBox[0]=AC
    for i in range(0x1,0x100):
        SBox[i] = invMultiGF8( i, IP)
        SBox[i] = affTransf(SBox[i], AC, MC )
    return SBox

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


def genInvSBox( SBox ):
    """
    genInvSBox - generates inverse of an SBox.
    Args:
        SBox: The SBox to generate the inverse.
    Returns:
        The inverse SBox.
    """
    InvSBox = [0]*0x100
    for i in range(0x100):
        InvSBox[ SBox[i] ] = i
    return InvSBox


def tweakSBox( SBox ):
    """
    tweakSBox - tweak the SBox to make stronger for FlexAE cipher.
    Args:
        SBox: the SBoxto be Tweaked.
    Returns:
        a tweaked SBox.
    """
    TweakSBox = [0]*0x100
    for i in range(0x100):
        left  = (SBox[i] & 0xF0) >> 4 
        right = (SBox[i] & 0x0F)
        TweakSBox[i] =  SBox[i] ^ \
                        ((0x00 if parityOf(left)  else 0x0F) + \
                        (0x00 if parityOf(right) else 0xF0))
    return TweakSBox


def printSBox( name, SBox ):
    """
    printSBox - print the SBox on screen.
    Args:
        name: the SBox name.
        SBox: the SBox to be printed.
    Returns:
        nothing.
    """
    print('    """')
    print('    {}: '.format(name))
    print('      -  0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F')
    for i in range(0x10):
        s='    {:1X} -'.format(i)
        for j in range(0x10):
            s = s + ' {:02X}'.format(SBox[i*0x10+j])
        print(s)
    print('    """')

def printFlexAESBoxClass( SBoxDict ):
    """
    printFlexAESBoxClass - print the FlexAESBox Class Code on screen.
    Args:
        SBox0, SBox1, SBox2: the SBoxes to be used on the class.
    Returns:
        nothing.
    """
    print('class FlexAESBox:')
    for name, SBox in SBoxDict.items():
        printSBox( name, SBox)
        s = '    {} = ['.format(name)
        for i in range(0x100):
            if (i%0x10)==0:
                print(s)
                s='    '
            s = s + '0x{:02X}'.format(SBox[i])+','
        print(s)
        print('    ]')


if __name__ == "__main__":
    """
    generate the FlexAE SBoxes
    """
    # track execution time
    from datetime import datetime
    startTime=datetime.now()
    #
    
    # Create an Empty Dictonary
    SBoxDict={}
    # SBox0
    IP0 = 0b100011011; MC0 = 0x1F; AC0 = 0x63;
    SBox0 = genSBox(IP0,MC0,AC0)
    SBoxDict['dirSBox0' ] = SBox0
    SBoxDict['invSBox0' ] = genInvSBox(SBox0)
    
    # SBox1
    IP1 = 0b100011101; MC1 = 0x1F; AC1 = 0x95;
    SBox1 = genSBox(IP1,MC1,AC1)
    SBoxDict['dirSBox1' ] = SBox1
    SBoxDict['invSBox1' ] = genInvSBox(SBox1)
    
    # SBox2
    IP2 = 0b100101011; MC2 = 0x1F; AC2 = 0xA6;
    SBox2 = genSBox(IP2,MC2,AC2)
    SBoxDict['dirSBox2' ] = SBox2
    SBoxDict['invSBox2' ] = genInvSBox(SBox2)
    
    # SBox2
    IP3 = 0b100101101; MC3 = 0x1F; AC3 = 0xD9;
    SBox3 = genSBox(IP3,MC3,AC3)
    SBoxDict['dirSBox3' ] = SBox3
    SBoxDict['invSBox3' ] = genInvSBox(SBox3)

    #
    # Print the Class FlexAESbox
    #
    printFlexAESBoxClass(SBoxDict)
    
    # track execution time
    finishTime=datetime.now()
    print( '\nStart: {}, Finish:{}, Running Time: {}'
           ''.format(startTime.replace(microsecond=0),
                     finishTime.replace(microsecond=0),
                     finishTime-startTime))
    ################### END #################
    
