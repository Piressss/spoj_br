/*
 * main.cpp
 *
 *  Created on: Jan 15, 2015
 *      Author: fpires
 */

#include<stdio.h>

int main(){

	float A, G, cA, cG;
	float preco, consumo;

	scanf("%f %f %f %f", &A, &G, &cA, &cG);

	//printf("%f %f %f %f", A, G, cA, cG);

	preco=(cA/cG);
    consumo=(A/G);

    if(consumo < preco){
    	printf("\nA\n");
    }
    else{
    	printf("\nG\n");
    }
}


