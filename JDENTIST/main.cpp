/*
 * main.cpp
 *
 *  Created on: Dec 18, 2014
 *      Author: fpires
 */

#include<stdio.h>
#include<stdlib.h>


#define loc 1000000

typedef int (*compfn)(const void*, const void*);

typedef struct {
	int X, Y;
}hora;

int compare (hora * a, hora * b)
{
	if ( a->Y <  b->Y ) return -1;
	if ( a->Y == b->Y ) return 0;
	if ( a->Y >  b->Y ) return 1;
}

int main(){

	int N, Xt=0, Yt=0, i, conf=0;
	int XY[loc][2];

	hora *h;

	scanf("%d", &N);

	h= (hora*) malloc(N*sizeof(hora));

	for(i=0; i<N; i++){
		scanf("%d %d", &h->X, &h->Y);
	}

	qsort(h, N, sizeof(hora), (compfn)compare);

	for(i=0; i<N; i++){
		printf("%d \n", h[i]);
	}

	free (h);

		/*if(X<Yt){
			conf++;
		}
		else{
			Xt=X; Yt=Y;
		}*/

	//printf("%d \n", N-conf);
}


