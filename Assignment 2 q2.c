#include<stdio.h>
int main(){
	//vectors A and B
	double vectorA[3]={2.3, 5, 6};
	double vectorB[3]={6.1, 5.7, 8};
	double C[3] = {0, 0, 0};
	double D=0;
	//A*B
	for(int i=0;i<3;i++){
		D+=vectorA[i]*vectorB[i];
	}
	printf("The dot product A.B is: %f",D);
	//A+B
	printf("\nThe sum A+B is: \n");
		for(int j=0;j<3;j++){
		C[j]=vectorA[j]+vectorB[j];
		printf("%f",C[j]);
		printf(" ");
	}
}
