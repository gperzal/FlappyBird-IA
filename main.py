from game import Game
from game_AI import Game_AI, Bird_AI


def main_menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Jugar al juego como usuario")
        print("2. Entrenar la IA")
        print("3. Ver jugar a la IA")
        print("4. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            print("\nControles:")
            print("- ESPACIO: Saltar/Iniciar")
            print("- P: Pausar/Reanudar el juego")
            print("- ESC/CERRAR VENTANA: Salir")

            input("Presiona Enter para comenzar...")
            game = Game()
            game.play()

        elif choice == "2":
            game = Game_AI()
            n_generations = int(
                input("Ingrese el número de generaciones para el entrenamiento: "))
            n_birds = int(
                input("Ingrese el número de pájaros por generación: "))
            limit_score = int(
                input("Ingrese el puntaje límite para cada pájaro: "))
            game.train(n_generations=n_generations, n_birds=n_birds,
                       limit_score=limit_score, draw=False)

        elif choice == "3":
            print("\nControles:")
            print("- ESPACIO: Iniciar")
            print("- P: Pausar/Reanudar el juego")
            print("- ESC/CERRAR VENTANA: Salir")

            input("Presiona Enter para continuar...")
            ia_menu()

        elif choice == "4":
            print("Saliendo del juego...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def ia_menu():
    print("\n=== Seleccione el Nivel de la IA ===")
    print("1. Novato")
    print("2. Principiante")
    print("3. Intermedio")
    print("4. Avanzado")
    print("5. Experto")
    print("6. Volver al Menú Principal")

    level_choice = input("Seleccione un nivel: ")
    model_files = {
        "1": "models/best_7.pkl",
        "2": "models/best_15.pkl",
        "3": "models/best_39.pkl",
        "4": "models/best_61.pkl",
        "5": "models/best_100.pkl"
    }

    if level_choice in model_files:
        bird = Bird_AI()
        bird.load_model(model_files[level_choice])
        game = Game_AI()
        game.play_AI(bird)

    elif level_choice == "6":
        print("Volviendo al menú principal...")

    else:
        print("Opción no válida. Por favor, seleccione un nivel válido.")


if __name__ == '__main__':
    main_menu()
