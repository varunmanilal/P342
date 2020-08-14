#include<stdio.h>
int main(){
	//vectors A and B
	double vectorA[3]={2.3, 5, 6};
	double vectorB[3]={6.1, 5.7, 8};
	double C[3] = {0, 0, 0};
	//A+B
	for(int i=0;i<3;i++){
		C[i]=vectorA[i]+vectorB[i];
		printf("%f",C[i]);
		printf(" ");
	}
	//A*B
	printf("\n");
		for(int j=0;j<3;j++){
		C[j]=vectorA[j]*vectorB[j];
		printf("%f",C[j]);
		printf(" ");
	}
}
