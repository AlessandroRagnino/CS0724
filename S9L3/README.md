# Business Continuity & Disaster Recovery Analysis

## Scopo
Il seguente documento illustra il processo per calcolare le perdite annuali attese (**Annual Loss Expectancy - ALE**) su vari asset di una compagnia in caso di specifici eventi disastrosi. I calcoli sono effettuati sulla base dei dati forniti riguardanti il valore degli asset, il tasso di occorrenza annualizzato (**ARO**) e il fattore di esposizione (**Exposure Factor**).

---

## Dati di Base

### Tabella Asset e Valori
| Asset                | Valore     |
|----------------------|------------|
| Edificio primario    | 350.000 €  |
| Edificio secondario  | 150.000 €  |
| Datacenter           | 100.000 €  |

### Eventi e ARO
| Evento       | ARO (Rateo annualizzato) |
|--------------|--------------------------|
| Terremoto    | 1/30 = 0,0333           |
| Incendio     | 1/20 = 0,05             |
| Inondazione  | 1/50 = 0,02             |

### Tabella Exposure Factor
| Asset               | Terremoto | Incendio | Inondazione |
|---------------------|-----------|----------|-------------|
| Edificio primario   | 80%       | 60%      | 55%         |
| Edificio secondario | 80%       | 50%      | 40%         |
| Datacenter          | 95%       | 60%      | 35%         |

---

## Metodo di Calcolo

I calcoli sono basati sulle seguenti formule:

1. **Single Loss Expectancy (SLE):**
   ```
   SLE = Valore dell'asset × Exposure Factor
   ```

2. **Annual Loss Expectancy (ALE):**
   ```
   ALE = SLE × ARO
   ```

---

## Calcoli Dettagliati

### 1. Inondazione sull'edificio secondario
- **Valore:** 150.000 €
- **Exposure Factor:** 40% = 0,4
- **ARO:** 1/50 = 0,02

**SLE:**
```
SLE = 150.000 × 0,4 = 60.000 €
```

**ALE:**
```
ALE = 60.000 × 0,02 = 1.200 €
```

---

### 2. Terremoto sul datacenter
- **Valore:** 100.000 €
- **Exposure Factor:** 95% = 0,95
- **ARO:** 1/30 = 0,0333

**SLE:**
```
SLE = 100.000 × 0,95 = 95.000 €
```

**ALE:**
```
ALE = 95.000 × 0,0333 = 3.166,50 €
```

---

### 3. Incendio sull'edificio primario
- **Valore:** 350.000 €
- **Exposure Factor:** 60% = 0,6
- **ARO:** 1/20 = 0,05

**SLE:**
```
SLE = 350.000 × 0,6 = 210.000 €
```

**ALE:**
```
ALE = 210.000 × 0,05 = 10.500 €
```

---

### 4. Incendio sull'edificio secondario
- **Valore:** 150.000 €
- **Exposure Factor:** 50% = 0,5
- **ARO:** 1/20 = 0,05

**SLE:**
```
SLE = 150.000 × 0,5 = 75.000 €
```

**ALE:**
```
ALE = 75.000 × 0,05 = 3.750 €
```

---

### 5. Inondazione sull'edificio primario
- **Valore:** 350.000 €
- **Exposure Factor:** 55% = 0,55
- **ARO:** 1/50 = 0,02

**SLE:**
```
SLE = 350.000 × 0,55 = 192.500 €
```

**ALE:**
```
ALE = 192.500 × 0,02 = 3.850 €
```

---

### 6. Terremoto sull'edificio primario
- **Valore:** 350.000 €
- **Exposure Factor:** 80% = 0,8
- **ARO:** 1/30 = 0,0333

**SLE:**
```
SLE = 350.000 × 0,8 = 280.000 €
```

**ALE:**
```
ALE = 280.000 × 0,0333 = 9.324 €
```

---

## Risultati Finali
| Evento                     | Asset                | ALE (€)        |
|----------------------------|----------------------|----------------|
| Inondazione                | Edificio secondario  | 1.200          |
| Terremoto                  | Datacenter           | 3.166,50       |
| Incendio                   | Edificio primario    | 10.500         |
| Incendio                   | Edificio secondario  | 3.750          |
| Inondazione                | Edificio primario    | 3.850          |
| Terremoto                  | Edificio primario    | 9.324          |

---

## Conclusione
L'analisi quantitativa ha permesso di stimare le perdite annuali attese per ogni evento specifico e asset. Questi risultati possono essere utilizzati per priorizzare le misure di mitigazione dei rischi e garantire una maggiore continuità operativa.

---

**Autore:** [Nome Utente]  
**Data:** Gennaio 2025
