#!/usr/bin/env python3

from FlexAEADv11SBox import FlexAEADv11SBox
from FlexAEADv11 import FlexAEADv11
import numpy as np
import matplotlib.pyplot as plt
import math

#"""
def dirShuffleLayer( a1 ):
    half = int(len(a1)/2)
    state = np.zeros(np.shape(a1),dtype=int)
    for i in range(half):
        state[(2*i)+0] =  a1[(half*0)+i]
        state[(2*i)+1] =  a1[(half*1)+i]
    return state
    
def invShuffleLayer( a1 ):
    half = int(len(a1)/2)
    state = np.zeros(np.shape(a1),dtype=int)
    for i in range(half):
        state[(half*0)+i] =  a1[(2*i)+0]
        state[(half*1)+i] =  a1[(2*i)+1]
    return a1
#"""
"""
def dirShuffleLayer( a1 ):
    quarter = int(len(a1)/4)
    state = np.zeros(np.shape(a1),dtype=int)
    for i in range(quarter):
        state[(4*i)+0] =  a1[(quarter*0)+i]
        state[(4*i)+1] =  a1[(quarter*1)+i]
        state[(4*i)+2] =  a1[(quarter*2)+i]
        state[(4*i)+3] =  a1[(quarter*3)+i]
    return state
    
def invShuffleLayer( a1 ):
    quarter = int(len(a1)/4)
    state = np.zeros(np.shape(a1),dtype=int)
    for i in range(quarter):
        state[(quarter*0)+i] =  a1[(4*i)+0]
        state[(quarter*1)+i] =  a1[(4*i)+1]
        state[(quarter*2)+i] =  a1[(4*i)+2]
        state[(quarter*3)+i] =  a1[(4*i)+3]
    return a1
"""
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
    np.set_printoptions(threshold=1024)
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
        a1 = np.identity(i,dtype=int)
        print( '           block -> ' + block.hex())
        print( '              a1 -> ')
        print(a1)
        block = FlexAEADv11.dirShuffleLayer(block)
        print( ' dirShuffleLayer -> ' + block.hex())
        block = FlexAEADv11.invShuffleLayer(block)
        print( ' invShuffleLayer -> ' + block.hex())
        block = FlexAEADv11.dirMixQuartersLayer(block)
        print( 'dirMixQuartersLayer -> ' + block.hex())
        block = FlexAEADv11.dirMixQuartersLayer(block)
        print( 'invMixQuartersLayer -> ' + block.hex())
        print( '#### permutation function effect ####' )
        print( '           block -> ' + block.hex())
        for n in range(int(math.log(i,2))+1):
        #for n in range(i):
            block = FlexAEADv11.dirShuffleLayer(block)
            a1 = dirShuffleLayer(a1)
            print( ' dirShuffleLayer -> ' + block.hex())
            block = FlexAEADv11.dirMixQuartersLayer(block)
            a1 = dirMixQuartersLayer(a1)
            print( 'dirMixQuartersLayer -> ' + block.hex())
            block = FlexAEADv11.dirSBoxLayer(block)
            print( '    dirSBoxLayer -> ' + block.hex())
            print( '              a1 -> ')
            print(a1)
            print( '    np.max(a1) -> {}'.format(np.max(a1)))
            print( '    np.min(a1) -> {}'.format(np.min(a1)))
            print( '           dif -> {}'.format(np.max(a1)-np.min(a1)))
            print( '           n+1 -> {}'.format(n+1))
            #imgplot = plt.imshow(a1)
            #plt.show()
            #time.sleep(2)
        #print( '#### result  ####' )
        #print( '           block -> ' + block.hex())
        #print( '              a1 -> ')
        #print(a1)
        imgplot = plt.imshow(a1)
        plt.show()
        #time.sleep(2)

        
    # track execution time
    finishTime=datetime.now()
    print( '\nStart: {}, Finish:{}, Running Time: {}'
           ''.format(startTime.replace(microsecond=0),
                     finishTime.replace(microsecond=0),
                     finishTime-startTime))
    ################### END #################
    
