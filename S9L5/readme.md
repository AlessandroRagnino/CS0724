# Guida: Analisi di una Cattura di Rete con Wireshark

Questa guida spiega, passo dopo passo, come analizzare una cattura di rete utilizzando **Wireshark**. L'obiettivo è identificare eventuali Indicatori di Compromissione (IOC), ipotizzare i vettori di attacco e proporre azioni per mitigare i rischi.

---

## **Passaggio 1: Apertura del file di cattura**

1. **Avvia Wireshark** sul tuo computer.
2. Vai su **File > Open** e seleziona il file di cattura (ad esempio, `Cattura_U3_W1_L5.pcapng`).
3. Una volta aperto, vedrai una lista di pacchetti catturati con informazioni su:
   - **Time** (tempo del pacchetto)
   - **Source** (indirizzo IP sorgente)
   - **Destination** (indirizzo IP di destinazione)
   - **Protocol** (protocollo utilizzato, es. TCP, DNS)
   - **Info** (ulteriori dettagli sul pacchetto)

---

## **Passaggio 2: Isolamento del traffico sospetto**

### Filtri utili
Utilizziamo i filtri di Wireshark per concentrarci sui pacchetti più rilevanti:

1. **Filtra per indirizzo IP sospetto**:
   ```
   ip.addr == 192.168.200.150 || ip.addr == 192.168.200.100
   ```
   Questo filtro mostra tutto il traffico tra gli indirizzi IP **192.168.200.150** e **192.168.200.100**.

2. **Individua traffico TCP con anomalie**:
   - **SYN senza ACK** (scansioni di rete):
     ```
     tcp.flags.syn == 1 && tcp.flags.ack == 0
     ```
   - **RST frequenti** (connessioni chiuse):
     ```
     tcp.flags.rst == 1
     ```

3. **Cerca richieste DNS** (domini sospetti):
   ```
   dns
   ```

4. **Filtra traffico su porte specifiche** (es. porte note per attività malevole, come 4444 o 3389):
   ```
   tcp.port == 4444 || tcp.port == 3389
   ```

---

## **Passaggio 3: Analisi dei dettagli**

1. **Controlla i pacchetti sospetti**:
   - Seleziona un pacchetto TCP sospetto.
   - Fai clic destro sul pacchetto e scegli **Follow > TCP Stream**.
   - Analizza i dati della comunicazione (se presenti). Cerca:
     - Dati insoliti o non crittografati.
     - Modelli ripetitivi di richieste.

2. **Verifica il contesto del traffico**:
   - Controlla chi comunica con chi.
   - Analizza il volume di dati scambiati.
   - Identifica modelli di comportamento anomali, come connessioni frequenti senza risposte.

3. **Richieste DNS**:
   - Esamina i domini richiesti.
   - Cerca nomi di dominio sospetti o sconosciuti.

---

## **Passaggio 4: Identificazione degli Indicatori di Compromissione (IOC)**

Dall'analisi dei pacchetti, abbiamo identificato i seguenti IOC:

1. **Indirizzi IP sospetti**:
   - **192.168.200.150**: Sembra essere l'origine della maggior parte delle connessioni.
   - **192.168.200.100**: Destinatario principale del traffico.

2. **Traffico TCP anomalo**:
   - Molti pacchetti con flag **SYN** senza follow-up (indicativo di una scansione di rete).
   - Numerosi pacchetti con flag **RST**, che possono indicare un tentativo di Denial of Service (DoS).

3. **Assenza di payload utili**:
   - I pacchetti non contengono dati significativi, suggerendo che l'attacco è in una fase iniziale (es. ricognizione).

---

## **Passaggio 5: Ipotesi sui vettori di attacco**

1. **Scansione di rete**:
   - L'attaccante sta cercando di identificare porte aperte su **192.168.200.100**.
   - Supportato dai pacchetti SYN senza ACK.

2. **Attacco DoS**:
   - L'elevato numero di pacchetti RST suggerisce un tentativo di interrompere le connessioni o sovraccaricare il sistema.

3. **Esfiltrazione dati non evidente**:
   - Nessun payload significativo nei pacchetti indica che non ci sono esfiltrazioni di dati in corso.

---

## **Passaggio 6: Azioni consigliate**

### **Azioni immediate**:
1. **Bloccare IP sospetti**:
   - Configurare regole del firewall per bloccare il traffico proveniente da **192.168.200.150**, se non è un dispositivo legittimo.

2. **Monitorare i log di rete**:
   - Analizzare i log per identificare tentativi di connessione simili da altri IP.

3. **Isolare i dispositivi compromessi**:
   - Se **192.168.200.150** è interno alla rete, isolarlo per verificare eventuali compromissioni.

### **Azioni preventive**:
1. **Implementare un IDS/IPS**:
   - Utilizzare un sistema di rilevamento e prevenzione delle intrusioni per identificare automaticamente comportamenti sospetti.

2. **Abilitare il logging DNS**:
   - Registrare e analizzare tutte le richieste DNS per rilevare domini malevoli.

3. **Formazione del personale**:
   - Educare gli utenti su pratiche di sicurezza per prevenire compromissioni interne.

4. **Aggiornare e patchare i sistemi**:
   - Assicurarsi che tutti i dispositivi siano aggiornati con le ultime patch di sicurezza.

---

## **Conclusione**

Dall'analisi della cattura di rete, abbiamo identificato un comportamento sospetto che suggerisce un tentativo di ricognizione (scansione di rete) e potenzialmente un attacco DoS. Le azioni consigliate includono il blocco degli IP sospetti, il monitoraggio dei log e l'implementazione di misure preventive per proteggere la rete.

Se hai bisogno di ulteriori dettagli o hai domande, non esitare a chiedere!
