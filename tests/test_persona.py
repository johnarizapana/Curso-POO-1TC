from persona import Persona


def test_saludo_y_cumpleanos():
    p = Persona("Ana", 25, None)
    assert "Ana" in p.saludar()
    prev = p.edad
    p.cumpleanos()
    assert p.edad == prev + 1
