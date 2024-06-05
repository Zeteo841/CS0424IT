#include<stdio.h>


float MEDIA(float num1, float num2){
    float media = (num1 + num2)/2;
    return media;
}


int main(){

    float num1;
    float num2;

    printf("immetti il primo numero\n");
    scanf("%f", &num1);
    printf("immetti il secondo numero\n");
    scanf("%f", &num2);

    float media = MEDIA(num1,num2);
    printf("La media dei due numeri scelti e': %.2f",media);
    return 0;

}