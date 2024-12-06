def find_client_by_id(clients, client_id):
    """Busca un cliente por ID."""
    for client in clients:
        if client["id"] == client_id:
            return client
    return None

def add_client(clients, new_client):
    """Añade un nuevo cliente si el ID no está duplicado."""
    if find_client_by_id(clients, new_client["id"]):
        raise ValueError("El ID ya existe.")
    clients.append(new_client)
    return "Cliente agregado exitosamente."

def update_client(clients, client_id, updated_data):
    """Actualiza los datos de un cliente existente."""
    client = find_client_by_id(clients, client_id)
    if not client:
        raise ValueError("Cliente no encontrado.")
    client.update(updated_data)
    return "Cliente actualizado exitosamente."

def delete_client(clients, client_id):
    """Elimina un cliente existente."""
    client = find_client_by_id(clients, client_id)
    if not client:
        raise ValueError("Cliente no encontrado.")
    clients.remove(client)
    return "Cliente eliminado exitosamente."