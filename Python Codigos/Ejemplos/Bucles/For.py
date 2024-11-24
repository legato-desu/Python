# For

"""
Crea un programa que use el bucle for para imprimir los números.
de 5 a 17, de 0 a -9 en 3 y un bucle for para imprimir elementos desde una lista hasta llegar al idioma del bucle
"""

for x in range(5,18,1):
    print(x)

for y in range(0,-12,-3):
    print(y)

language = ["Ingles","Español","Portugues","Frances","Japones","Ruso"]    

for a in language:
    if a == "Frances":
        # pass,continue,break
        # pass "enseña todos los elementos de la lista"
        # continue "quita el elemento que se nombro"
        # break "detiene la ejecucion hasta dicho elemento"
        break
    print(a)