# 📌 Esercitazione S11L5: 🔍 Analisi e Attacco con Strumenti di Cybersecurity

## 🛠️ Introduzione
Questa esercitazione esplora l'uso di strumenti di cybersecurity per **analizzare e monitorare** attività di rete.  
Verranno utilizzati:  
🔹 **PowerShell**  
🔹 **Wireshark**  
🔹 **Nmap**  
🔹 **Analisi attacchi SQL Injection su MySQL**  

---

## ⚡ Windows PowerShell: Diagnostica & Automazione  
PowerShell è una piattaforma di **automazione e gestione** per sistemi Windows e cloud.  

### 📌 Comandi utilizzati  

✅ **Ping per verifica connessione di rete**  
```powershell
ping google.com
```
📸 **Screenshot**  
![Ping Screenshot](./ping_screenshot.png)

✅ **Visualizzazione file e directory**  
```powershell
dir
```
📸 **Screenshot**  
![Dir Screenshot](./dir_screenshot.png)

✅ **Navigazione tra cartelle**  
```powershell
cd C:\Users
```
📸 **Screenshot**  
![CD Screenshot](./cd_screenshot.png)

✅ **Visualizzazione della configurazione di rete**  
```powershell
ipconfig
```
📸 **Screenshot**  
![IPConfig Screenshot](./ipconfig_screenshot.png)

✅ **Monitoraggio della tabella di routing**  
```powershell
netstat -r
```
📸 **Screenshot**  
![Netstat Screenshot](./netstat_screenshot.png)

✅ **Visualizzazione delle connessioni di rete attive con dettagli sui processi**  
```powershell
netstat -abno
```
📸 **Screenshot**  
![Netstat Active Screenshot](./netstat_active_screenshot.png)

✅ **Svuotare il Cestino**  
```powershell
Clear-RecycleBin
```
📸 **Screenshot**  
![RecycleBin Screenshot](./recyclebin_screenshot.png)

---

## 🌐 Wireshark: Analisi del traffico HTTP & HTTPS  
Wireshark è uno **strumento essenziale** per l'analisi dei pacchetti di rete.  
Qui analizzeremo il traffico HTTP e HTTPS per osservare le **differenze di sicurezza**.

### 📌 Passaggi eseguiti  

✅ **Cattura del traffico HTTP**  
```bash
sudo tcpdump -i enp0s3 -s 0 -w httpdump.pcap
```
📸 **Screenshot**  
![HTTP Dump Screenshot](./httpdump_screenshot.png)

✅ **Apertura della cattura in Wireshark e applicazione del filtro HTTP**  
```
http
```
📸 **Screenshot**  
![Wireshark HTTP Screenshot](./wireshark_http_screenshot.png)

✅ **Ripetizione della cattura con traffico HTTPS**  
```bash
sudo tcpdump -i enp0s3 -s 0 -w httpsdump.pcap
```
📸 **Screenshot**  
![HTTPS Dump Screenshot](./httpsdump_screenshot.png)

✅ **Analisi della crittografia TLS**  
```
tls
```
📸 **Screenshot**  
![Wireshark TLS Screenshot](./wireshark_tls_screenshot.png)

---

## 🎯 Nmap: Scansione di rete  
Nmap è uno **strumento avanzato** per la scansione di reti, utile per identificare **porte aperte e servizi attivi**.

### 📌 Tipologie di scansioni eseguite  

✅ **Scansione del localhost (127.0.0.1)**  
```bash
nmap -A -T4 localhost
```
📸 **Screenshot**  
![Nmap Localhost Screenshot](./nmap_localhost_screenshot.png)

✅ **Scansione di una rete IP per elencare dispositivi e porte aperte**  
```bash
nmap -sn 192.168.1.0/24
```
📸 **Screenshot**  
![Nmap Network Screenshot](./nmap_network_screenshot.png)

✅ **Scansione di un server remoto con identificazione dettagliata**  
```bash
nmap -A -T4 scanme.nmap.org
```
📸 **Screenshot**  
![Nmap Remote Screenshot](./nmap_remote_screenshot.png)

---

## 🔥 Wireshark: Analisi di un attacco SQL Injection  
Questa sezione analizza il traffico relativo a un attacco **SQL Injection** contro un database **MySQL**.

### 📌 Passaggi eseguiti  

✅ **Identificazione degli IP coinvolti (attaccante e server).**  
📸 **Screenshot**  
![SQL IP Screenshot](./sql_ip_screenshot.png)

✅ **Apertura della conversazione HTTP Stream per osservare l’invio della query malevola.**  
📸 **Screenshot**  
![SQL Stream Screenshot](./sql_stream_screenshot.png)

✅ **Uso del payload `1=1` per verificare la vulnerabilità.**  

✅ **Query per ottenere il nome del database:**  
```sql
SELECT database();
```
📸 **Screenshot**  
![SQL Database Screenshot](./sql_database_screenshot.png)

✅ **Estrazione delle tabelle disponibili:**  
```sql
SELECT table_name FROM information_schema.tables;
```
📸 **Screenshot**  
![SQL Tables Screenshot](./sql_tables_screenshot.png)

✅ **Recupero di username e hash delle password:**  
```sql
SELECT username, password FROM users;
```
📸 **Screenshot**  
![SQL Users Screenshot](./sql_users_screenshot.png)

---

## 🚀 Conclusioni  
Questa esercitazione ha mostrato come:

✅ **PowerShell** può essere usato per il monitoraggio e la diagnostica di sistema.  
✅ **Wireshark** permette di intercettare traffico HTTP e analizzare vulnerabilità.  
✅ **Nmap** è essenziale per mappare reti e identificare servizi esposti.  
✅ **Analizzare gli attacchi SQL Injection** aiuta a comprendere le minacce ai database.  

🔐 **Proteggi sempre la tua rete e approfondisci la cybersecurity!** 🔥

📌🚀 **Buon lavoro!** 🎯