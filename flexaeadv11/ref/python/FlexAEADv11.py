#!/usr/bin/env python3
"""
FlexAEADv11.py - this class is used to define the FlexAEADv11 cipher
Usage:
  import FlexAEADv11
Options:
  no options
"""
__author__      = 'Eduardo Marsola do Nascimento'
__copyright__   = 'Copyright 2019-10-20'
__credits__     = ''
__license__     = 'MIT'
__version__     = '0.01'
__maintainer__  = ''
__email__       = ''
__status__      = 'Development'

from FlexAEADv11SBox import FlexAEADv11SBox
import math

class FlexAEADv11:
    def dirShuffleLayer( block ):
        half = int(len(block)/2)
        state = [0]*len(block)
        for i in range(half):
            state[(2*i)+0] =  block[(half*0)+i]
            state[(2*i)+1] =  block[(half*1)+i]
        return bytes(state)
        
    def invShuffleLayer( block ):
        half = int(len(block)/2)
        state = [0]*len(block)
        for i in range(half):
            state[(half*0)+i] =  block[(2*i)+0]
            state[(half*1)+i] =  block[(2*i)+1]
        return bytes(state)
        
    def dirMixQuartersLayer( block ):
        quarter = int(len(block)/4)
        A = block[0*quarter:1*quarter]
        B = block[1*quarter:2*quarter]
        C = block[2*quarter:3*quarter]
        D = block[3*quarter:4*quarter]
        state = bytes([int(a)^int(b) for a,b in zip(A,B)])
        state = bytes([int(a)^int(b) for a,b in zip(state,C)])
        state = bytes([int(a)^int(b) for a,b in zip(state,D)])
        A = bytes([int(a)^int(b) for a,b in zip(state,A)])
        B = bytes([int(a)^int(b) for a,b in zip(state,B)])
        C = bytes([int(a)^int(b) for a,b in zip(state,C)])
        D = bytes([int(a)^int(b) for a,b in zip(state,D)])
        return A+B+C+D
        
    def dirSBoxLayer( block ):
        state = [0]*len(block)
        quarter = int(len(block)/4)
        for i in range(0*quarter,2*quarter):
            state[i] = FlexAEADv11SBox.dirSBox0[int(block[i])]
        for i in range(1*quarter,2*quarter):
            state[i] = FlexAEADv11SBox.dirSBox1[int(block[i])]
        for i in range(2*quarter,3*quarter):
            state[i] = FlexAEADv11SBox.dirSBox2[int(block[i])]
        for i in range(3*quarter,4*quarter):
            state[i] = FlexAEADv11SBox.dirSBox3[int(block[i])]
        return bytes(state)
        
    def invSBoxLayer( block ):
        state = [0]*len(block)
        quarter = int(len(block)/4)
        for i in range(0*quarter,2*quarter):
            state[i] = FlexAEADv11SBox.invSBox0[int(block[i])]
        for i in range(1*quarter,2*quarter):
            state[i] = FlexAEADv11SBox.invSBox1[int(block[i])]
        for i in range(2*quarter,3*quarter):
            state[i] = FlexAEADv11SBox.invSBox2[int(block[i])]
        for i in range(3*quarter,4*quarter):
            state[i] = FlexAEADv11SBox.invBox3[int(block[i])]
        return bytes(state)
