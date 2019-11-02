#!/usr/bin/env pypy3
"""
FlexAEADv1.py - this class is used to define the FlexAEADv1 cipher
Usage:
  import FlexAEADv1
Options:
  no options
"""
__author__      = 'Eduardo Marsola do Nascimento'
__copyright__   = 'Copyright 2018-11-25'
__credits__     = ''
__license__     = 'MIT'
__version__     = '0.01'
__maintainer__  = ''
__email__       = ''
__status__      = 'Development'

from FlexAESBox import FlexAESBox
import math

def byteToHex(data):
    """
    byteToHex - convert a byte array into a comma sepparated hex representation
    Args:
        data: the byte array to be converted
    Returns:
        returns comma separated hex representation.
    """
    result = '0x{:02X}'.format(data[0])
    for ch in data[1:]:
        result += ',0x{:02X}'.format(ch)
    return result

class FlexAEADv1:
    dirSBox = [ FlexAESBox.dirSBox0 ]
    invSBox = [ FlexAESBox.invSBox0 ]
    nSBoxes = len( dirSBox )
    
    def __init__(self, key = bytes(16), nBytes = 8, nRounds = 0):
        self.nBytes   = nBytes
        self.counter  = bytes([0] * self.nBytes)
        self.checksum = bytes([0] * self.nBytes)

        t0 = bytes([0] * int(len(key)/2))
        t1 = b''
        ### init nRounds for the subkey generation
        self.nRounds = int(math.log(len(t0),2)+2)
        while(len(t1)<(nBytes*8)):
            t0 = self.dirPFK( t0, key)
            t0 = self.dirPFK( t0, key)
            t0 = self.dirPFK( t0, key)
            t1 += t0
        self.key0 = t1[nBytes*0:nBytes*2]
        self.key1 = t1[nBytes*2:nBytes*4]
        self.key2 = t1[nBytes*4:nBytes*6]
        self.key3 = t1[nBytes*6:nBytes*8]

        if(nRounds==0):
            self.nRounds = int(math.log(nBytes,2)+2)
        else:
            self.nRounds = nRounds
        
        ### Debug - comment next line
        """
        print(' ### FlexAEADv1 - init ### - Debug Start')
        print(' self.nRounds : ',self.nRounds)
        print('    self.key0 : '+byteToHex(self.key0))
        print('    self.key1 : '+byteToHex(self.key1))
        print('    self.key2 : '+byteToHex(self.key2))
        print('    self.key3 : '+byteToHex(self.key3))
        print('self.checksum : '+byteToHex(self.checksum))
        print(' self.counter : '+byteToHex(self.counter))
        print(' ### FlexAEADv1 - init ### - Debug End')
        #"""
        
    def encryptMessage( self, nonce, AD, message ):
        self.counter = FlexAEADv1.inc32(self.dirPFK( nonce, self.key3))
        self.checksum = bytes([0]*self.nBytes)
        ### Debug - comment next line
        """
        print(' ### FlexAEADv1 - encryptmessage ### - Debug Start')
        print('self.checksum : '+byteToHex(self.checksum))
        print(' self.counter : '+byteToHex(self.counter))
        print('           s0 : '+byteToHex(self.dirPFK( self.counter, self.key3)))
        print(' ### FlexAEADv1 - encryptmessage ### - Debug End')
        #"""
        ### Encrypt the Associate Data just to calculate the tag
        AD += bytes([0] * (len(AD)%self.nBytes))
        i = 0
        while( i < len(AD)):
            self.encryptBlock(AD[i:i+self.nBytes],isAD=True)
            i += self.nBytes
        ### Encrypt the PlainText
        state = b''
        while( len(state)+self.nBytes < len(message)):
            state += self.encryptBlock(message[len(state):len(state)+self.nBytes])
        lastblock, tag = self.encryptBlock(message[len(state):], final = True)
        return state+lastblock, tag

    def decryptMessage( self, nonce, AD, message, tag ):
        self.counter = FlexAEADv1.inc32(self.dirPFK( nonce, self.key3))
        self.checksum = bytes([0]*self.nBytes)
        ### Debug - comment next line
        """
        print(' ### FlexAEADv1 - decryptmessage ### - Debug Start')
        print('self.checksum : '+byteToHex(self.checksum))
        print(' self.counter : '+byteToHex(self.counter))
        print('           s0 : '+byteToHex(self.dirPFK( self.counter, self.key2)))
        print(' ### FlexAEADv1 - decryptmessage ### - Debug End')
        #"""
        ### Encrypt the Associate Data just to calculate the tag
        AD += bytes([0] * (len(AD)%self.nBytes))
        i = 0
        while( i < len(AD)):
            self.encryptBlock(AD[i:i+self.nBytes],isAD=True)
            i += self.nBytes
        ### Encrypt the PlainText
        state = b''
        while( len(state)+self.nBytes < len(message)):
            state += self.decryptBlock(message[len(state):len(state)+self.nBytes],None)
        lastblock, validmessage = self.decryptBlock(message[len(state):], tag, final = True)
        if( validmessage ):
            return state+lastblock, validmessage
        else:
            return b'', validmessage

    def encryptBlock( self, block, final=False, isAD=False ):
        if( final ):
            paddingXOR = bytes([0xAA] * self.nBytes)
            if( len(block)<self.nBytes ):
                block += b'\x80'
                block += bytes(self.nBytes-len(block))
                paddingXOR = bytes([0x55] * self.nBytes)
        sn = self.dirPFK( self.counter, self.key3)
        state = bytes([ int(a)^int(b) for a,b in zip(sn,block) ])
        state = self.dirPFK( state, self.key2)
        self.checksum = bytes([ int(a)^int(b) for a,b in zip(self.checksum,state) ])
        ### Debug - comment next line
        """
        print(' ### FlexAEADv1 - encryptblock ### - Debug Start')
        print(' self.counter : '+byteToHex(self.counter))
        print('           sn : '+byteToHex(sn))
        print('        block : '+byteToHex(block))
        print('     checksum : '+byteToHex(self.checksum))
        print(' ### FlexAEADv1 - encryptblock ### - Debug End')
        #"""
        ### Just encrypt the first part if it is the associate data
        if( isAD ):
            self.counter = FlexAEADv1.inc32(self.counter)
            return
        state = self.dirPFK( state, self.key1)
        state = bytes([ int(a)^int(b) for a,b in zip(sn,state) ])
        ### Added on algoritm v1
        state = self.dirPFK( state, self.key0)
        if( final ):
            #print('   paddingXOR : '+byteToHex(paddingXOR))
            tag = bytes([ int(a)^int(b) for a,b in zip(self.checksum,paddingXOR) ])
            tag = self.dirPFK( tag, self.key0)
            return state,tag
        else:
            self.counter = FlexAEADv1.inc32(self.counter)
        return state
        
    def decryptBlock( self, block, tag, final=False ):
        sn = self.dirPFK( self.counter, self.key3)
        ### Added on algoritm v1
        state = self.invPFK( block, self.key0)
        state = bytes([ int(a)^int(b) for a,b in zip(sn,state) ])
        state = self.invPFK( state, self.key1)
        self.checksum = bytes([ int(a)^int(b) for a,b in zip(self.checksum,state) ])
        state = self.invPFK( state, self.key2)
        state = bytes([ int(a)^int(b) for a,b in zip(sn,state) ])
        ### Debug - comment next line
        """
        print(' ### FlexAEADv1 - decryptblock ### - Debug Start')
        print('           sn : '+byteToHex(sn))
        print('     checksum : '+byteToHex(self.checksum))
        print(' ### FlexAEADv1 - decryptblock ### - Debug End')
        #"""
        if( final ):
            #print('          tag : '+byteToHex(tag))
            check1 = bytes([ int(a)^0xAA for a in self.checksum ])
            check1 = self.dirPFK( check1, self.key0)
            #print('       check1 : '+byteToHex(check1))
            if( tag == check1[:len(tag)]):
                return state, True
            check2 = bytes([ int(a)^0x55 for a in self.checksum ])
            check2 = self.dirPFK( check2, self.key0)
            #print('       check2 : '+byteToHex(check2))
            if( tag == check2[:len(tag)]):
                i=self.nBytes-1
                ### Debug - comment next line
                """
                print('        state : '+byteToHex(state))
                print('            i : ',i)
                print('     state[i] : ',state[i])
                #"""
                while( (int(state[i])==0) and (i>0) ):
                    i -= 1
                if( (int(state[i])==0x80) and (i>0)):
                    return state[:i], True
                ### Debug - comment next line
                """
                print('            i : ',i)
                print('     state[i] : ',state[i])
                print('        state : '+byteToHex(state))
                #"""
            return b'', False
        else:
            self.counter = FlexAEADv1.inc32(self.counter)
        return state

    def inc32( block, inc=1 ):
        state = b''
        for i in range(0,len(block),4):
            state += ((int.from_bytes(block[i:(i+4)],'big')+inc).to_bytes(4,'big'))
        return state

    def shuffleLayer( block ):
        zero = 0
        half = int(len(block)/2)
        state = [0]*len(block)
        for i in range(half):
            state[(2*i)+0] =  (int(block[i+zero])&0xF0) + \
                             ((int(block[i+half])&0xF0)>>4)
            state[(2*i)+1] = ((int(block[i+zero])&0x0F)<<4)+\
                             (int(block[i+half])&0x0F)
        return bytes(state)

    def invshuffleLayer( block ):
        zero = 0
        half = int(len(block)/2)
        state = [0]*len(block)
        for i in range(half):
            state[i+zero] =  (int(block[(2*i)+0])&0xF0) + \
                            ((int(block[(2*i)+1])&0xF0)>>4)
            state[i+half] =  (int(block[(2*i)+1])&0x0F) + \
                            ((int(block[(2*i)+0])&0x0F)<<4)
        return bytes(state)

    def dirSBoxLayer( block ):
        state = [0]*len(block)
        for i in range(len(block)):
            state[i] = FlexAEADv1.dirSBox[i%FlexAEADv1.nSBoxes][int(block[i])]
        return bytes(state)

    def invSBoxLayer( block ):
        state = [0]*len(block)
        for i in range(len(block)):
            state[i] = FlexAEADv1.invSBox[i%FlexAEADv1.nSBoxes][int(block[i])]
        return bytes(state)

    def dirPFK( self, plaintext, key_pfk):
        if len(plaintext)*2 != len(key_pfk):
            print('wrong block({})/key({}) size on dirPFK'.format(len(plaintext),len(key_pfk)))
            return plaintext
        
        half = int(len(plaintext)/2)
        ciphertext = bytes([int(a)^int(b) for a,b in zip(plaintext,key_pfk)])
        
        for i in range(self.nRounds):
            ### Shuffle Layer
            ciphertext = FlexAEADv1.shuffleLayer(ciphertext)
            left  = ciphertext[:half]
            right = ciphertext[half:]
            ### SBox Layer (right)
            right = FlexAEADv1.dirSBoxLayer(right)
            #### XOR L + R -> L
            left = bytes([int(a)^int(b) for a,b in zip(left,right)])
            ### SBox Layer (left)
            left = FlexAEADv1.dirSBoxLayer(left)
            #### XOR L + R -> R
            right = bytes([int(a)^int(b) for a,b in zip(left,right)])
            ### SBox Layer (right)
            right = FlexAEADv1.dirSBoxLayer(right)
            ### ciphertext = left+right
            ciphertext = left+right
            
        ciphertext = bytes([int(a)^int(b) for a,b in zip(ciphertext,key_pfk[len(ciphertext):])])

        return ciphertext

    def invPFK( self, ciphertext, key_pfk):
        if len(ciphertext)*2 != len(key_pfk):
            print('wrong block({})/key({}) size on dirPFK'.format(len(ciphertext),len(key_pfk)))
            return ciphertext
        
        half = int(len(ciphertext)/2)
        plaintext = bytes([int(a)^int(b) for a,b in zip(ciphertext,key_pfk[len(ciphertext):])])
        
        for i in range(self.nRounds):
            ### ciphertext = left+right
            left  = plaintext[:half]
            right = plaintext[half:]
            ### SBox Layer (right)
            right = FlexAEADv1.invSBoxLayer(right)
            #### XOR L + R -> R
            right = bytes([int(a)^int(b) for a,b in zip(left,right)])
            ### SBox Layer (left)
            left = FlexAEADv1.invSBoxLayer(left)
            #### XOR L + R -> L
            left = bytes([int(a)^int(b) for a,b in zip(left,right)])
            ### SBox Layer (right)
            right = FlexAEADv1.invSBoxLayer(right)
            ### Shuffle Layer
            plaintext = left + right
            plaintext = FlexAEADv1.invshuffleLayer(plaintext)
            
        plaintext = bytes([int(a)^int(b) for a,b in zip(plaintext,key_pfk)])

        return plaintext

        
def __templatefunc( input1, input2, input3):
    """
    __templatefunc - this function ....
    Args:
        input1: first arg ....
        input2: second arg ....
        input3: third arg ....
    Returns:
        the function result.
    """
    pass
    return

if __name__ == "__main__":
    import sys
    # track execution time
    from datetime import datetime
    startTime=datetime.now()
    #
    print(sys.version)
    """
    your code
    """
    # track execution time
    finishTime=datetime.now()
    print( '\nStart: {}, Finish:{}, Running Time: {}'
           ''.format(startTime.replace(microsecond=0),
                     finishTime.replace(microsecond=0),
                     finishTime-startTime))
    ################### END #################
