from .base import IdClass

class Studio(IdClass):
    def __init__(self, id, name, address):
        super().__init__(id)
        self._name = self._validateName(name)
        self._address = self._validateAddress(address)

    def _validateName (self, name):
        name = str(name).strip()
        if len(name) > 50:
            raise ValueError("Name must be 50 characters or fewer.")
        return name
    
    def _validateAddress(self, address):
        address = str(address).strip()
        if len(address) > 50:
            raise ValueError("Address must be 50 characters or fewer.")
        return address
    
    def __str__ (self):
        return  f"Nombre: {self._name}" \
                f"Dirección: {self._address}"