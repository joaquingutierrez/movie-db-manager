from .base import IdClass
from datetime import datetime

class Star(IdClass):
    def __init__ (self, name, address, gender, birth_date):
        self.name = self._validateName(name)
        self.address = self._validateAddress(address)
        self.gender = self._validateGender(gender)
        self.birth_date = self._validateBirthDate(birth_date)

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
    
    def _validateGender(self, gender):
        gender = str(gender).strip().upper()
        if gender not in ["M", "F"]:
            raise ValueError("Gender must be M or F.")
        return gender
    
    def _validateBirthDate(self, birth_date):
        try:
            birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Birth date must be in the format DD-MM-YYYY.")
        
        if birth_date > datetime.now():
            raise ValueError("Birth date cannot be in the future.")
        
        return birth_date
    
    def __str__(self):
        return  f"Nombre: {self.name} \n" \
                f"Direccion: {self.address}\n" \
                f"Género: {self.gender}\n" \
                f"Fecha de Nacimiento: {self.birth_date.strftime("%d-%m-%Y")}"
