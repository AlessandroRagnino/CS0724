📌 Esercitazione S11L5: Analisi e Attacco con Strumenti di Cybersecurity
🛠️ Introduzione
Questa esercitazione esplora l'uso di strumenti di cybersecurity per analizzare e monitorare attività di rete. Verranno utilizzati PowerShell, Wireshark e Nmap, oltre all'analisi di attacchi a database MySQL.

🔹 Windows PowerShell
PowerShell è una piattaforma di automazione e gestione della configurazione sviluppata da Microsoft. Combina una shell a riga di comando con un linguaggio di scripting potente, consentendo agli utenti di eseguire comandi, automatizzare attività e gestire sistemi Windows e cloud. Andremo a confrontarla con il Prompt dei Comandi per evidenziare le differenze.

Comandi utilizzati
Ping per verifica connessione di rete
powershell
Copia
Modifica
ping google.com  
Visualizzazione file e directory
powershell
Copia
Modifica
dir  
Navigazione tra cartelle
powershell
Copia
Modifica
cd C:\\Users  
Visualizzazione della configurazione di rete
powershell
Copia
Modifica
ipconfig  
Verifica alias PowerShell
powershell
Copia
Modifica
Get-Alias dir  
Monitoraggio della tabella di routing
powershell
Copia
Modifica
netstat -r  
Visualizzazione delle connessioni di rete attive con dettagli sui processi
powershell
Copia
Modifica
netstat -abno  
Svuotare il Cestino
powershell
Copia
Modifica
Clear-RecycleBin  
🔹 Wireshark: Analisi del traffico HTTP & HTTPS
Wireshark è uno strumento essenziale per l'analisi dei pacchetti di rete. Qui analizzeremo il traffico HTTP e HTTPS per osservare le differenze di sicurezza.

Passaggi eseguiti
Cattura del traffico HTTP
bash
Copia
Modifica
sudo tcpdump -i enp0s3 -s 0 -w httpdump.pcap  
Navigazione su un sito HTTP ed effettuazione del login.
Apertura della cattura in Wireshark e applicazione del filtro:
Copia
Modifica
http  
Analisi del traffico HTTP, osservando richieste GET/POST con credenziali in chiaro.
Ripetizione della cattura con traffico HTTPS, utilizzando:
bash
Copia
Modifica
sudo tcpdump -i enp0s3 -s 0 -w httpsdump.pcap  
Analisi della crittografia TLS, applicando il filtro:
Copia
Modifica
tls  
🔹 Nmap: Scansione di rete
Nmap è uno strumento avanzato per la scansione di reti, utile per identificare porte aperte e servizi attivi.

Tipologie di scansioni eseguite
Scansione del localhost (127.0.0.1)
bash
Copia
Modifica
nmap -A -T4 localhost  
Scansione di una rete IP per elencare dispositivi e porte aperte:
bash
Copia
Modifica
nmap -sn 192.168.1.0/24  
Scansione di un server remoto con identificazione dettagliata:
bash
Copia
Modifica
nmap -A -T4 scanme.nmap.org  
🔹 Wireshark: Analisi di un attacco SQL Injection
Questa sezione analizza il traffico relativo a un attacco SQL Injection contro un database MySQL.

Passaggi eseguiti
Identificazione degli IP coinvolti (attaccante e server).
Apertura della conversazione HTTP Stream per osservare l’invio della query malevola.
Analisi dell’attacco:
Uso del payload 1=1 per verificare la vulnerabilità.
Query per ottenere il nome del database:
sql
Copia
Modifica
SELECT database();  
Estrazione delle tabelle disponibili:
sql
Copia
Modifica
SELECT table_name FROM information_schema.tables;  
Recupero di username e hash delle password:
sql
Copia
Modifica
SELECT username, password FROM users;  
🎯 Conclusioni
Questa esercitazione ha mostrato come:
✅ PowerShell può essere usato per il monitoraggio e la diagnostica di sistema.
✅ Wireshark permette di intercettare traffico HTTP e analizzare vulnerabilità.
✅ Nmap è essenziale per mappare reti e identificare servizi esposti.
✅ Analizzare gli attacchi SQL Injection aiuta a comprendere le minacce ai database.

📌🚀