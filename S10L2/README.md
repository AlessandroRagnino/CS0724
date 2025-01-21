
# 🛠️ Esercizio: Gestione dei Permessi in Linux

Questo documento descrive i passaggi eseguiti per configurare e gestire i permessi di **lettura**, **scrittura** ed **esecuzione** su file e directory in un sistema Linux. 🐧

---

## 📋 Passaggi Eseguiti

### 1️⃣ Creazione di un File e di una Directory:
- Ho aperto il terminale e creato:
  - Un nuovo file chiamato `esercizio_file.txt` utilizzando il comando:
    ```bash
    touch esercizio_file.txt
    ```
    ✅ **Scopo:** Creare un file su cui testare i permessi.
  - Una nuova directory chiamata `esercizio_permessi` utilizzando il comando:
    ```bash
    mkdir esercizio_permessi
    ```
    ✅ **Scopo:** Creare una directory per simulare permessi su cartelle condivise.

---

### 2️⃣ Verifica dei Permessi Attuali:
- Ho controllato i permessi iniziali del file e della directory utilizzando:
  ```bash
  ls -l esercizio_file.txt
  ls -ld esercizio_permessi
  ```
  🔎 **Risultato:** I permessi di default sono stati visualizzati correttamente.

---

### 3️⃣ Modifica dei Permessi:
- Ho modificato i permessi usando il comando `chmod`:
  - **File `esercizio_file.txt`:**
    ```bash
    chmod u=rw,g=r,o=r esercizio_file.txt
    ```
    🔐 **Permessi Assegnati:** Lettura e scrittura per il proprietario, solo lettura per il gruppo e altri.

  - **Directory `esercizio_permessi`:**
    ```bash
    chmod u=rwx,g=rx,o=rx esercizio_permessi
    ```
    🔐 **Permessi Assegnati:** Lettura, scrittura ed esecuzione per il proprietario; lettura ed esecuzione per il gruppo e gli altri.

- Ho verificato i nuovi permessi con:
  ```bash
  ls -l esercizio_file.txt
  ls -ld esercizio_permessi
  ```
  📊 **Conferma:** I nuovi permessi sono stati applicati correttamente.

---

### 4️⃣ Test dei Permessi:
- **Test sul File `esercizio_file.txt`:**
  - Ho provato a scrivere nel file:
    ```bash
    echo "Test dei permessi" > esercizio_file.txt
    ```
    ✅ **Risultato Atteso:** Il proprietario è stato in grado di scrivere.

- **Test sulla Directory `esercizio_permessi`:**
  - Ho provato a creare un nuovo file nella directory:
    ```bash
    touch esercizio_permessi/nuovo_file.txt
    ```
    ✅ **Risultato Atteso:** Il proprietario ha potuto creare un nuovo file, mentre altri utenti con permessi limitati non possono farlo.

---

## 📝 Relazione

### 🔧 Scelte di Permessi:
1. **File `esercizio_file.txt`:**
   - **Motivazione:** Ho scelto i permessi `u=rw,g=r,o=r` per consentire al proprietario di leggere e scrivere nel file, mentre gli altri utenti possono solo leggerlo. Questo è utile per file condivisi che devono essere modificati solo dal proprietario ma letti dagli altri utenti.

2. **Directory `esercizio_permessi`:**
   - **Motivazione:** Ho scelto i permessi `u=rwx,g=rx,o=rx` per permettere al proprietario di leggere, scrivere ed eseguire nella directory, mentre gli altri utenti possono solo leggere il contenuto e accedervi. Questo è utile per directory condivise per la lettura senza concedere permessi di modifica.

---

### 🔍 Analisi dei Risultati:
- **File `esercizio_file.txt`:** Ha funzionato come previsto: il proprietario ha potuto modificarlo, mentre altri utenti senza permessi di scrittura non potevano farlo.
- **Directory `esercizio_permessi`:** Il proprietario ha potuto creare nuovi file, mentre gli altri utenti potevano solo visualizzarne il contenuto.

---

## 🚀 Conclusioni:
Grazie alla gestione dei permessi, è possibile controllare in modo dettagliato l'accesso ai file e alle directory in Linux, garantendo sicurezza e flessibilità. 🛡️ Questo esercizio mi ha permesso di comprendere meglio il funzionamento del comando `chmod` e dei permessi.

---

🎉 **Esercizio Completato con Successo!**
