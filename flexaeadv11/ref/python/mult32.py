#!/usr/bin/env python3

from FlexAEADv11SBox import FlexAEADv11SBox
from FlexAEADv11 import FlexAEADv11
#import numpy as np
#import matplotlib.pyplot as plt
import math

def multiGF32( input1, input2, modP32):
    """
    multiGF32 - multiply 2 number on a Galois Field defined by a polynomial.
    Args:
        input1: first number to multiply.
        input2: second number to multiply.
        modP32: polynomial defining the Galos Field.
    Returns:
        the multiplication result.
    """
    state1 = 0x0
    for i in range(32):
        if input2&0x1:
            state1 ^= input1
        input1 <<= 1
        input2 >>= 1
        if input1&0x1_00_00_00_00:
            input1 ^= modP32
    return state1


def invMultiGF32( input1, modP32):
    """
    invMultiGF32 - calculate the inverse multiplicative of a number
                    on a Galois Field defined by a polynomial.
    Args:
        input1: number to find the inverse multiplicative.
        modP32: polynomial defining the Galos Field.
    Returns:
        the inverse multiplicative.
    """
    invmulti=1
    while invmulti<0x1_00_00_00_00:
        state1=multiGF32(invmulti,input1,modP32);
        if state1==1:
            return invmulti
        invmulti = invmulti + 1
    return invmulti


def dirMixQuartersLayer( a1 ):
    quarter = int(len(a1)/4)
    state = np.zeros(np.shape(a1),dtype=int)
    for i in range(quarter):
        state[(0*quarter)+i] = a1[(1*quarter)+i]+a1[(2*quarter)+i]+a1[(3*quarter)+i]
        state[(1*quarter)+i] = a1[(0*quarter)+i]+a1[(2*quarter)+i]+a1[(3*quarter)+i]
        state[(2*quarter)+i] = a1[(0*quarter)+i]+a1[(1*quarter)+i]+a1[(3*quarter)+i]
        state[(3*quarter)+i] = a1[(0*quarter)+i]+a1[(1*quarter)+i]+a1[(2*quarter)+i]
    return state

if __name__ == "__main__":
    import sys
    import random
    import time
    # track execution time
    from datetime import datetime
    startTime=datetime.now()
    #
    # IP x^32+X^7+X^5+X^3+X^2+X^1+X^0 (753210) 
    IP = 0b1_0000_0000_0000_0000_0000_0000_1010_1111
    #plt.ion()
    for i in [8, 16, 32]:
        print( '' )
        print( '' )
        print( '#### {} bits block ####'.format(8*i) )
        print( '#### validate functions ####' )
        block=b''
        for n in range(i):
           block += bytes([random.randint(0,256)])
        #block=bytes([*range(i)])
        print( '              block -> ' + block.hex())
        block = FlexAEADv11.dirShuffleLayer(block)
        print( '    dirShuffleLayer -> ' + block.hex())
        block = FlexAEADv11.invShuffleLayer(block)
        print( '    invShuffleLayer -> ' + block.hex())
        block = FlexAEADv11.dirMixQuartersLayer(block)
        print( 'dirMixQuartersLayer -> ' + block.hex())
        block = FlexAEADv11.dirMixQuartersLayer(block)
        print( 'invMixQuartersLayer -> ' + block.hex())
        print( '#### permutation function effect ####' )
        print( '              block -> ' + block.hex())
        for n in range(int(math.log(i,2))):
        #for n in range(i):
            block = FlexAEADv11.dirShuffleLayer(block)
            print( '    dirShuffleLayer -> ' + block.hex())
            block = FlexAEADv11.dirMixQuartersLayer(block)
            print( 'dirMixQuartersLayer -> ' + block.hex())
            block = FlexAEADv11.dirSBoxLayer(block)
            print( '       dirSBoxLayer -> ' + block.hex())
        #time.sleep(2)
        for n in range(30):
            state = b''
            for i2 in range(0,i,4):
                """
                x = block[i2:i2+4]
                print( '                    x -> {}'.format(x.hex()) )
                x = int.from_bytes(block[i2:i2+4], "little")
                print( '               int(x) -> {:x}'.format(x) )
                x = multiGF32( x, 2, IP)
                print( ' multiGF32( x, 2, IP) -> {:x}'.format(x) )
                x = x.to_bytes(4, byteorder='little')
                print( '              x.hex() -> {}'.format(x) )
                state += x
                """
                state += multiGF32(int.from_bytes(block[i2:i2+4], "little"),2,IP).to_bytes(4, byteorder='little')
            block = state
            print( '          multiGF32 -> ' + block.hex())
        
    # track execution time
    finishTime=datetime.now()
    print( '\nStart: {}, Finish:{}, Running Time: {}'
           ''.format(startTime.replace(microsecond=0),
                     finishTime.replace(microsecond=0),
                     finishTime-startTime))
    ################### END #################
