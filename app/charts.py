import matplotlib.pyplot as plt

def generar(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generar1(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 800, 20]
    #generar(labels, values)
    generar1(labels, values)