#!/usr/bin/env pypy3
"""
__FlexAEADv1printTestVectors.py - generate the Test Vectors for FlexAEADv1
Usage:
  __FlexAEADv1printTestVectors.py
Options:
  no options
"""
__author__      = 'Eduardo Marsola do Nascimento'
__copyright__   = 'Copyright 2018-11-21'
__credits__     = ''
__license__     = 'MIT'
__version__     = '0.01'
__maintainer__  = ''
__email__       = ''
__status__      = 'Development'

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


def printTestVectors(key,blocksize=64,rounds=5):
    """
    printTestVectors - print the test vectors for the FlexAEADv1 algorithm
    Args:
        key: the key to be used to generate the test vectors
        blocksize: the blocksize to be used to generate the test vectors
        rounds: the number of rounds to be used to generate the test vectors
    Returns:
        returns nothing.
    """
    from FlexAEADv1 import FlexAEADv1
    #byte [] ciphertext, plaintext,key0,key1,key2,nonce,ctr,t0,t1,s0;
    nBytes = int(blocksize/8)
    print('\n\n')
    print('*****************************************************************')
    print('Block Size: {} / Key Size: {} / Rounds: {}'.format( blocksize,
          len(key)*8, rounds ) )
    print('*****************************************************************')
    t0 = bytes(nBytes)
    plaintext = bytes(nBytes)
    ciphertext = bytes(nBytes)
    nonce = bytes(nBytes)
    checksum = bytes(nBytes)
    ad = bytes(nBytes)
    
    flexaeadv1=FlexAEADv1(key, nBytes, rounds)
    
    '''
    print('Key  : '+byteToHex(key))
    
        
    ##init key0
    t0 = flexaeadv1.dirPFK( t0, key)
    t0 = flexaeadv1.dirPFK( t0, key)
    t0 = flexaeadv1.dirPFK( t0, key)
    key0 = t0
    t0 = flexaeadv1.dirPFK( t0, key)
    t0 = flexaeadv1.dirPFK( t0, key)
    t0 = flexaeadv1.dirPFK( t0, key)
    key0 = key0 + t0
    print('Key0 : '+byteToHex(key0))
    
    ##init key1
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    key1 = t0
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    key1 = key1 + t0
    print('key1 : '+byteToHex(key1))
    
    #init key2
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    key2 = t0
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    key2 = key2 + t0
    print('Key2 : '+byteToHex(key2))

    #init key3
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    key3 = t0
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    t0 = flexaeadv1.dirPFK( t0, key);
    key3 = key3 + t0
    print('Key3 : '+byteToHex(key3))

    #init ctr
    ctr = flexaeadv1.dirPFK( nonce, key3)
    print('ctr        : '+byteToHex(ctr))
    ctr = FlexAEADv1.inc32(ctr)
    print('inc32(ctr) : '+byteToHex(ctr))
    s0  = flexaeadv1.dirPFK( ctr, key2)
    print('S0         : '+byteToHex(s0))
    ciphertext = bytes([ int(a)^int(b) for a,b in zip(s0,ad) ])
    ciphertext = flexaeadv1.dirPFK( ciphertext, key1)
    checksum = ciphertext
    print('checksum   : '+byteToHex(checksum))
    ctr = FlexAEADv1.inc32(ctr)
    print('inc32(ctr) : '+byteToHex(ctr))
    s0  = flexaeadv1.dirPFK( ctr, key2)
    print('S0         : '+byteToHex(s0))


    print('')
    print('Key        : '+byteToHex(key))
    print('plaintext  : '+byteToHex(plaintext))
    ciphertext = bytes([ int(a)^int(b) for a,b in zip(s0,plaintext) ])
    ciphertext = flexaeadv1.dirPFK( ciphertext, key1)
    checksum = bytes([ int(a)^int(b) for a,b in zip(ciphertext,checksum) ])
    checksum = bytes([ int(a)^0xAA for a in checksum ])
    tag = flexaeadv1.dirPFK( checksum, key0)
    ciphertext = flexaeadv1.dirPFK( ciphertext, key0)
    ciphertext = bytes([ int(a)^int(b) for a,b in zip(s0,ciphertext) ])
    print('ciphertext : '+byteToHex(ciphertext))
    print('tag        : '+byteToHex(tag))    
    ciphertext = bytes([ int(a)^int(b) for a,b in zip(s0,ciphertext) ])
    ciphertext = flexaeadv1.invPFK( ciphertext, key0)
    ciphertext = flexaeadv1.invPFK( ciphertext, key1)
    plaintext = bytes([ int(a)^int(b) for a,b in zip(ciphertext,s0) ])
    print('plaintext  : '+byteToHex(plaintext))
    print('')
    '''
    print('##### Using cipher')
    print('Key        : '+byteToHex(key))
    print('ad         : '+byteToHex(ad))
    print('nonce      : '+byteToHex(nonce))
    print('plaintext  : '+byteToHex(plaintext))
    print('# Encrypting...')
    flexaeadv1=FlexAEADv1(key, nBytes, rounds)
    ciphertext, tag = flexaeadv1.encryptMessage( nonce, ad, plaintext )
    print('ciphertext : '+byteToHex(ciphertext))
    print('tag        : '+byteToHex(tag))
    print('# Decrypting...')
    plaintext, validmessage = flexaeadv1.decryptMessage( nonce, ad, ciphertext, tag )
    print('validmessage : ', validmessage )
    if( validmessage ):
        print('plaintext  : '+byteToHex(plaintext))
    print('##### Using cipher (padded)')
    print('# Encrypting...')
    plaintext += b'\x01\x02\x03\x04'
    print('plaintext  : '+byteToHex(plaintext))
    print('len(plaintext) : ',len(plaintext))
    flexaeadv1=FlexAEADv1(key, nBytes, rounds)
    ciphertext, tag = flexaeadv1.encryptMessage( nonce, ad, plaintext )
    print('ciphertext : '+byteToHex(ciphertext))
    print('len(ciphertext) : ',len(ciphertext))
    print('tag        : '+byteToHex(tag))
    print('# Decrypting...')
    plaintext, validmessage = flexaeadv1.decryptMessage( nonce, ad, ciphertext, tag )
    print('validmessage : ', validmessage )
    if( validmessage ):
        print('plaintext  : '+byteToHex(plaintext))
        print('len(plaintext) : ',len(plaintext))
    print('# Decrypting (bad nonce)...')
    badnonce=b'\x01'+nonce[1:]
    plaintext, validmessage = flexaeadv1.decryptMessage( badnonce, ad, ciphertext, tag )
    print('validmessage : ', validmessage )
    if( validmessage ):
        print('plaintext  : '+byteToHex(plaintext))
        print('len(plaintext) : ',len(plaintext))
    print('# Decrypting (bad tag)...')
    badtag = b'\x01'+tag[1:]
    plaintext, validmessage = flexaeadv1.decryptMessage( nonce, ad, ciphertext, badtag )
    print('validmessage : ', validmessage )
    if( validmessage ):
        print('plaintext  : '+byteToHex(plaintext))
        print('len(plaintext) : ',len(plaintext))
    print('# Decrypting (bad ciphertext)...')
    badciphertext = b'\x01'+ciphertext[1:]
    plaintext, validmessage = flexaeadv1.decryptMessage( nonce, ad, badciphertext, tag )
    print('validmessage : ', validmessage )
    if( validmessage ):
        print('plaintext  : '+byteToHex(plaintext))
        print('len(plaintext) : ',len(plaintext))
    print('# Decrypting (bad AD)...')
    badad = b'\x01'+ad[1:]
    plaintext, validmessage = flexaeadv1.decryptMessage( nonce, badad, ciphertext, tag )
    print('validmessage : ', validmessage )
    if( validmessage ):
        print('plaintext  : '+byteToHex(plaintext))
        print('len(plaintext) : ',len(plaintext))
    return

if __name__ == "__main__":
    import sys
    # track execution time
    from datetime import datetime
    startTime=datetime.now()
    #
    k1 = bytes([ 0x5E, 0x64, 0x7C, 0x3C, 0xAE, 0x97, 0x2D, 0x13,
                 0x84, 0x28, 0xFC, 0x44, 0x06, 0xC4, 0xEE, 0x1A ])
    k2 = bytes([ 0xB1, 0x69, 0x62, 0x6B, 0x7D, 0x5B, 0x30, 0x96,
                 0x14, 0x08, 0x0A, 0x03, 0x9E, 0x08, 0xA9, 0x90,
                 0xC2, 0x05, 0xF6, 0xBB, 0xA7, 0x4B, 0x8C, 0x84,
                 0x16, 0xB1, 0x52, 0x76, 0x97, 0xDC, 0x53, 0xAA ])
    k3 = bytes([ 0xB5, 0x81, 0x47, 0x03, 0x83, 0x2D, 0x00, 0x10,
                 0xBA, 0xB7, 0x98, 0x66, 0xC3, 0x6C, 0xA5, 0x82,
                 0xFD, 0x6F, 0x1E, 0xC8, 0xFB, 0xCE, 0x74, 0x30,
                 0x3E, 0x89, 0x87, 0xFF, 0x71, 0x34, 0xFB, 0xEE,
                 0xC4, 0x1C, 0xFB, 0x47, 0x32, 0x63, 0x5E, 0x12,
                 0xBF, 0x8D, 0xE3, 0x2F, 0xDD, 0x29, 0x98, 0x7A,
                 0xB4, 0x1A, 0x6C, 0xD1, 0x7D, 0x5A, 0x79, 0xCE,
                 0xB7, 0x19, 0x7E, 0xD7, 0x51, 0x3E, 0xB3, 0x07 ])
    k4 = bytes([ 0x55, 0xCF, 0x18, 0x0A, 0x2E, 0x10, 0x4D, 0x7F,
                 0xA6, 0x74, 0x17, 0xD3, 0x9E, 0xF7, 0xDD, 0x2E,
                 0x47, 0x96, 0xBE, 0x89, 0xB6, 0x2A, 0xF9, 0x7F,
                 0xB7, 0x89, 0xDD, 0x8B, 0xDC, 0x1A, 0xCB, 0x43,
                 0x93, 0xDE, 0x7D, 0xDA, 0x3D, 0x41, 0x5D, 0x1E,
                 0xF9, 0xBE, 0xE7, 0x54, 0x59, 0xDF, 0x45, 0xBE,
                 0x15, 0x05, 0xD0, 0xC4, 0x6E, 0x88, 0x12, 0xB3,
                 0x14, 0xBD, 0xB9, 0x25, 0xDA, 0x9C, 0x8E, 0xE7,
                 0x70, 0x4F, 0x23, 0xEB, 0xA1, 0x5B, 0xD1, 0xDD,
                 0x79, 0x67, 0x10, 0xF6, 0x4E, 0xD6, 0xCE, 0xAC,
                 0x48, 0xC7, 0x86, 0x33, 0x8A, 0xAB, 0x7F, 0xFF,
                 0xAB, 0x7E, 0xFF, 0xA6, 0xED, 0x7C, 0x1C, 0x7D,
                 0x63, 0x4D, 0xCF, 0x8F, 0x69, 0xD4, 0xE9, 0x60,
                 0x52, 0xCA, 0x57, 0xA1, 0xB1, 0x98, 0x2A, 0x30,
                 0x06, 0x1D, 0xC0, 0xC5, 0x94, 0xE2, 0xC1, 0xB4,
                 0xBF, 0xAF, 0x3D, 0x34, 0xC1, 0x56, 0x05, 0x72 ])

    printTestVectors(key=k1,blocksize=64,rounds=5)
    printTestVectors(key=k2,blocksize=128,rounds=6)
    printTestVectors(key=k3,blocksize=256,rounds=7)
    printTestVectors(key=k4,blocksize=512,rounds=8)
    # track execution time
    finishTime=datetime.now()
    print( '\nStart: {}, Finish:{}, Running Time: {}'
           ''.format(startTime.replace(microsecond=0),
                     finishTime.replace(microsecond=0),
                     finishTime-startTime))
    ################### END #################






