
# **Report di Scansione di Rete**

## **Host 1: Metasploitable**
- **IP**: `192.168.50.101`  
- **Sistema Operativo**: **Linux 2.6.X (General Purpose)**  
- **MAC Address**: `08:00:27:4D:36:7D`  
- **Porte Aperte e Servizi in Ascolto**:  
  - **Porta 21 (FTP)**: vsftpd 2.3.4  
  - **Porta 22 (SSH)**: OpenSSH 4.7p1  
  - **Porta 23 (Telnet)**: Servizio generico  
  - **Porta 80 (HTTP)**: Apache 2.2.8 (Debian)  
  - **Porta 3306 (MySQL)**: MySQL 5.x  
  - **Porta 139/445 (NetBIOS/SMB)**: Samba 3.x  

---

## **Host 2: Windows XP**
- **IP**: `192.168.50.102`  
- **Sistema Operativo**: **Windows XP SP2/SP3**  
- **MAC Address**: `08:00:27:5C:8D:1C`  
- **Porte Aperte e Servizi in Ascolto**:  
  - **Porta 139 (NetBIOS-SSN)**: Microsoft Windows NetBIOS-SSN  
  - **Porta 445 (Microsoft-DS)**: Microsoft Windows XP Microsoft-DS  
- **Service Info**:  
  - **OSs**: Windows, Windows XP  
  - **CPE**: `cpe:/o:microsoft:windows`, `cpe:/o:microsoft:windows_xp`  

---

## **🔍 Scansione del Target: Metasploitable**

### **1. Rilevamento del Sistema Operativo**
- **Comando**:  
  ```bash
  nmap -O 192.168.50.101
  ```
- **Risultati**:  
  - Sistema Operativo Rilevato: **Linux 2.6.X**  
  - MAC Address: `08:00:27:4D:36:7D`  
  - Tipo di Dispositivo: **General Purpose**  

---

### **2. Scansione SYN**
- **Comando**:  
  ```bash
  nmap -sS 192.168.50.101
  ```
- **Risultati**:  
  - Porte Aperte (principali):  
    - 21 (FTP)  
    - 22 (SSH)  
    - 23 (Telnet)  
    - 80 (HTTP)  
    - 3306 (MySQL)  

> **Nota**: La scansione SYN è più rapida e discreta rispetto a una scansione TCP completa, poiché non termina il processo di handshake.

---

### **3. Scansione TCP Completa**
- **Comando**:  
  ```bash
  nmap -sT 192.168.50.101
  ```
- **Risultati**:  
  - Porte Aperte: **Uguali alla scansione SYN**  
  - **Differenza Principale**:  
    La scansione TCP completa esegue il **3-way handshake**, risultando più rilevabile nei log del target rispetto alla scansione SYN.

---

### **4. Rilevamento delle Versioni**
- **Comando**:  
  ```bash
  nmap -sV 192.168.50.101
  ```
- **Risultati**:  
  - Servizi Rilevati:  
    - **SSH**: OpenSSH 4.7p1  
    - **MySQL**: Versione 5.x  
    - **Server Web Apache**  

---

## **🖥️ Scansione del Target: Windows XP**

### **1. Rilevamento del Sistema Operativo**
- **Comando**:  
  ```bash
  sudo nmap -O 192.168.50.102
  ```
- **Risultati**:  
  - Sistema Operativo Rilevato: **Windows XP SP2/SP3 (97%)**  
  - Porte Aperte:  
    - **139 (NetBIOS-SSN)**  
    - **445 (Microsoft-DS)**  

---

### **Osservazioni**:
- **Nmap** ha fornito diverse possibili corrispondenze, ma con una probabilità elevata di essere **Windows XP SP2/SP3**.  
- Questi servizi, in particolare NetBIOS e SMB, potrebbero essere soggetti a vulnerabilità note (es. EternalBlue).

---

## **Conclusione**
Le scansioni hanno individuato **due host attivi** sulla rete `192.168.50.0/24`:  
1. **Metasploitable**: Sistema vulnerabile per esercitazioni di penetration testing, con numerosi servizi esposti.  
2. **Windows XP**: Sistema non più supportato e potenzialmente vulnerabile, con servizi SMB e NetBIOS che potrebbero essere sfruttati.

---
