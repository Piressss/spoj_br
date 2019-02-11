/*
 * main.cpp
 *
 *  Created on: Dec 18, 2014
 *      Author: fpires
 */

#include<stdio.h>

int main(){

	int nband, nlata, ncopo, tcopo=0, i;

	scanf("%d", &nband);

	for(i=0; i<nband; i++){
		scanf("%d %d", &nlata, &ncopo);
		if((nlata-ncopo)>0){
			tcopo=tcopo+ncopo;
		}
	}
	printf("%d \n", tcopo);
}


