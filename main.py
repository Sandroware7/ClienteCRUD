from iu.menu import display_menu
from database.data import clients
from utils.utils import add_client, find_client_by_id, update_client, delete_client

def main():
    while True:
        option = display_menu()
        if option == "1":
            for client in clients:
                print(client)
        elif option == "2":
            client_id = input("Ingrese el ID del cliente: ")
            client = find_client_by_id(clients, client_id)
            print(client if client else "Cliente no encontrado.")
        elif option == "3":
            try:
                new_client = {
                    "id": input("ID: "),
                    "name": input("Nombre: "),
                    "email": input("Correo: "),
                    "phone": input("Teléfono: "),
                }
                print(add_client(clients, new_client))
            except ValueError as e:
                print(e)
        elif option == "4":
            client_id = input("Ingrese el ID del cliente a actualizar: ")
            updated_data = {}
            updated_data["name"] = input("Nuevo nombre (dejar en blanco para mantener): ")
            updated_data["email"] = input("Nuevo correo (dejar en blanco para mantener): ")
            updated_data["phone"] = input("Nuevo teléfono (dejar en blanco para mantener): ")
            updated_data = {k: v for k, v in updated_data.items() if v}  # Filtrar valores vacíos
            try:
                print(update_client(clients, client_id, updated_data))
            except ValueError as e:
                print(e)
        elif option == "5":
            client_id = input("Ingrese el ID del cliente a eliminar: ")
            try:
                print(delete_client(clients, client_id))
            except ValueError as e:
                print(e)
        elif option == "6":
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()