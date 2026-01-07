def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def media(a, b):
    return (a + b) / 2

def mostrar_resultado(opcion, num1, num2):
    # Aceptamos tanto el número como el nombre por si el usuario escribe "suma"
    if opcion == 'suma' or opcion == '1':
        print(f"Resultado: {suma(num1, num2)}")
    elif opcion == 'resta' or opcion == '2':
        print(f"Resultado: {resta(num1, num2)}")
    elif opcion == 'multiplicacion' or opcion == '3':
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif opcion == 'division' or opcion == '4':
        print(f"Resultado: {division(num1, num2)}")
    elif opcion == 'media' or opcion == '5':
        print(f"Resultado: {media(num1, num2)}")
    else:
        print("Opción no válida.")

def main():
    # Ya no hay verificación de argumentos (sys.argv).
    # Entramos directamente al modo interactivo.
    print("--- MENU ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Media")
    
    opcion = input("Elige opción (1-5 o nombre): ")
    
    try:
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        mostrar_resultado(opcion, num1, num2)
    except ValueError:
        print("Error: Introduce números válidos.")

if __name__ == "__main__":
    main()
