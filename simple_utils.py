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

def es_par(numero):
    return numero % 2 == 1
