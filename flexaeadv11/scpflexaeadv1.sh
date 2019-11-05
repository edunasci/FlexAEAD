#/bin/bash

rm -rf crypto_aead

mkdir crypto_aead
mkdir crypto_aead/flexaead128b064v11
mkdir crypto_aead/flexaead128b064v11/ref
mkdir crypto_aead/flexaead128b064v11/opt1
mkdir crypto_aead/flexaead128b128v11
mkdir crypto_aead/flexaead128b128v11/ref
mkdir crypto_aead/flexaead128b128v11/opt1
mkdir crypto_aead/flexaead256b128v11
mkdir crypto_aead/flexaead256b128v11/ref
mkdir crypto_aead/flexaead256b128v11/opt1
mkdir crypto_aead/flexaead256b256v11
mkdir crypto_aead/flexaead256b256v11/ref
mkdir crypto_aead/flexaead256b256v11/opt1

####

scp ref/designers crypto_aead/flexaead128b064v11
scp ref/designers crypto_aead/flexaead128b128v11
scp ref/designers crypto_aead/flexaead256b128v11
scp ref/designers crypto_aead/flexaead256b256v11

scp ref/TestVectorGen/LWC_AEAD_KAT_128_64.txt crypto_aead/flexaead128b064v11
scp ref/TestVectorGen/LWC_AEAD_KAT_128_128.txt crypto_aead/flexaead128b128v11
scp ref/TestVectorGen/LWC_AEAD_KAT_256_128.txt crypto_aead/flexaead256b128v11
scp ref/TestVectorGen/LWC_AEAD_KAT_256_256.txt crypto_aead/flexaead256b256v11

scp ref/implementors crypto_aead/flexaead128b064v11/ref
scp ref/implementors crypto_aead/flexaead128b128v11/ref
scp ref/implementors crypto_aead/flexaead256b128v11/ref
scp ref/implementors crypto_aead/flexaead256b256v11/ref

scp ref/h/api-128-64.h crypto_aead/flexaead128b064v11/ref/api.h
scp ref/h/api-128-128.h crypto_aead/flexaead128b128v11/ref/api.h
scp ref/h/api-256-128.h crypto_aead/flexaead256b128v11/ref/api.h
scp ref/h/api-256-256.h crypto_aead/flexaead256b256v11/ref/api.h

scp ref/h/encrypt-128-64.h crypto_aead/flexaead128b064v11/ref/encrypt.h
scp ref/h/encrypt-128-128.h crypto_aead/flexaead128b128v11/ref/encrypt.h
scp ref/h/encrypt-256-128.h crypto_aead/flexaead256b128v11/ref/encrypt.h
scp ref/h/encrypt-256-256.h crypto_aead/flexaead256b256v11/ref/encrypt.h

scp ref/FlexAEADv1.1.c crypto_aead/flexaead128b064v11/ref/encrypt.c
scp ref/FlexAEADv1.1.c crypto_aead/flexaead128b128v11/ref/encrypt.c
scp ref/FlexAEADv1.1.c crypto_aead/flexaead256b128v11/ref/encrypt.c
scp ref/FlexAEADv1.1.c crypto_aead/flexaead256b256v11/ref/encrypt.c

scp opt1/implementors crypto_aead/flexaead128b064v11/opt1
scp opt1/implementors crypto_aead/flexaead128b128v11/opt1
scp opt1/implementors crypto_aead/flexaead256b128v11/opt1
scp opt1/implementors crypto_aead/flexaead256b256v11/opt1

scp opt1/h/encrypt-128-64.h crypto_aead/flexaead128b064v11/opt1/encrypt.h
scp opt1/h/encrypt-128-128.h crypto_aead/flexaead128b128v11/opt1/encrypt.h
scp opt1/h/encrypt-256-128.h crypto_aead/flexaead256b128v11/opt1/encrypt.h
scp opt1/h/encrypt-256-256.h crypto_aead/flexaead256b256v11/opt1/encrypt.h

scp opt1/h/api-128-64.h crypto_aead/flexaead128b064v11/opt1/api.h
scp opt1/h/api-128-128.h crypto_aead/flexaead128b128v11/opt1/api.h
scp opt1/h/api-256-128.h crypto_aead/flexaead256b128v11/opt1/api.h
scp opt1/h/api-256-256.h crypto_aead/flexaead256b256v11/opt1/api.h

scp opt1/FlexAEADv1.1.c crypto_aead/flexaead128b064v11/opt1/encrypt.c
scp opt1/FlexAEADv1.1.c crypto_aead/flexaead128b128v11/opt1/encrypt.c
scp opt1/FlexAEADv1.1.c crypto_aead/flexaead256b128v11/opt1/encrypt.c
scp opt1/FlexAEADv1.1.c crypto_aead/flexaead256b256v11/opt1/encrypt.c

###
### rm -rf crypto_aead/flexaead256b128v11 crypto_aead/flexaead128b064v11/opt1 crypto_aead/flexaead128b128v11/opt1 crypto_aead/flexaead256b256v11/opt1
###

rm -f crypto_aead.tar.gz
tar -czvf crypto_aead.tar.gz crypto_aead
