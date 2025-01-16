# 🛡️ Guida alla Configurazione dei File di Log di Sicurezza su Windows

## 🎯 Obiettivo
Questa guida illustra come configurare e gestire i file di log di sicurezza su Windows. È pensata per principianti, con istruzioni semplici e dettagliate per ogni passaggio. 📝✨

---

## ✅ Requisiti
- 🖥️ Sistema operativo Windows (Home, Pro o Enterprise).
- 👩‍💻 Accesso come amministratore sul computer.

---

## 📚 Passaggi per Configurare i Log di Sicurezza

### 1️⃣ Accedere al Visualizzatore Eventi
1. Premi **Win + R** per aprire la finestra "Esegui". 🏃‍♂️
2. Digita `eventvwr` e premi **Invio**. ⌨️
3. Si aprirà la finestra del **Visualizzatore Eventi**. 👀

---

### 2️⃣ Navigare al Registro di Sicurezza
1. Nella barra laterale sinistra, espandi **Registri di Windows**. 📂
2. Clicca su **Sicurezza** per visualizzare i log relativi agli eventi di sicurezza. 🔒

---

### 3️⃣ Configurare le Proprietà del Registro
1. Nel pannello di destra, clicca su **Proprietà**. ⚙️
2. Configura:
   - **Dimensione massima del registro**: Imposta un valore adeguato (es. 10 MB). 📏
   - **Azione quando pieno**: Scegli tra:
     - 🔄 Sovrascrivere eventi più vecchi.
     - ❌ Non sovrascrivere eventi (richiede monitoraggio dello spazio).
3. Salva le modifiche e chiudi la finestra. 💾

---

### 4️⃣ Applicare un Filtro per Monitorare Eventi Specifici
1. Nel pannello di destra, clicca su **Filtra registro corrente**. 🔍
2. Configura:
   - **ID evento**: Inserisci uno o più codici (es. 4624 per accessi riusciti, 4625 per tentativi falliti). 🔢
   - **Parole chiave**: Seleziona "Audit riuscito" o "Audit fallito". ✅❌
3. Premi **OK** per applicare il filtro. ✔️

---

### 5️⃣ Configurare le Politiche di Auditing
#### Se il comando `secpol.msc` non è disponibile, utilizza `auditpol`:
1. Apri il Prompt dei Comandi come amministratore:
   - Premi **Win + R**, digita `cmd` e premi **Ctrl + Shift + Invio**. 🖱️
2. Abilita il monitoraggio degli accessi:
   ```cmd
   auditpol /set /category:"Logon/Logoff" /subcategory:"Logon" /success:enable /failure:enable
   ```
3. Verifica le modifiche:
   ```cmd
   auditpol /get /category:*
   ```
   Questo comando mostrerà tutte le categorie configurate. 📋

---

### 6️⃣ Testare la Configurazione
1. Effettua alcune azioni, come:
   - ✅ Accedere al sistema con successo.
   - ❌ Provare un accesso con credenziali errate.
2. Torna al Visualizzatore Eventi e verifica che gli eventi siano registrati correttamente nella sezione **Sicurezza**. 🔎

---

### 7️⃣ Esportare i Log
1. Nel pannello di destra, clicca su **Salva registro con nome**. 💾
2. Salva il registro come file `.evtx` in una posizione a tua scelta. 📂
3. Usa questo file per analisi future o per condividerlo. 🔄

---

## 🎉 Conclusione
Seguendo questa guida, hai configurato con successo i file di log di sicurezza su Windows. Ora sei in grado di monitorare gli eventi di accesso e identificare eventuali problemi di sicurezza sul sistema. 🚀💻

Se hai ulteriori domande o dubbi, non esitare a chiedere! 🧐😊