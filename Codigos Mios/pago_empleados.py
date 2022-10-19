
def empleados(empleados):
    print("-------Nomina De BlueSystem-------\n")
    conteo = 0
    lista = []
    pago_diario = 45000
    while conteo < empleados:
        dias = int(input(f"Dias trabajados del empleado numero {conteo + 1}: "))
        pago = dias * pago_diario
        lista.append(pago)
        conteo +=1
    print("Lista de Pagos a empleados\n")
    conteo = 0
    for i in lista: 
        conteo +=1
        print(f"El empleado numero {conteo} gano {i} pesos")



def empleados1(empleado, pago_dia):
    print("-------Nomina De BlueSystem-------\n")
    conteo = 0
    lista = []
    nombres = []
    dia = []
    while conteo < empleado:
        nombre = input("Digita tu nombre: ")
        nombres.append(nombre)
        dias = int(input("Digite los dias trabajados: "))
        dia.append(dias)
        pago = dias * pago_dia
        lista.append(pago)
        conteo +=1
        print("")
    print("-------Datos De Los Empleados-------\n")
    for c, d, e in  zip(nombres, lista, dia):
        print(f"El empleado {c} gano {d} pesos por los {e} dias trabajados ")


if __name__ == '__main__':
    empleados1(2, 50000)