# 🔍 Analisi della Stretta di Mano TCP con Wireshark e tcpdump

## 📌 Introduzione

Questa guida dettagliata documenta l’uso di **Wireshark** e **tcpdump** per analizzare la **stretta di mano TCP a tre vie**. Verranno catturati e analizzati pacchetti di rete per comprendere meglio il funzionamento del protocollo TCP.

---

## 🔹 1. Preparazione degli Host

### ✅ 1.1 Avviare la VM CyberOps  
1. Accedere con:
   ```bash
   user: analyst  
   password: cyberops
   ```
2. Avviare Mininet con il comando:
   ```bash
   sudo lab.support.files/scripts/cyberops/start_mininet.sh
   ```

3. Avviare gli host H1 e H4:
   ```bash
   mininet> xterm H1
   mininet> xterm H4
   ```

4. Avviare il server web su H4:
   ```bash
   /home/analyst/lab.support.files/scripts/start_web_server.sh
   ```

5. Per motivi di sicurezza, su H1 passare all’utente analyst:
   ```bash
   su analyst
   ```

6. Avviare il browser Firefox su H1:
   ```bash
   firefox &
   ```

📸 **Scattare screenshot di ogni passaggio.**

---

## 🔹 2. Cattura dei Pacchetti con tcpdump

1️⃣ **Avviare la cattura su H1**  
   ```bash
   sudo tcpdump -i H1-eth0 -v -c 50 -w capture.pcap
   ```

2️⃣ **Generare traffico TCP visitando il server web su H4**  
   - Aprire Firefox su H1 e accedere a:  
     `http://172.16.0.40`

3️⃣ **Attendere la cattura di 50 pacchetti e salvare lo screenshot.**

📸 **Screenshot del terminale con tcpdump attivo.**

---

## 🔹 3. Analisi dei Pacchetti con Wireshark

1️⃣ **Avviare Wireshark su H1**  
   ```bash
   wireshark &
   ```

2️⃣ **Aprire il file di acquisizione**  
   - **File > Apri**  
   - Selezionare `/home/analyst/capture.pcap`

3️⃣ **Applicare un filtro TCP per isolare la stretta di mano:**  
   ```plaintext
   tcp.flags.syn == 1
   ```

4️⃣ **Identificare i tre pacchetti della stretta di mano TCP:**  
   - **SYN** → Richiesta del client  
   - **SYN-ACK** → Risposta del server  
   - **ACK** → Conferma del client  

📸 **Scattare screenshot dell’handshake TCP su Wireshark.**

---

## 🔹 4. Esaminare i Dettagli dei Pacchetti

1️⃣ **Selezionare il primo pacchetto (SYN)**  
   - Identificare **porta di origine e destinazione**  
   - Verificare che il flag **SYN** sia impostato

2️⃣ **Selezionare il secondo pacchetto (SYN-ACK)**  
   - Controllare che i flag **SYN** e **ACK** siano impostati

3️⃣ **Selezionare il terzo pacchetto (ACK)**  
   - Controllare il **numero di conferma**

📸 **Scattare screenshot di ogni pacchetto analizzato.**

---

## 🔹 5. Visualizzare i Pacchetti con tcpdump

1️⃣ **Aprire un terminale e leggere il file pcap:**  
   ```bash
   tcpdump -r /home/analyst/capture.pcap
   ```

2️⃣ **Filtrare i primi 3 pacchetti TCP:**  
   ```bash
   tcpdump -r /home/analyst/capture.pcap -c 3
   ```

📸 **Screenshot dell’output di tcpdump.**

---

## 🔹 6. Conclusione

✔️ **Abbiamo analizzato il traffico TCP** e identificato la stretta di mano a tre vie  
✔️ **Abbiamo usato Wireshark per filtrare e interpretare i pacchetti**  
✔️ **Abbiamo confermato le informazioni con tcpdump**  
✔️ **Abbiamo imparato a leggere il traffico e analizzare il comportamento delle connessioni TCP**  

📌 **Prossimo passo:** approfondire l’analisi del traffico **UDP** con Wireshark! 🚀  

