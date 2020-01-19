#include <stdio.h> 
#include "crypto_uint8.h"
#include "crypto_uint16.h"
#include "crypto_uint32.h"
#include "crypto_uint64.h"

int main() 
{ 
    printf("crypto_uint8 -> %lu \n",sizeof(crypto_uint8)); 
    printf("crypto_uint16 -> %lu \n",sizeof(crypto_uint16)); 
    printf("crypto_uint32 -> %lu \n",sizeof(crypto_uint32)); 
    printf("crypto_uint64 -> %lu \n",sizeof(crypto_uint64)); 
    
    return 0;
}