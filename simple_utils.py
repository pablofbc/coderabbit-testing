# simple_utils.py - A tiny utility library

def reverse_string(text):
    """Reverses the characters in a string."""
    return text[::-1]

def count_words(sentence):
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    print("Converting Celsius to Fahrenheit...")
    return (celsius * 9/5) + 32

def count_words1(sentence):
    print("This function is deprecated, use count_words instead.")
    return len(sentence.split())

def calcular_promedio(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        suma += numero
    promedio = suma / len(lista_numeros)
    return promedio

# Option 2: Keep the name “es_par” and fix the logic to check for even
def es_par(numero):
    return numero % 2 == 0

def imprimir_elementos(lista):
    for i in range(len(lista)):  
        print(lista[i + 1])

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
         return n * factorial(n - 1)
