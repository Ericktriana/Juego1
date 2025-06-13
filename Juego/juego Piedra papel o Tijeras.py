import random

opciones = ["piedra", "papel", "tijeras"]

while True:
    print("\n--- Piedra, Papel o Tijeras ---")
    usuario = input("Elige (piedra, papel, tijeras o salir): ").lower()

    if usuario == "salir":
        print("¡Hasta pronto!")
        break
    if usuario not in opciones:
        print("Opción inválida.")
        continue

    compu = random.choice(opciones)
    print(f"Computadora eligió: {compu}")

    if usuario == compu:
        print("¡Empate!")
    elif (usuario == "piedra" and compu == "tijeras") or \
         (usuario == "papel" and compu == "piedra") or \
         (usuario == "tijeras" and compu == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste.")