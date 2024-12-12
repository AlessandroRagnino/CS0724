
# Simulazione di UDP Flood

## Descrizione del Progetto
Questo progetto consiste in una simulazione di attacco **UDP Flood**, sviluppato in Python, per comprendere meglio il funzionamento di attacchi DoS (Denial of Service). 
L'esercizio fa parte di un corso di Cybersecurity ed è destinato esclusivamente a scopi educativi.

Il programma consente di inviare un numero configurabile di pacchetti UDP a un indirizzo IP e una porta specificati dall'utente.

---

## Dettagli Tecnici
- **Linguaggio Utilizzato**: Python
- **Tipologia di Attacco**: UDP Flood
- **Dimensione dei Pacchetti**: 1 KB (1024 byte)

---

## Simulazione Eseguita
Durante l'esercitazione, è stato eseguito il programma creato su una macchina **Kali Linux** con l'indirizzo IP `192.168.50.100`.  
Sono stati inviati pacchetti UDP verso una macchina **Windows XP** con indirizzo IP `192.168.50.102` all'interno della stessa rete interna.  
Il programma è stato avviato utilizzando il comando `Run` e i dettagli richiesti sono stati forniti tramite input utente.

---

## Utilizzo del Programma
### Prerequisiti
- Python installato (versione 3.6 o superiore).

### Esecuzione
1. Scarica lo script `udp_flood.py`.
2. Avvia lo script in un terminale utilizzando:
   ```bash
   python udp_flood.py
   ```
3. Inserisci i seguenti dettagli quando richiesti:
   - IP della macchina target
   - Porta UDP della macchina target
   - Numero di pacchetti da inviare

---

## Nota di Sicurezza
Questo programma è progettato esclusivamente per scopi educativi. Non deve essere utilizzato per attività non autorizzate o illecite.  
L'uso improprio del programma può violare leggi locali e internazionali.

---

## Autore
Creato durante il corso di Cybersecurity come esercizio pratico di apprendimento.
