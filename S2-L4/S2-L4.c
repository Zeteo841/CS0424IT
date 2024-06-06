#include <stdio.h>
#include <string.h>
#include <ctype.h> //Ho Inserito anche questo per usare la funzione toupper() per normalizzare le risposte

#define MAX_DOMANDE 3 // Definizione del numero massimo di domande (se viene modificato, bisogna aggiungere un'altra domanda)

// La struct assomiglia ad un dizioanrio in python, serve per raggruppare le variabili.
typedef struct {
    char Domande[256];
    char Opzioni[3][100];
    char Risp_Corretta;
} Quiz;

// Creazione della Funzione che spiega il gioco (richiamabile in modo easy dal main)
void SpiegazioneGioco() {
    printf("\nQuesto gioco consiste nel rispondere correttamente alle domande.\n");
    printf("Ogni domanda ha 3 risposte selezionabili. A fine gioco, il tuo punteggio verrà mostrato.\n");
    printf("NB: per vincere devi azzeccare almeno 2 risposte su 3.\n");
}

// Stessa cosa dell'aktra funzione ma per il menu'
void Menu() {
    printf("\n***********MENU'***********\n");
    printf(" A) Inizia una nuova partita\n");
    printf(" B) Esci dal gioco\n");
    printf(" Scegli 'A' per iniziare o 'B' per uscire.\n");
}

// Creazione Funzione che gestisce il flusso di gioco, fa domande, riceve risposte e calcola il punteggio
int Gioca(Quiz quizzes[], int numDomande) {
    char Risposta;
    int Punteggio = 0;
    char Nome_Giocatore[100];

    printf("Inserisci il tuo nome: ");
    scanf(" %99s", Nome_Giocatore); // Chiede il nome al giocatore (spero abbia un nome piu corto di 100 caratteri...)
    printf("\nCiao %s, iniziamo il gioco!\n", Nome_Giocatore);

    // Creazione di un loop lungo quante sono le domande, che stampa i le domande 
    for (int i = 0; i < numDomande; i++) {
        printf("\nDomanda %d: %s\n", i + 1, quizzes[i].Domande);
        // per ogni domanda esistono 3 risposte, quindi questo loop stampa le 3 possibili risposte
        for (int j = 0; j < 3; j++) {
            printf("%c) %s\n", 'A' + j, quizzes[i].Opzioni[j]);
        }
        printf("La tua risposta (A, B, C): ");
        // Scegli la risposta tra A,B,C
        scanf(" %c", &Risposta);
        if (toupper(Risposta) == quizzes[i].Risp_Corretta) {
            printf("Risposta corretta!\n");
            Punteggio++;
        } else {
            printf("Risposta sbagliata!\n");
        }
    }

    printf("\n%s, hai completato il gioco! Il tuo punteggio e': %d su %d\n", Nome_Giocatore, Punteggio, numDomande);
    return Punteggio;
}

// Il main fa funzionare il tutto
int main() {
    char Scegli;
    // Inizializzazione del set di domande
    Quiz quizzes[MAX_DOMANDE] = {
        {"Quale comando in bash mostra i file per data?", {"ls -l", "ls -t", "ls -a"}, 'B'},
        {"In che linguaggio e' fondamentale l'identazione?", {"C++", "C", "Python"}, 'C'},
        {"Se mostro un pezzo di codice simile in C: 'unsigned long long array[n];'", {"32", "480", "6400"}, 'C'}
    };

    // Parte la spiegazione del gioco
    SpiegazioneGioco();
    //  questo do while serve per far funzionare lo scritp affiche non lo interrompa lui stesso con 'B' o 'b'
    do {
        Menu();
        scanf(" %c", &Scegli); // Legge la scelta dell'utente 

        if (Scegli == 'A' || Scegli == 'a') {
            Gioca(quizzes, MAX_DOMANDE); // Avvia la partita se l'opzione è 'A' o 'a'
        } else if (Scegli != 'B' && Scegli != 'b') {
            printf("Seleziona una delle lettere correnti\n");
        }
    } while (Scegli != 'B' && Scegli != 'b'); // Continua fino a quando l'utente non sceglie di uscire con 'B' o 'b'

    printf("Uscita dal gioco...\n");
    return 0;
}

