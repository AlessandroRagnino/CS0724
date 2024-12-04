# Analisi delle Vulnerabilità con Nessus su Metasploitable

Questo progetto documenta un'esercitazione pratica svolta con **Nessus**, uno scanner di vulnerabilità, utilizzato per analizzare **Metasploitable**, un ambiente vulnerabile progettato per scopi didattici. L'obiettivo principale è stato configurare diverse scansioni di rete, identificare vulnerabilità e proporre raccomandazioni per mitigare i rischi.

---

## Scopo dell'Esercitazione

- Configurare una scansione di rete con Nessus.
- Analizzare le vulnerabilità rilevate in un ambiente volutamente vulnerabile.
- Comprendere l'impatto delle vulnerabilità critiche.
- Proporre soluzioni per mitigare i rischi di sicurezza.

---

## Scansioni Effettuate

### **1. Scansione Completa**  
#### Configurazione:
- **Target**: `192.168.50.101` (IP della macchina Metasploitable).
- **Tipo di scansione**: Scansione completa su tutte le porte.
- **Profilo utilizzato**: "Basic Network Scan".
- **Tempo di scansione**: 36 minuti.

#### Risultati principali:
- **Numero totale di vulnerabilità**: 18  
  - Critiche: 5  
  - Alte: 2  
  - Medie: 3  
  - Miste: 6  
  - Basse: 2  

#### Vulnerabilità critiche rilevate:
1. **VNC Server 'password' Password** *(CVSS 10.0)*: Rischio di accesso remoto completo.  
2. **Apache Tomcat AJP Connector Request Injection (Ghostcat)** *(CVSS 9.8)*: Permette l'esecuzione arbitraria di codice.  
3. **SSL Version 2 and 3 Protocol Detection**: Utilizzo di protocolli obsoleti e insicuri.  

---

### **2. Scansione Avanzata**  
#### Configurazione:
- **Target**: `192.168.50.101` (IP della macchina Metasploitable).
- **Porte analizzate**: 21, 22, 23, 25, 80, 110, 139, 443, 445, 3389.
- **Profilo utilizzato**: "Advanced Scan".
- **Tempo di scansione**: 31 minuti.

#### Risultati principali:
- **Numero totale di vulnerabilità**: 18  
  - Critiche: 5  
  - Alte: 2  
  - Medie: 3  
  - Miste: 6  
  - Basse: 2  

#### Osservazioni:
- Le vulnerabilità critiche rilevate coincidono con quelle della scansione completa.
- La scansione completa ha evidenziato vulnerabilità su porte non standard, dimostrando l'importanza di analizzare l'intero spettro delle porte in ambienti potenzialmente compromessi.

---

## Impatto delle Vulnerabilità Critiche

1. **Accesso remoto tramite VNC** con credenziali deboli rappresenta un rischio immediato, consentendo il controllo totale del sistema.  
2. **Ghostcat su Apache Tomcat** espone il sistema a compromissioni totali tramite esecuzione di codice remoto.  
3. **Problemi di configurazione SSL** possono portare a intercettazioni e compromissione delle comunicazioni crittografate.  

---

## Raccomandazioni

### 1. **Aggiornare i sistemi e disabilitare protocolli obsoleti**  
- Disabilitare SSLv2/SSLv3 e configurare il server per utilizzare TLS moderno (1.2/1.3).  

### 2. **Rinforzare l'autenticazione**  
- Cambiare le password predefinite per VNC e altre applicazioni.  
- Implementare restrizioni di accesso basate su IP e VPN, ove possibile.  

### 3. **Verifica continua**  
- Eseguire scansioni periodiche su tutte le porte.  
- Analizzare i risultati con framework di exploit come Metasploit per testare le vulnerabilità rilevate.

---

## Focus sulle Vulnerabilità Critiche

### 1. **VNC Server 'password' Password**
- **Descrizione**: Password debole che consente accesso remoto completo al sistema.  
- **Impatto**: Controllo totale della macchina.  
- **Raccomandazioni**:  
  - Sostituire la password predefinita con una più complessa.  
  - Disabilitare VNC se non necessario.  

### 2. **Apache Tomcat AJP Connector Request Injection (Ghostcat)**
- **Descrizione**: Consente lettura di file arbitrari ed esecuzione di codice JSP.  
- **Impatto**: Controllo totale del server.  
- **Raccomandazioni**:  
  - Aggiornare Apache Tomcat.  
  - Disabilitare il connettore AJP se non necessario.  

### 3. **SSL Version 2 and 3 Protocol Detection**
- **Descrizione**: Protocolli SSL deprecati, vulnerabili a diversi attacchi come POODLE.  
- **Impatto**: Intercettazione e compromissione delle comunicazioni crittografate.  
- **Raccomandazioni**:  
  - Disabilitare SSLv2 e SSLv3.  
  - Configurare il server per abilitare solo protocolli moderni.  

### 4. **Bind Shell Backdoor Detection**
- **Descrizione**: Backdoor che consente accesso remoto e bypass delle autenticazioni.  
- **Impatto**: Esecuzione arbitraria di comandi con privilegi elevati.  
- **Raccomandazioni**:  
  - Rimuovere immediatamente la backdoor.  
  - Eseguire una scansione antivirus e verificare i file compromessi.  

### 5. **SSL (Multiple Issues)**
- **Descrizione**: Suite di cifratura obsolete o configurazioni errate.  
- **Impatto**: Intercettazioni e attacchi man-in-the-middle.  
- **Raccomandazioni**:  
  - Configurare il server per abilitare solo protocolli e suite moderni.  

---

## Conclusione

Questa esercitazione ha dimostrato l'importanza di eseguire scansioni di rete approfondite e configurare correttamente i servizi. Le vulnerabilità critiche, se non mitigate, possono compromettere gravemente la sicurezza di un sistema. Le raccomandazioni proposte devono essere implementate con priorità per minimizzare i rischi.

---

