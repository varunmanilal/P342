#include<stdio.h>
#include <stdlib.h>
int main(){
	//(x1,y1) is first point .(x2,y2) is second point.
	int x1 =1;
	int y1 =1;
	int x2 =1;
	int y2 =1;
	int max=6;
	float no=0;
	float length =0;
	//mapped from 1 to 6
	while(y1<=max){
		x1=1;
		while(x1<=max){
			y2=1;
			while(y2<=max){
				x2=1;
				while(x2<=max){
					length+=abs(x2-x1)+abs(y2-y1);
					no+=1;
					x2+=1;
				}
				y2+=1;
			}
			x1+=1;
		}
		y1+=1;
	}
	
printf("Total length is %lf",length);
float average = length/no;
printf("\nThe average distance is: ");
printf("%lf",average);		
}


