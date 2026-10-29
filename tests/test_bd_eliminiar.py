import pytest
from persistance.db import agregar_animal, obtener_animal, eliminar_animal


def test_eliminar_animal():
    animal_id = agregar_animal(
        "PruebaEliminar", "Tigre", 4, "Selva"
    )

    assert obtener_animal(animal_id) is not None

    eliminar_animal(animal_id)

    animal = obtener_animal(animal_id)

    assert animal is None
