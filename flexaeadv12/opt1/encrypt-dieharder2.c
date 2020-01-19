#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "FlexAEADv1.2.c"
#include "crypto_uint32.h"
#include "crypto_uint64.h"


int main (  ) {
	unsigned char *state,*inc;

	fprintf(stderr, "encrypt-dieharder2 %d %d\n", BLOCKSIZE*8, KEYSIZE*8 );
	state = malloc(BLOCKSIZE);
	inc = malloc(BLOCKSIZE);
    for( int i=0;i<BLOCKSIZE;i++)
    {
        *(state+i) = (unsigned char) (rand()&0xFF);
        *(inc+i) = 0x00;
    }
	while(1)
	{
        // for( unsigned long long  i = 0; i < BLOCKSIZE; i += 4)
        //     cmwc( state+i, inc+i);
        mwc32(state,inc,BLOCKSIZE);
        fwrite(state, 1, BLOCKSIZE, stdout);
	}
	free(state);
    free(inc);
}
