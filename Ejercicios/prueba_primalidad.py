def es_primo(numero):
    contador  = 0

    for c in range (1, numero + 1):
        if c == 1 or c == numero:
            continue
        if numero % c == 0:
            contador += 1
    if  contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Digite un Numero: "))
    if es_primo(numero):
        print("'Es primo")
    else:
        ("No es primo")


if __name__ == '__main__':
    run()