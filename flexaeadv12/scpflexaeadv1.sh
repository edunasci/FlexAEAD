#/bin/bash

rm -rf crypto_aead

mkdir crypto_aead
mkdir crypto_aead/flexaead128b064v12
mkdir crypto_aead/flexaead128b064v12/ref
mkdir crypto_aead/flexaead128b064v12/opt1
mkdir crypto_aead/flexaead128b128v12
mkdir crypto_aead/flexaead128b128v12/ref
mkdir crypto_aead/flexaead128b128v12/opt1
mkdir crypto_aead/flexaead256b128v12
mkdir crypto_aead/flexaead256b128v12/ref
mkdir crypto_aead/flexaead256b128v12/opt1
mkdir crypto_aead/flexaead256b256v12
mkdir crypto_aead/flexaead256b256v12/ref
mkdir crypto_aead/flexaead256b256v12/opt1

####

scp ref/designers crypto_aead/flexaead128b064v12
scp ref/designers crypto_aead/flexaead128b128v12
scp ref/designers crypto_aead/flexaead256b128v12
scp ref/designers crypto_aead/flexaead256b256v12

scp ref/TestVectorGen/LWC_AEAD_KAT_128_64.txt crypto_aead/flexaead128b064v12
scp ref/TestVectorGen/LWC_AEAD_KAT_128_128.txt crypto_aead/flexaead128b128v12
scp ref/TestVectorGen/LWC_AEAD_KAT_256_128.txt crypto_aead/flexaead256b128v12
scp ref/TestVectorGen/LWC_AEAD_KAT_256_256.txt crypto_aead/flexaead256b256v12

scp ref/implementors crypto_aead/flexaead128b064v12/ref
scp ref/implementors crypto_aead/flexaead128b128v12/ref
scp ref/implementors crypto_aead/flexaead256b128v12/ref
scp ref/implementors crypto_aead/flexaead256b256v12/ref

scp ref/h/api-128-64.h crypto_aead/flexaead128b064v12/ref/api.h
scp ref/h/api-128-128.h crypto_aead/flexaead128b128v12/ref/api.h
scp ref/h/api-256-128.h crypto_aead/flexaead256b128v12/ref/api.h
scp ref/h/api-256-256.h crypto_aead/flexaead256b256v12/ref/api.h

scp ref/h/encrypt-128-64.h crypto_aead/flexaead128b064v12/ref/encrypt.h
scp ref/h/encrypt-128-128.h crypto_aead/flexaead128b128v12/ref/encrypt.h
scp ref/h/encrypt-256-128.h crypto_aead/flexaead256b128v12/ref/encrypt.h
scp ref/h/encrypt-256-256.h crypto_aead/flexaead256b256v12/ref/encrypt.h

scp ref/FlexAEADv1.2.c crypto_aead/flexaead128b064v12/ref/encrypt.c
scp ref/FlexAEADv1.2.c crypto_aead/flexaead128b128v12/ref/encrypt.c
scp ref/FlexAEADv1.2.c crypto_aead/flexaead256b128v12/ref/encrypt.c
scp ref/FlexAEADv1.2.c crypto_aead/flexaead256b256v12/ref/encrypt.c

scp opt1/implementors crypto_aead/flexaead128b064v12/opt1
scp opt1/implementors crypto_aead/flexaead128b128v12/opt1
scp opt1/implementors crypto_aead/flexaead256b128v12/opt1
scp opt1/implementors crypto_aead/flexaead256b256v12/opt1

scp opt1/h/encrypt-128-64.h crypto_aead/flexaead128b064v12/opt1/encrypt.h
scp opt1/h/encrypt-128-128.h crypto_aead/flexaead128b128v12/opt1/encrypt.h
scp opt1/h/encrypt-256-128.h crypto_aead/flexaead256b128v12/opt1/encrypt.h
scp opt1/h/encrypt-256-256.h crypto_aead/flexaead256b256v12/opt1/encrypt.h

scp opt1/h/api-128-64.h crypto_aead/flexaead128b064v12/opt1/api.h
scp opt1/h/api-128-128.h crypto_aead/flexaead128b128v12/opt1/api.h
scp opt1/h/api-256-128.h crypto_aead/flexaead256b128v12/opt1/api.h
scp opt1/h/api-256-256.h crypto_aead/flexaead256b256v12/opt1/api.h

scp opt1/FlexAEADv1.2.c crypto_aead/flexaead128b064v12/opt1/encrypt.c
scp opt1/FlexAEADv1.2.c crypto_aead/flexaead128b128v12/opt1/encrypt.c
scp opt1/FlexAEADv1.2.c crypto_aead/flexaead256b128v12/opt1/encrypt.c
scp opt1/FlexAEADv1.2.c crypto_aead/flexaead256b256v12/opt1/encrypt.c

###
### rm -rf crypto_aead/flexaead256b128v12 crypto_aead/flexaead128b064v12/opt1 crypto_aead/flexaead128b128v12/opt1 crypto_aead/flexaead256b256v12/opt1
###

rm -f crypto_aead_flexaead12.tar.gz
tar -czvf crypto_aead_flexaead12.tar.gz crypto_aead
