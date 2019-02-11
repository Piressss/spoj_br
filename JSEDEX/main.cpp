/*
 * main.cpp
 *
 *  Created on: Dec 18, 2014
 *      Author: fpires
 */

#include<stdio.h>

int main(){

	int x, A, L, P;

	scanf("%d", &x);
	scanf("%d %d %d", &A, &L, &P);

	if(x<=A && x<=L && x<=P){
		printf("S\n");
	}
	else{
		printf("N\n");
	}

}


