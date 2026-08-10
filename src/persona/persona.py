from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class Persona:
    """Clase simple que representa a una persona."""
    nombre: str
    edad: int
    email: Optional[str] = None

    def saludar(self) -> str:
        """Devuelve un saludo personalizado."""
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

    def cumpleanos(self) -> None:
        """Incrementa la edad en 1 (cumpleaños)."""
        self.edad += 1

    def actualizar_email(self, nuevo_email: str) -> None:
        """Actualiza el email de la persona."""
        self.email = nuevo_email

    def __str__(self) -> str:
        return f"Persona(nombre={self.nombre}, edad={self.edad}, email={self.email})"
