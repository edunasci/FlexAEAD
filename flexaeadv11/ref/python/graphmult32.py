#!/usr/bin/env python3

from FlexAEADv11SBox import FlexAEADv11SBox
from FlexAEADv11 import FlexAEADv11
import numpy as np
import matplotlib.pyplot as plt
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
    a1=np.zeros((100,100))
    x = 1
    for i in range(100):
        for j in range(25):
            x = multiGF32( x, 2, IP)
            print( 'x -> {:x}'.format(x) )
            a1[i][j*4+0] = (x//0x1)&0xFF
            a1[i][j*4+1] = (x//0x1_00)&0xFF
            a1[i][j*4+2] = (x//0x1_00_00)&0xFF
            a1[i][j*4+3] = (x//0x1_00_00_00)&0xFF
    imgplot = plt.imshow(a1)
    plt.show()
    
    # track execution time
    finishTime=datetime.now()
    print( '\nStart: {}, Finish:{}, Running Time: {}'
           ''.format(startTime.replace(microsecond=0),
                     finishTime.replace(microsecond=0),
                     finishTime-startTime))
    ################### END #################
