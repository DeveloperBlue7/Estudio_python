items = [
    {
        'producto': "Camisa",
        'precio': 70000
    },
    {
        'producto': "Chaqueta",
        'precio': 200000
    },
    {
        'producto': "Botas",
        'precio': 400000
    }
]

precios = list(map(lambda d: d['precio'], items))
print(items)
print(precios)

def agregar(d):
    new_d = d.copy()
    new_d['impuesto'] = new_d['precio'] * 0.19
    return new_d

nuevo = list(map(agregar, items))
print(nuevo)
print(items)