import random
#Definicion de la funcion menu principal
def main_menu():
    print("1- Adivina numero")
    print("2- piedra papel, tijera")
    print("3- EL penjat")
    print("4- Salir")
    menu = input("Elije un juego: ")
    return menu
#Definicion de la funcion adivina numero
def adivina_numero():
                numero_secreto = random.randint(1, 10)
                intentos = 3
                while intentos > 0:
                    try:
                        intento = int(input("Adivina el numero del 1 al 10: "))
                        if intento == numero_secreto:
                            print("Has adivinado el numero.")
                            return
                        elif intento < numero_secreto:
                            print("El numero es mayor.")
                        elif intento > 10:
                            print("Por favor, introduce un número del 1 al 10.")
                        else:
                            print("El numero es menor.")
                        intentos -= 1
                    except ValueError:
                        print("Por favor, introduce un número válido.")
                print(f"Lo siento, no has adivinado el numero. Era {numero_secreto}.")
#Definicion de la funcion PIedra papel tijera
def piedra_papel_tijera():
                opciones = ["piedra", "papel", "tijera"]
                puntos_usuario = 0
                puntos_maquina = 0

                while puntos_usuario < 3 and puntos_maquina < 3:
                    eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
                    if eleccion_usuario not in opciones:
                        print("Opcion no valida. Por favor, elige piedra, papel o tijera.")
                        continue

                    eleccion_maquina = random.choice(opciones)
                    print(f"La maquina eligió: {eleccion_maquina}")

                    if eleccion_usuario == eleccion_maquina:
                        print("Empate.")
                    elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or \
                         (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or \
                         (eleccion_usuario == "tijera" and eleccion_maquina == "papel"):
                        print("Ganas esta ronda.")
                        puntos_usuario += 1
                    else:
                        print("La maquina gana esta ronda.")
                        puntos_maquina += 1

                    print(f"Puntuación - Usuario: {puntos_usuario}, maquina: {puntos_maquina}")

                if puntos_usuario == 3:
                    print("¡Felicidades! Has ganado el juego. GOAT")
                else:
                    print("La maquina ha ganado el juego. Loser")

#Definicion de la funcion el ahorcado
def el_ahorcado():
                try:
                    with open("Palabras.txt", "r") as file:
                        palabras = file.read().splitlines()
                except FileNotFoundError:
                    print("El archivo Palabras.txt no se encuentra.")
                    return

                if len(palabras) < 30:
                    print("El archivo debe contener al menos 30 palabras.")
                    return

                palabra_secreta = random.choice(palabras).lower()
                letras_adivinadas = ["_"] * len(palabra_secreta)
                intentos = 2
                letras_usadas = set()

                print(f"La palabra tiene {len(palabra_secreta)} letras: {' '.join(letras_adivinadas)}")

                while intentos > 0 and "_" in letras_adivinadas:
                    letra = input("Introduce una letra: ").lower()

                    if not letra.isalpha() or len(letra) != 1:
                        print("Por favor, introduce una única letra.")
                        continue

                    if letra in letras_usadas:
                        print("Ya has usado esa letra. Intenta con otra.")
                        continue

                    letras_usadas.add(letra)

                    if letra in palabra_secreta:
                        for i, char in enumerate(palabra_secreta):
                            if char == letra:
                                letras_adivinadas[i] = letra
                        print(f"¡Bien hecho! {' '.join(letras_adivinadas)}")
                    else:
                        intentos -= 1
                        print(f"Letra incorrecta. Te quedan {intentos} intentos.")

                if "_" not in letras_adivinadas:
                    print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
                else:
                    print(f"Lo siento, te has quedado sin intentos. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    while True:
        menu = main_menu()
        if menu == '1':
            print("Adivina numero")
            adivina_numero()
        elif menu == '2':
            piedra_papel_tijera()
        elif menu == '3':
            el_ahorcado()
        elif menu == '4':
            print("Saliendo del menu...")
            break
        else:
            print("Opcion Incorrecta")