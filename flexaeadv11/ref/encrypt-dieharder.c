#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "FlexAEADv1.1.c"

int main (  ) {

	unsigned char *npub;
	unsigned char *k;
	unsigned char *state;

	struct FlexAEADv1 flexaeadv1;
			
	k = malloc(KEYSIZE);
	memset( k, 0x00, KEYSIZE);
	
	npub = malloc(BLOCKSIZE);
	memset( npub, 0x00, BLOCKSIZE);

	FlexAEADv1_init( &flexaeadv1, k );

	fprintf(stderr, "FlexAEADv1 ZERO %d %d\n", BLOCKSIZE*8, KEYSIZE*8 );
		

	// ### reset the counter and checksum	
	memcpy( flexaeadv1.counter, npub, NONCESIZE);
	dirPFK( flexaeadv1.counter, flexaeadv1.nBytes, (flexaeadv1.subkeys + (4*flexaeadv1.nBytes)),  flexaeadv1.nRounds, flexaeadv1.state );

	state = malloc(BLOCKSIZE);
	while(1)
	{
		memset( state, 0x00, BLOCKSIZE );
		inc32( flexaeadv1.counter, flexaeadv1.nBytes, 0x11111111 );
		encryptBlock( &flexaeadv1, state);
		fwrite(state, 1, flexaeadv1.nBytes, stdout);
	}
	
	free(state);
}
