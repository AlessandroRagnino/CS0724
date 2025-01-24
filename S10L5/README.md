# Creazione e Gestione di Gruppi in Windows Server 2022 🎯

## Obiettivo 🚀
Familiarizzare con la gestione dei gruppi di utenti in Windows Server 2022, creando gruppi, assegnando permessi specifici e verificandone il funzionamento in un contesto militare. 🪖

---

## Preparazione ⚙️
1. **Accesso al Server:**
   - Accedi a Windows Server 2022 con un account amministrativo. 👨‍💻
2. **Ambiente Configurato:**
   - **VM1:** Domain Controller (Windows Server 2022).
   - **VM2:** Client aggiunto al dominio (Windows 10 Pro N).

---

## Creazione dei Gruppi 👥
### Gruppi creati:
1. **CommandTeam**:
   - Ruolo: Comandanti e ufficiali superiori. 🪖
   - Permessi: Accesso completo a risorse strategiche e operative.
2. **Soldiers**:
   - Ruolo: Truppe operative. 🥾
   - Permessi: Accesso limitato alle risorse operative.

### Procedura 🛠️:
1. Apri **Active Directory Users and Computers**.
2. Naviga in `Esercito.local > Users`.
3. Crea i due gruppi:
   - Tipo: **Security**
   - Ambito: **Global**

---

## Creazione delle Cartelle Condivise 📂
### Cartelle create:
1. **StrategicPlans**:
   - Accesso esclusivo ai Comandanti. 🗂️
2. **Operations**:
   - Accesso condiviso per Comandanti e Soldati. 📜

### Procedura 🛠️:
1. Crea le cartelle:
   - `C:\MilitaryData\StrategicPlans`
   - `C:\MilitaryData\Operations`
2. Configura la condivisione:
   - Proprietà > **Sharing** > **Advanced Sharing** > Abilita condivisione. 🔗
3. Configura i permessi:
   - **StrategicPlans:** Full Control per `CommandTeam`, Negato per `Soldiers`.
   - **Operations:** Full Control per `CommandTeam`, Read per `Soldiers`.

---

## Assegnazione dei Permessi 🔒
1. Apri le proprietà delle cartelle condivise. 🖱️
2. Nella scheda **Security**, aggiungi i gruppi:
   - `CommandTeam`: Full Control per entrambe le cartelle. ✅
   - `Soldiers`: Read per *Operations*, accesso negato a *StrategicPlans*. 🚫

---

## Creazione degli Utenti di Prova 👤
### Utenti creati:
1. **Comandanti Utente:**
   - Gruppo: `CommandTeam`. 🪖
2. **Soldati Utente:**
   - Gruppo: `Soldiers`. 🥾

### Procedura 🛠️:
1. Apri **Active Directory Users and Computers**.
2. Naviga in `Esercito.local > Users`.
3. Crea i due utenti:
   - Nome, Cognome, Nome di accesso. 📝
   - Imposta una password temporanea. 🔑
4. Aggiungi gli utenti ai rispettivi gruppi. 🔗

---

## Verifica dei Permessi ✅
### Test eseguiti:
1. **Comandanti Utente:**
   - Verificato accesso completo a *StrategicPlans* e *Operations*. 🗂️✅
2. **Soldati Utente:**
   - Verificato accesso in sola lettura a *Operations*. 📜✅
   - Accesso negato a *StrategicPlans*. 🚫

### Risultati 📊:
- Gli utenti hanno ottenuto i permessi assegnati in base al gruppo.
- La configurazione funziona correttamente per entrambi i gruppi.

---

## Documentazione 📄
1. **Nomi dei Gruppi Creati:**
   - CommandTeam
   - Soldiers
2. **Permessi Assegnati:**
   - **CommandTeam:** Accesso completo a *StrategicPlans* e *Operations*.
   - **Soldiers:** Accesso in sola lettura a *Operations*, accesso negato a *StrategicPlans*.
3. **Passaggi Seguiti:**
   - Creazione dei gruppi.
   - Configurazione delle cartelle condivise.
   - Assegnazione dei permessi ai gruppi.
   - Creazione degli utenti e assegnazione ai gruppi.
   - Verifica dei permessi con utenti di prova.
4. **Problemi Riscontrati:**
   - **Errore nella creazione degli utenti:** Risolto verificando unicità dei nomi.
   - **Errore di rete:** Risolto configurando correttamente i permessi.

---

## Conclusione 🏁
- 🎯 Creazione di gruppi e utenti con ruoli specifici completata.
- 🔒 Configurazione permessi per protezione risorse.
- ✅ Test di verifica eseguiti con successo.

Questo progetto dimostra l'importanza della gestione centralizzata in Active Directory, replicabile in altri contesti aziendali o educativi. 🚀
