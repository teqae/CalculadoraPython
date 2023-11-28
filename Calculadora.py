from colorama import init, Fore, Style

# Inicializar colorama para sistemas Windows
init(autoreset=True)

# Funciones para operaciones matemáticas
# (Manteniendo las funciones definidas en ejemplos anteriores)

# Función principal de la calculadora
def calculadora():
    print("\n" * 2)
    print(Style.BRIGHT + Fore.BLUE + " " * 50 + "Calculadora Avanzada por TEQAE" + " " * 50)
    print(" " * 30 + Fore.BLUE + "╔═══════════════════════════════════════════════════════════════════╗")
    print(" " * 30 + Fore.BLUE + "║" + " " * 18 + Fore.YELLOW + "Bienvenido a la Calculadora" + " " * 17 + Fore.BLUE + "     ║")
    print(" " * 30 + Fore.BLUE + "║" + " " * 10 + Fore.YELLOW + "            Realice sus operaciones matemáticas" + " " * 10 + Fore.BLUE + "║")
    print(" " * 30 + Fore.BLUE + "╠═══════════════════════════════════════════════════════════════════╣")
    
    while True:
        print(Fore.CYAN + "\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Salir")
        
        opcion = input(Fore.YELLOW + "Seleccione la operación que desea realizar (1-6): ")
        
        if opcion == '6':
            print(Fore.GREEN + "\n¡Gracias por usar la calculadora de TEQAE! ¡Hasta luego!")
            break
        
        if opcion in ('1', '2', '3', '4', '5'):
            num1 = float(input(Fore.YELLOW + "Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            print(Fore.CYAN + "----------------------------------------------")
            
            if opcion == '1':
                print(Fore.MAGENTA + "Resultado:", suma(num1, num2))
            elif opcion == '2':
                print(Fore.MAGENTA + "Resultado:", resta(num1, num2))
            elif opcion == '3':
                print(Fore.MAGENTA + "Resultado:", multiplicacion(num1, num2))
            elif opcion == '4':
                print(Fore.MAGENTA + "Resultado:", division(num1, num2))
            elif opcion == '5':
                print(Fore.MAGENTA + "Resultado:", potencia(num1, num2))
                
            print(Fore.CYAN + "----------------------------------------------")
        else:
            print(Fore.RED + "Opción no válida. Por favor, seleccione una opción válida (1-6).")

    print(Style.RESET_ALL)  # Restaurar el estilo predeterminado después de la ejecución

# Ejecutar la calculadora
calculadora()
