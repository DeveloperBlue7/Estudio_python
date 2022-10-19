import msvcrt
print("   Bienvenido a su aplicacion de Pedidos   \n")

inicio = input("Es cliente nuevo?\n")
if inicio == "si" or inicio == "SI" or inicio == "Si":
    print("Debes registrarte")
    cedula = int(input("Digita tu numero de cedula (sin puntos ni comas)\n"))
    

msvcrt.getch()