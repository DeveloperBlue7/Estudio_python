def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invert = palabra[::-1]
    if palabra == palabra_invert:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Si es palindromo")
    else:
        print("No es Palindromo")

if __name__ == "__main__": 
    run()