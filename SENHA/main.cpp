/*
 * main.cpp
 *
 *  Created on: Jan 14, 2015
 *      Author: fpires
 */

#include<stdio.h>

int main(){

	int N, i, j, k;
	int teste=0, sel=0;
	int dig[10];
	char C[6];
	int senha_tmp[9][12];
	int senha[6];
	int senha_final[10][6];

	scanf("%d", &N);

	while(N != 0){

	for(i=0; i<N; i++){

		scanf("%d %d %d %d %d %d %d %d %d %d %c %c %c %c %c %c",
		&dig[0], &dig[1], &dig[2], &dig[3], &dig[4], &dig[5], &dig[6], &dig[7], &dig[8], &dig[9],
		&C[0], &C[1], &C[2], &C[3], &C[4], &C[5]);

		k=0;
		for(j=0; j<6; j++){
			switch(C[j]){
			case 'A':
				senha_tmp[i][k] = dig[0];
				senha_tmp[i][k+1] = dig[1];
				k=k+2;
				break;
			case 'B':
				senha_tmp[i][k] = dig[2];
				senha_tmp[i][k+1] = dig[3];
				k=k+2;
				break;
			case 'C':
				senha_tmp[i][k] = dig[4];
				senha_tmp[i][k+1] = dig[5];
				k=k+2;
				break;
			case 'D':
				senha_tmp[i][k] = dig[6];
				senha_tmp[i][k+1] = dig[7];
				k=k+2;
				break;
			case 'E':
				senha_tmp[i][k] = dig[8];
				senha_tmp[i][k+1] = dig[9];
				k=k+2;
				break;
			}
		}
	}

	// DEBUG
	/*for(j=0; j<10; j++){
		printf("%d ", dig[j]);
	}
	printf("\n");
	for(j=0; j<6; j++){
		printf("%c ", C[j]);
	}
	printf("\n");
	for(j=0; j<N; j++){
		for(k=0; k<12; k++){
			printf("%d ", senha_tmp[j][k]);
		}
		printf("\n");
	}
	printf("\n");
	// DEBUG */


	// Comparação
	k=0;
	for(i=0; i<12; i=i+2){
		sel=0;
		for(j=0; j<N; j++){
			if(senha_tmp[0][i] != senha_tmp[j][i]){
				if(senha_tmp[0][i] != senha_tmp[j][i+1]){
					sel=1;
					break;
				}
			}
		}
		if(sel==0){
			senha[k]=senha_tmp[0][i];
			k++;
		}
		else{
			senha[k]=senha_tmp[0][i+1];
			k++;
		}
	}

	for(i=0; i<6; i++){
		//printf("SENHA %d ", senha[i]);
		senha_final[teste][i] = senha[i];
	}

	teste++;
	scanf("%d", &N);

	}

	printf("\n");

	for(i=0; i<teste; i++){

		printf("Teste %i \n", i+1);
			for(j=0; j<6; j++){
				printf("%d ", senha_final[i][j]);
			}
			printf("\n \n");
	}
}


