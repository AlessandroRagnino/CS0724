# 📖 Consegna S11/L1 - Remediation & Mitigazione

## 🌍 Introduzione
Ciao e benvenuto! 🚀 Questo documento ti guiderà attraverso il processo di **remediation** e **mitigazione** delle minacce informatiche legate al **phishing** e agli **attacchi DoS (Denial of Service)**. L'obiettivo è fornirti una panoramica chiara e dettagliata su come affrontare queste problematiche, proteggendo al meglio i sistemi aziendali. 🔐

Nel mondo della **cybersecurity**, affrontare queste minacce richiede un mix di strategie:
- **Remediation**: eliminare completamente le vulnerabilità con interventi mirati. 🛠️
- **Mitigazione**: ridurre il rischio e limitare i danni finché non vengono implementate soluzioni definitive. ⚠️

---
## 🕵️ Parte 1: Minaccia di Phishing

### 📌 Cos'è il phishing?
Il **phishing** è una delle tecniche di attacco più diffuse e insidiose. 🕵️‍♂️ Gli aggressori utilizzano email fraudolente, siti web contraffatti e tecniche di **social engineering** per sottrarre dati sensibili o indurre azioni dannose. Questi messaggi, spesso camuffati da enti affidabili (banche, aziende, colleghi), possono compromettere seriamente la sicurezza aziendale. 🚨

### 🔍 Analisi del rischio
**Impatto potenziale:**
- 🏢 **Compromissione di account aziendali** con accesso non autorizzato a risorse critiche.
- 🦠 **Diffusione di malware** come ransomware e spyware.
- ⚠️ **Danni reputazionali** che possono minare la fiducia di clienti e partner.

Le risorse più a rischio includono **email aziendali, database sensibili e credenziali di accesso** ai sistemi gestionali e finanziari.

### 🛠 Piano di remediation
Per affrontare efficacemente un attacco di **phishing**, segui questi passaggi:

1️⃣ **Bloccare immediatamente le email sospette** 📧
   - Configurare filtri avanzati anti-phishing con **Microsoft Defender for Office 365** o **Proofpoint**.
   - Abilitare SPF, DKIM e DMARC per prevenire lo **spoofing** dei domini aziendali.
   - Creare regole personalizzate per individuare pattern sospetti.

2️⃣ **Formare e sensibilizzare i dipendenti** 🧑‍🏫
   - Organizzare **workshop regolari** per riconoscere email malevole.
   - Creare procedure chiare per **segnalare un tentativo di phishing**.
   - Eseguire **simulazioni periodiche** per testare la consapevolezza.

3️⃣ **Monitorare continuamente i sistemi** 🖥️
   - Implementare un **SIEM** (Security Information and Event Management) per analizzare i log.
   - Utilizzare strumenti come **CrowdStrike o Carbon Black** per il rilevamento delle minacce.

4️⃣ **Pulizia e recupero** 🔄
   - Revocare immediatamente le credenziali compromesse.
   - Eseguire **scansioni di sicurezza** approfondite.
   - Applicare le **patch di sicurezza** per chiudere le vulnerabilità.

### 🌐 Mitigazione dei rischi residui
✅ Abilitare **autenticazione a due fattori (2FA)** su tutti gli account critici.
✅ Effettuare **backup regolari** dei dati sensibili.
✅ Condurre **test periodici** per valutare la prontezza contro nuovi tentativi di attacco. 🔄

---
## 💥 Parte 2: Attacco DoS (Denial of Service)

### 📌 Cos'è un attacco DoS?
Un attacco **DoS** mira a rendere indisponibili i servizi sovraccaricando i server con traffico eccessivo. 🏴‍☠️ Questo può includere:
- **Saturazione della larghezza di banda** 🚦
- **Esaurimento delle risorse hardware** come CPU e RAM 💾

Quando l'attacco è **distribuito (DDoS)**, una **botnet** amplifica l'effetto, rendendo la mitigazione più complessa. ⚡

### 🔍 Analisi del rischio

**Impatto potenziale:**
- ❌ **Interruzione dei servizi critici** per clienti e dipendenti.
- 💸 **Danni economici** dovuti alla perdita di entrate e ai costi di ripristino.
- 📉 **Danni reputazionali** legati a disservizi prolungati.

**Servizi vulnerabili:**
- 🌐 **Server web** e sistemi di pagamento online.
- 🛡️ **Applicazioni interne/esterne critiche**.
- 🗂️ **Database aziendali**.

### 🛠 Piano di remediation

1️⃣ **Identificare le fonti del traffico malevolo** 🔍
   - Analizzare i **log di rete** con strumenti come **Wireshark o Zeek**.
   - Isolare e bloccare gli **IP sospetti** con firewall dinamici.
   - Collaborare con il provider di rete per mitigare il traffico dannoso.

2️⃣ **Mitigare il traffico malevolo** 🚦
   - Configurare un **Web Application Firewall (WAF)**.
   - Usare soluzioni **anti-DDoS** come **Cloudflare o AWS Shield**.
   - Implementare il **blackhole routing** per deviare il traffico sospetto.

3️⃣ **Distribuire il carico e migliorare la resilienza** ⚙️
   - Implementare un **load balancer** (es. HAProxy) per distribuire il traffico.
   - Usare una **Content Delivery Network (CDN)** per alleggerire i server.
   - Potenziare le risorse hardware per gestire i picchi di traffico. 📈

4️⃣ **Recupero e miglioramento** 🔄
   - Ripristinare i **servizi critici** con backup recenti.
   - Aggiornare le **regole di firewall** per prevenire futuri attacchi.
   - Condurre un'**analisi post-incidente** per rafforzare le difese. 🏰

### 🌐 Mitigazione dei rischi residui
✅ Monitorare il **traffico di rete** con strumenti di analisi avanzati 📊
✅ Organizzare **test periodici** per valutare l'efficacia delle misure di mitigazione 🛡️
✅ Creare **piani di emergenza dettagliati** per garantire continuità operativa 🚀
