
# Progetto Cybersecurity: Social Engineering e Analisi dei CVE

## Descrizione

Questo repository contiene un progetto di cybersecurity incentrato su:
1. Analisi e spiegazione delle tecniche di **social engineering**.
2. Descrizione delle strategie difensive per mitigare gli attacchi.
3. Approfondimenti su vulnerabilità note (CVE) relative a Kali Linux, Metasploitable e Windows XP.

---

## Indice

1. [Introduzione](#introduzione)
2. [Social Engineering](#social-engineering)
   - [Tecniche Comuni](#tecniche-comuni)
3. [Strategie di Difesa](#strategie-di-difesa)
4. [Analisi delle Vulnerabilità (CVE)](#analisi-delle-vulnerabilità-cve)
   - [Kali Linux](#kali-linux)
   - [Metasploitable](#metasploitable)
   - [Windows XP](#windows-xp)
5. [Conclusioni](#conclusioni)

---

## Introduzione

Questo progetto è stato sviluppato durante il primo mese del mio corso intensivo di cybersecurity. L'obiettivo principale è stato:
- Esplorare e comprendere i principali attacchi di social engineering.
- Analizzare vulnerabilità note (CVE) di sistemi operativi e strumenti di test.

---

## Social Engineering

### Che cos'è il Social Engineering?
Il **social engineering** è una tecnica di attacco che sfrutta le vulnerabilità umane per accedere a informazioni sensibili o sistemi protetti. Non richiede necessariamente competenze tecniche avanzate, ma si basa sulla manipolazione psicologica delle vittime.

---

### Tecniche Comuni

1. **Phishing**  
   Comunicazioni fraudolente per rubare dati sensibili.  
   - **Varianti**: Spear phishing, whaling, smishing, vishing.

2. **Tailgating (Piggybacking)**  
   Ingresso fisico non autorizzato seguendo una persona autorizzata.

3. **Pretexting**  
   Creazione di false identità o scenari per ingannare la vittima.

4. **Baiting**  
   Uso di ricompense per indurre la vittima a compiere azioni pericolose.

5. **Impersonation**  
   Fingere di essere un'entità affidabile per ottenere informazioni sensibili.

6. **Dumpster Diving**  
   Ricerca di dati sensibili in documenti o dispositivi scartati.

---

## Strategie di Difesa

1. **Formazione e Consapevolezza**
   - Simulare attacchi per testare le reazioni.
   - Educare gli utenti a riconoscere tentativi di phishing.

2. **Verifica delle Identità**
   - Non condividere informazioni senza verifiche.
   - Usare canali ufficiali per comunicazioni sensibili.

3. **Controlli Fisici**
   - Implementare badge di accesso e sistemi biometrici.

4. **Protezione delle Credenziali**
   - Utilizzare password uniche e robustezza.
   - Abilitare l'autenticazione a due fattori (2FA).

5. **Distruzione Sicura dei Dati**
   - Distruggere documenti fisici e dispositivi smaltiti.

---

## Analisi delle Vulnerabilità (CVE)

### Kali Linux
1. **CVE-2024-26581**  
   Vulnerabilità "Use After Free" nel kernel Linux che consente l'esecuzione di codice arbitrario.  
   **Soluzione**: Aggiornamento del kernel alla versione >6.2.

2. **CVE-2023-6111**  
   Consente l'escalation di privilegi su alcune distribuzioni basate su Debian.  
   **Soluzione**: Applicare le patch di sicurezza disponibili.

---

### Metasploitable
1. **CVE-2020-7385**  
   Exploit nel modulo `drb_remote_codeexec` del Metasploit Framework.  
   **Soluzione**: Non utilizzare moduli vulnerabili.

2. **CVE-2017-15944**  
   Backdoor in VSFTPD 2.3.4.  
   **Soluzione**: Aggiornamento del software.

---

### Windows XP
1. **CVE-2010-0232**  
   Elevazione di privilegi nel kernel Windows.  
   **Soluzione**: Passare a una versione supportata di Windows.

2. **CVE-2009-1544**  
   Esecuzione di codice arbitrario tramite gestione impropria della memoria.  
   **Soluzione**: Mitigazione tramite software di sicurezza.

---

## Conclusioni

Questo progetto ha evidenziato:
- L'importanza della consapevolezza umana nella prevenzione degli attacchi di social engineering.
- La necessità di mantenere aggiornati i sistemi per proteggersi da vulnerabilità note.
- L'uso pratico di strumenti come Metasploit e Kali Linux per testare e analizzare vulnerabilità.

---

Se hai domande o suggerimenti, sentiti libero di aprire un'issue su questo repository. 😊

---
