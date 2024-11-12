#include<stdio.h>
int main() {
    float media;
    int numero1, numero2, risultato;

    printf("Inserisci il primo numero: ");
    scanf("%d", &numero1);

    printf("Inserisci il secondo numero: ");
    scanf("%d", &numero2);

    risultato = numero1 * numero2;

    printf("Il risultato della moltiplicazione e': %d\n", risultato);


printf("Inserisci il primo numero intero per la divisione: ");
    scanf("%d", &numero1);

    printf("Inserisci il secondo numero intero per la divisione: ");
    scanf("%d", &numero2);


float divisione(int numero1, int numero2);
      
    printf("Hai inserito i numeri: %d e %d\n", numero1, numero2);

    
    media = (numero1 + numero2) / 2.0;


    printf("La media aritmetica è: %.2f\n", media);




    return 0;
}