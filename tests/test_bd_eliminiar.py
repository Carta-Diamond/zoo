import pytest
from persistance.db import eliminar_animal

def test_eliminar_animal():
    # Llamar a la función eliminar_animal para eliminar un animal de la base de datos
    eliminar_animal(6)

    assert True  # Verificar que la función se ejecutó sin errores