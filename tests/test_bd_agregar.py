import pytest
from persistance.db import agregar_animal

def test_agregar_animal():
    # Llamar a la función agregar_animal para agregar un animal a la base de datos
    agregar_animal("Simba", "León", 5, "Savana")

    assert True  # Verificar que la función se ejecutó sin errores  

