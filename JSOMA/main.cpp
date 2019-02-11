/*
 * main.cpp
 *
 *  Created on: Dec 18, 2014
 *      Author: fpires
 */

#include<stdio.h>

int main(){

	int n, x, t=0, i;

	scanf("%d", &n);

	for(i=0; i<n; i++){
		scanf("%d", &x);
		t=t+x;
	}
	printf("%d \n", t);
}



