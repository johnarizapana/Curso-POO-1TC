from persona import Persona


def main() -> None:
    p = Persona("Juan", 30, "juan@example.com")
    print(p.saludar())
    print(p)
    p.cumpleanos()
    print(f"Después del cumpleaños: {p}")


if __name__ == "__main__":
    main()
