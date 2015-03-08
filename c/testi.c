#import <stdio.h>

int main(){
	int i = 2048;
	
	while(i >>= 1){
		printf("i = %d\n",i);
	}
	
	return 0;
}