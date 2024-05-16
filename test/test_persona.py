import pytest
from persona import Persona

class TestPersona:
    def test_prueba(self):

        assert 0 == 0
    def test_constructor(self):

        persona = Persona(nombre="Diego", edad=25)

        assert persona.dar_nombre() == "Diego"

        assert persona.dar_edad() == 25