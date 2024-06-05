#include<stdio.h>
#include<stdlib.h>
#include <math.h>

//utilizzo dei paramentri argc e argv
int main(){
    // Creazione variabili
    float n1;
    float n2;
    double sum;
    double diff;
    double prod;
    double div;
    double media;
    double modulo;

    // Richiesta dei 2 numeri in input
    printf("Immetti il primo numero:\n");
    scanf("%f", &n1);
    printf("Immetti il secondo numero:\n");
    scanf("%f", &n2);

    // Impedisce la scelta del numero 0 per evitare la divisione per 0
    while( n2 == 0){
        printf("Metti un numero diverso da zero:\n");
        scanf("%f", &n2);
    }
    
    // Definizione variabili
    sum = n1 + n2;
    diff = n1 - n2;
    prod = n1 * n2;
    div = n1 / n2;
    media = (n1 + n2)/2;
    modulo = fmod(n1, n2);

    // Stampa delle variabili
    printf("La somma dei 2 numeri scelti e': %.2f\n",sum);
    printf("La differenza dei 2 numeri scelti e': %.2f\n",diff);
    printf("Il prodotto dei 2 numeri scelti e': %.2f\n",prod);
    printf("La divisione dei 2 numeri scelti e': %.2f\n",div);
    printf("La media dei 2 numeri scelti e': %.2f\n",media);
    printf("Il modulo dei 2 numeri scelti e': %.2f\n",modulo);


    return 0;
}
