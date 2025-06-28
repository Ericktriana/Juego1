import random

opciones = ["piedra", "papel", "tijeras"]
historial_total = []
ultima_partida = []

def mostrar_menu_principal():
    while True:
        print("\n🎮 MENÚ PRINCIPAL")
        print("1. Jugar")
        print("2. Reglas")
        print("3. Salir")
        op = input("Opción: ")
        if op == "1":
            menu_juego()
        elif op == "2":
            print("\n📜 Reglas:")
            print("- Piedra gana a Tijeras")
            print("- Tijeras gana a Papel")
            print("- Papel gana a Piedra\n")
        elif op == "3":
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida.")

def menu_juego():
    while True:
        print("\n🕹️ MENÚ DE JUEGO")
        print("1. Solo jugador")
        print("2. Contra la computadora")
        print("3. Multijugador")
        print("4. Ver estadísticas generales")
        print("5. Volver al menú principal")
        op = input("Opción: ")

        if op == "1" or op == "2":
            nombre = input("Nombre del jugador: ")
            jugar_partidas(nombre, "Computadora", True)
        elif op == "3":
            j1 = input("Nombre del jugador 1: ")
            j2 = input("Nombre del jugador 2: ")
            jugar_partidas(j1, j2, False)
        elif op == "4":
            ver_estadisticas(historial_total)
        elif op == "5":
            break
        else:
            print("Opción inválida.")

def jugar_partidas(j1, j2, contra_pc):
    partidas = []
    modo = input("¿Deseas definir cuántas partidas jugar? (si/no): ").lower()
    num = int(input("¿Cuántas?: ")) if modo == "si" else None
    count = 0

    while True:
        if num and count >= num:
            break
        print(f"\n⚔️ Partida {count + 1}")
        jugada1 = pedir_jugada(j1)
        jugada2 = random.choice(opciones) if contra_pc else pedir_jugada(j2)
        print(f"{j2} eligió: {jugada2}")

        ganador = evaluar(j1, j2, jugada1, jugada2)
        resultado = (j1, jugada1, j2, jugada2, ganador)
        partidas.append(resultado)
        historial_total.append(resultado)
        ultima_partida = [resultado]
        count += 1

        if not num:
            while True:
                print("\n¿Continuar?")
                print("1. Jugar otra partida")
                print("2. Ver estadística de la última partida")
                print("3. Salir del modo de juego")
                elec = input("Opción: ")
                if elec == "1":
                    break
                elif elec == "2":
                    ver_estadisticas(ultima_partida)
                elif elec == "3":
                    ver_estadisticas(partidas)
                    return
                else:
                    print("Opción inválida.")
    ver_estadisticas(partidas)

def pedir_jugada(jugador):
    while True:
        jugada = input(f"{jugador}, elige piedra, papel o tijeras: ").lower()
        if jugada in opciones:
            return jugada
        print("Jugada inválida.")

def evaluar(j1, j2, jg1, jg2):
    if jg1 == jg2:
        print("¡Empate!")
        return "Empate"
    gana1 = (jg1 == "piedra" and jg2 == "tijeras") or \
            (jg1 == "tijeras" and jg2 == "papel") or \
            (jg1 == "papel" and jg2 == "piedra")
    print(f"¡{j1 if gana1 else j2} gana esta ronda!")
    return j1 if gana1 else j2

def ver_estadisticas(lista):
    if not lista:
        print("No hay partidas registradas.")
        return

    print("\n📊 RESUMEN:")
    total = len(lista)
    print(f"\nNúmero de partidas realizadas: {total}\n")

    resumen = {}
    jg1 = lista[0][0]
    jg2 = lista[0][2]

    for i, (j1, jg1, j2, jg2, ganador) in enumerate(lista, 1):
        if ganador == "Empate":
            resultado_j1 = "empato"
            resultado_j2 = "empato"
        elif ganador == j1:
            resultado_j1 = "gano"
            resultado_j2 = "perdió"
        else:
            resultado_j1 = "perdió"
            resultado_j2 = "gano"

        print(f"Partida {i}: {j1} {resultado_j1} - {j2} {resultado_j2}")

        # Inicializar estadísticas si no existen
        for jugador in [j1, j2]:
            if jugador not in resumen:
                resumen[jugador] = {"gana": 0, "pierde": 0, "empata": 0}

        # Sumar estadísticas
        if ganador == "Empate":
            resumen[j1]["empata"] += 1
            resumen[j2]["empata"] += 1
        elif ganador == j1:
            resumen[j1]["gana"] += 1
            resumen[j2]["pierde"] += 1
        else:
            resumen[j2]["gana"] += 1
            resumen[j1]["pierde"] += 1

    print("\n📈 ESTADÍSTICAS:")
    for jugador, stats in resumen.items():
        print(f"{jugador}: gano {stats['gana']} partidas, perdió {stats['pierde']} partidas, empato {stats['empata']} partidas")
mostrar_menu_principal()