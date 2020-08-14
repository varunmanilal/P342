#include<stdio.h>
#include<stdlib.h>
int main(){
	FILE *A;
	//Reading Matrix M from text file
	A = fopen("MatrixM.txt","r");
	float matM[3][3];
	int i,j;
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			fscanf(A,"%f*%c", &matM[i][j]);

		}
	}
	//reading matrix N file
	FILE *B;
	B = fopen("MatrixN.txt","r");
	float matN[3][3];
	int k,l;
	for(k=0;k<3;k++){
		for(l=0;l<3;l++){
			fscanf(B,"%f*%c", &matN[k][l]);

		}
	}
	//reading matrix a file
	FILE *C;
	C = fopen("MatrixA.txt","r");
	float vectorA[3][1];
	for(i=0;i<3;i++){
		for(j=0;j<1;j++){
			fscanf(C,"%f*%c", &vectorA[i][j]);

		}
	}
	



	//matrix C =A*B
	float matC[3][3]={
	{0, 0, 0},
	{0, 0, 0},
	{0, 0, 0},
	};
	printf("M*N is given as:\n");
	//I is the index of rows and j is the index of columns
	i=0;
	while(i<3){
		j=0;
		while(j<3){
			for(int k=0;k<3;k++){
				matC[i][j]+=matM[i][k]*matN[k][j];
			}
			j++;
		}
		i++;
	}
	//printing M*N
	for(i=0; i<3; i++) {
      for(j=0;j<3;j++) {
         	printf("%f ", matC[i][j]);
         	if(j==2){
            printf("\n");	
    		}
    	}
	}
	printf("\n M*A is given as:\n ");
	float matD[3][1] ={
	    {0},
	    {0},
	    {0},
	};
	//I is the index of rows and j is the index of columns
	i=0;
	while(i<3){
		j=0;
		while(j<1){
			for(int k=0;k<3;k++){
				matD[i][j]+=matM[i][k]*vectorA[k][j];
			}
			j++;
		}
		i++;
	}
	//printing M*A
	for(i=0; i<3; i++) {
      for(j=0;j<1;j++) {
         	printf("%f ", matD[i][j]);
         	if(j==2){
            printf("\n");	
    		}
    	}
	}
	
	
	
}
