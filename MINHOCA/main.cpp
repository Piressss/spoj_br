/*
 * main.cpp
 *
 *  Created on: Jan 15, 2015
 *      Author: fpires
 */

#include<stdio.h>

int main(){

	int N, M, i, j, result=0, soma=0;
	int array[100][100];

	scanf("%d %d", &N, &M);

	for(i=0; i<N; i++){
		for(j=0; j<M; j++){
			scanf("%d", &array[i][j]);
		}
	}

	/*for(i=0; i<N; i++){
			for(j=0; j<M; j++){
				printf("%d ", array[i][j]);
			}
			printf("\n");
		}*/

	// Varredura em linha
	for(i=0; i<N; i++){
			for(j=0; j<M; j++){
				soma=soma+array[i][j];
			}
			if(soma > result){
				result=soma;
			}
			//printf("SOMA= %d\n", soma);
			soma=0;
		}

	// Varredura em coluna
		for(i=0; i<M; i++){
				for(j=0; j<N; j++){
					soma=soma+array[j][i];
				}
				if(soma > result){
					result=soma;
				}
				//printf("SOMA= %d\n", soma);
				soma=0;
			}

	printf("\n%d\n", result);
}


