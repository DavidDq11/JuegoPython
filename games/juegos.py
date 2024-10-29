# Importamos las librerías necesarias
import random  # Para juegos que necesitan números aleatorios
import re      # Para el extractor de correos
from typing import List  # Para tipos más complejos
from models.jugador import Jugador  # Importamos nuestra clase Jugador

class Juegos:
    """
    Clase que contiene todos los minijuegos disponibles.
    Cada juego es un método diferente.
    """
    def __init__(self, jugador: Jugador):
        # Guardamos la referencia al jugador actual
        self.jugador = jugador

    # Empecemos con el primer juego: Par o Impar
    def par_impar(self) -> None:
        """
        Juego que determina si un número es par o impar
        -> None significa que no retorna nada (como void en TypeScript)
        """
        numero = int(input("Ingresa un número: "))
        # Usamos un operador ternario - similar a TypeScript pero con diferente sintaxis
        resultado = "par" if numero % 2 == 0 else "impar"
        print(f"El número {numero} es {resultado}")

    def mad_libs(self) -> None:
        """
        Juego de crear historias con palabras proporcionadas por el usuario
        """
        print("Juego Mad Libs - Completa la historia!")
        # En Python, las variables son directamente accesibles en los f-strings
        nombre = input("Ingresa un nombre: ")
        lugar = input("Ingresa un lugar: ")
        verbo = input("Ingresa un verbo: ")
        print(f"{nombre} fue a {lugar} y decidió {verbo} todo el día!")

    def contador_palabras(self) -> None:
        """
        Cuenta las palabras en un texto
        split() divide el texto en palabras (similar a split(' ') en TypeScript)
        """
        texto = input("Ingresa un texto: ")
        palabras = len(texto.split())
        print(f"El texto tiene {palabras} palabras")

    def informacion_biografia(self) -> None:
        """
        Muestra la información del jugador actual
        Usa self.jugador para acceder a los datos
        """
        print(f"""
        Biografía de {self.jugador.nombre}
        ============================
        Dirección: {self.jugador.direccion}
        Teléfono: {self.jugador.telefono}
        Descripción: {self.jugador.descripcion}
        """)

    def acronimo(self) -> None:
        """
        Crea un acrónimo a partir de una frase
        Usa comprensión de lista (similar a map en TypeScript)
        """
        frase = input("Ingresa una frase para convertir en acrónimo: ")
        # Esta línea es equivalente a:
        # let acronimo = frase.split(' ').map(palabra => palabra[0].toUpperCase()).join('');
        acronimo = ''.join(palabra[0].upper() for palabra in frase.split())
        print(f"El acrónimo es: {acronimo}")

    def piedra_papel_tijera(self) -> None:
        """
        Juego clásico de piedra, papel o tijera
        Usa random.choice para la elección de la computadora
        """
        opciones = ['piedra', 'papel', 'tijera']
        computadora = random.choice(opciones)
        jugador = input("Elige piedra, papel o tijera: ").lower()
        
        if jugador == computadora:
            print("¡Empate!")
        elif(jugador == 'piedra' and computadora == 'tijera') or \
            (jugador == 'papel' and computadora == 'piedra') or \
            (jugador == 'tijera' and computadora == 'papel'):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")
    
    def adivina_numero(self) -> None:
        """
        Juego de adivinar un número
        Usa random.randint para generar un número aleatorio
        """
        numero_secreto = random.randint(1, 100)
        intentos = 0
        
        while True:  # Bucle infinito (similar a while(true) en TypeScript)
            intento = int(input("Adivina el número (1-100): "))
            intentos += 1  # Incremento (no existe ++ en Python)
            
            if intento == numero_secreto:
                print(f"¡Correcto! Lo adivinaste en {intentos} intentos")
                break  # Sale del bucle
            elif intento < numero_secreto:
                print("El número es mayor")
            else:
                print("El número es menor")

    def es_palindromo(self) -> None:
        """
        Verifica si una palabra o frase es palíndromo
        Usa métodos de string y comprensión de lista
        """
        texto = input("Ingresa una palabra o frase: ").lower()
        # Elimina espacios y caracteres especiales
        texto = ''.join(c for c in texto if c.isalnum())
        # texto[::-1] invierte la cadena (similar a reverse() en TypeScript)
        es_palindromo = texto == texto[::-1]
        print(f"{'¡Es un palíndromo!' if es_palindromo else 'No es un palíndromo'}")

    def calculadora_pro(self) -> None:
        """
        Calculadora que evalúa expresiones matemáticas
        Usa eval() con try/except para manejar errores
        """
        try:
            expresion = input("Ingresa una expresión matemática: ")
            resultado = eval(expresion)  # eval es peligroso en producción
            print(f"Resultado: {resultado}")
        except:
            print("Expresión inválida")
    
    def extractor_emails(self) -> None:
        """10
        
        Extrae correos electrónicos de un texto
        Usa expresiones regulares (similar a RegExp en TypeScript)
        """
        texto = input("Ingresa un texto que contenga correos electrónicos: ")
        patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(patron, texto)
        print("Correos encontrados:")
        for email in emails:  # for...of en TypeScript
            print(email)

    def generador_letras(self) -> None:
        """
        Genera una cadena aleatoria de letras
        Usa random.choice y join
        """
        longitud = int(input("Ingresa la longitud de la cadena a generar: "))
        # Comprensión de lista con random.choice
        letras = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') 
                        for _ in range(longitud))
        print(f"Cadena generada: {letras}")
