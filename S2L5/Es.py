import datetime 

def assistente_virtuale(comando):
    if comando == "Qual è la data di oggi?":
        oggi = datetime.datetime.today()  # Correzione del metodo
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando() == "Che ore sono?":
        ora_attuale = datetime.datetime.now().time()  # Corretto per ottenere l'ora attuale
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")  # Correzione nel formato
    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."

    return risposta 

while True:
    comando_utente = input("Cosa vuoi sapere? ")
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break 
    else:
        print(assistente_virtuale(comando_utente))
