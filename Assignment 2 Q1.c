#include<stdio.h>
#include<stdlib.h>
int main(){
	
	int no = 0;
	double numb = 1;
	double index = 1;
	double length = 0;
	while (index<=6){
		int numb=1;
		while (numb<=6){
			length=length+abs(numb-index);
			no+=1;
			numb+=1;
		}
		index+=1;
	
	}
	
	printf("Total distance is ");
	printf("%f",length);

	printf("\nThe average distance is ");
	printf("%f",length/no);

}
