from typing import List
from models.jugador import Jugador
from games.juegos import Juegos

class Menu:
    def __init__(self):
        # Inicializamos el jugador con datos vacíos
        self.jugador = None
        self.juegos = None

    def obtener_datos_jugador(self):
        """Método para obtener los datos iniciales del jugador"""
        print("\nDatos del jugador:")
        print("=======================")
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        descripcion = input("Descripción: ")
        numeroJugado = 3  # Valor por defecto

        # Creamos la instancia del jugador
        self.jugador = Jugador(nombre, direccion, telefono, descripcion, numeroJugado)
        # Inicializamos los juegos con el jugador
        self.juegos = Juegos(self.jugador)

    def mostrar_menu(self):
        """Método para mostrar el menú principal"""
        print("\n=======================")
        print("MENÚ DE JUEGOS")
        print("=======================")
        print("1. Par o impar")
        print("2. Juego Mad Libs")
        print("3. Contador de palabras")
        print("4. Información de la biografía")
        print("5. ¿Cuál es el acrónimo?")
        print("6. Piedra, Papel y tijera")
        print("7. Adivina el número")
        print("8. ¿Es palíndromo?")
        print("9. Calculador de pro")
        print("10. Extractor de correos electrónicos")
        print("11. Generador de letras")
        print("0. Salir")
        print("=======================")

    def ejecutar_opcion(self, opcion: int) -> bool:
        """
        Ejecuta la opción seleccionada del menú
        Retorna False si se debe salir del programa
        """
        if opcion == 0:
            print("¡Gracias por jugar!")
            return False
            
        opciones = {
            1: self.juegos.par_impar,
            2: self.juegos.mad_libs,
            3: self.juegos.contador_palabras,
            4: self.juegos.informacion_biografia,
            5: self.juegos.acronimo,
            6: self.juegos.piedra_papel_tijera,
            7: self.juegos.adivina_numero,
            8: self.juegos.es_palindromo,
            9: self.juegos.calculadora_pro,
            10: self.juegos.extractor_emails,
            11: self.juegos.generador_letras
        }

        if opcion in opciones:
            opciones[opcion]()
            return True
        else:
            print("Opción inválida")
            return True

    def iniciar(self):
        """Método principal que inicia el menú"""
        self.obtener_datos_jugador()
        
        while True:
            self.mostrar_menu()
            try:
                opcion = int(input("\nSeleccione una opción: "))
                if not self.ejecutar_opcion(opcion):
                    break
            except ValueError:
                print("Por favor, ingrese un número válido")

