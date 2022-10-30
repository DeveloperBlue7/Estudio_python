with open("write.text", "a") as file:
    file.write("Final de las filas\n")
    file.write("inicio de las filas\n")
    file.write("vamos con toda\n")

with open("./write.text", "r") as read:
    for d in read:
        print(d)