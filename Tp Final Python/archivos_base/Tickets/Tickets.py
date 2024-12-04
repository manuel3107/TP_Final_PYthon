import pickle
import random
import os

def clear_screen():
    os.system("clear")

def generar_numero_ticket():
    return random.randint(1000, 9999)

def alta_ticket(tickets):
    clear_screen()
    print("=== Alta Ticket ===")
    nombre = input("Nombre: ")
    sector = input("Sector: ")
    asunto = input("Asunto: ")
    problema = input("Problema: ")
    
    numero_ticket = generar_numero_ticket()
    ticket = {
        "numero": numero_ticket,
        "nombre": nombre,
        "sector": sector,
        "asunto": asunto,
        "problema": problema
    }
    
    tickets[numero_ticket] = ticket
    print("\nTicket creado:")
    print(ticket)
    print("Recuerda tu número de ticket:", numero_ticket)
    
    crear_otro = input("\n¿Deseas crear otro ticket? (s/n): ")
    if crear_otro.lower() == 's':
        alta_ticket(tickets)

def leer_ticket(tickets):
    clear_screen()
    print("=== Leer Ticket ===")
    numero_ticket = int(input("Número de ticket: "))
    
    if numero_ticket in tickets:
        print("\nTicket encontrado:")
        print(tickets[numero_ticket])
    else:
        print("Ticket no encontrado.")
    
    leer_otro = input("\n¿Deseas leer otro ticket? (s/n): ")
    if leer_otro.lower() == 's':
        leer_ticket(tickets)

def guardar_tickets(tickets, filename):
    with open(filename, "wb") as f:
        pickle.dump(tickets, f)

def cargar_tickets(filename):
    if os.path.isfile(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    return {}

def main():
    filename = "tickets.pkl"
    tickets = cargar_tickets(filename)

    while True:
        clear_screen()
        print("=== Menú ===")
        print("1. Alta Ticket")
        print("2. Leer Ticket")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            alta_ticket(tickets)
            guardar_tickets(tickets, filename)
        elif opcion == '2':
            leer_ticket(tickets)
        elif opcion == '3':
            confirmacion = input("¿Estás seguro de que deseas salir? (s/n): ")
            if confirmacion.lower() == 's':
                print("Saliendo del programa...")
                break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()