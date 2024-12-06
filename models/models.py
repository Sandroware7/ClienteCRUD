class Client:
    def __init__(self, client_id, name, email, phone):
        self._id = client_id
        self._name = name
        self._email = email
        self._phone = phone

    def __str__(self):
        return f"{self._id} - {self._name} ({self._email}, {self._phone})"

    def to_dict(self):
        return {"id": self._id, "name": self._name, "email": self._email, "phone": self._phone}