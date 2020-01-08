# FlexAEAD
A flexible authenticated cipher family.

## flexaeadv1
This folder contains the v1 definition and implementation source files. This version was submited to NIST LWC contest. 

## flexaeadv11
This folder contains the v1.1 definition and implementation source files. This version correct the weakness detected on the cipher during Round 1 of NIST LWC Contest.

## flexaeadv12
This folder contains the v1.2 definition and implementation source files. This version improves the cipher performance by using a multiply with carry pseudorandom generator to replace the counter based on the internal permutation function. This version is arround two times faster than the former. Comparing the optimized version against the most performatic implementation of each cipher family competing on 2nd round of NIST LWC competition (32 families in total), it is on 7th position.  
