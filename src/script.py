def suma(a, b):
    return a + b

def main():
    # Vamos directo al grano
    print("--- SUMA ---")
    
    try:
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        
        # Llamamos directamente a la función suma
        print(f"Resultado: {suma(num1, num2)}")
        
    except ValueError:
        print("Error: Introduce números válidos.")

if __name__ == "__main__":
    main()
