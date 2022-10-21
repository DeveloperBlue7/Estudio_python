def lista():
    estudiantes = {
        "Christian": 25,
        "Carlos": 31,
        "Andres": 28 
    }
    #mostrar llaves
    for nombres in estudiantes.keys():
        print(nombres)

    #mostrar valores
    for nombres in estudiantes.values():
        print(nombres)

    for nombres, edad in estudiantes.items():
        print(f"{nombres} tiene {edad} años")


if __name__ == "__main__":
    lista()
