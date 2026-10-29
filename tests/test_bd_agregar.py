import pytest
from persistance.db import agregar_animal, obtener_animal, eliminar_animal

def test_agregar_animal():
    animal_id = agregar_animal(
        "Teodora", "Pinguino", 3, "Antartida"
    )
    try:
        animal = obtener_animal(animal_id)

        assert animal is not None
        assert animal["id"] == animal_id
        assert animal["nombre"] == "Teodora"
        assert animal["especie"] == "Pinguino"
        assert animal["edad"] == 3
        assert animal["habitat"] == "Antartida"

    finally:
        eliminar_animal(animal_id)


