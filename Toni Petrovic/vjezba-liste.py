"""
moja_lista = [10, 20, 30]
prvi_element = moja_lista[0]
print(prvi_element)

moja_lista.append(40)
print(moja_lista)

dio_liste = moja_lista[1:3]
print(dio_liste)
"""

#zadatak 1

"""
lista = ["jabuka", "banana", "kruska"]
print(lista[0])
lista.append("naranca")
print(lista)
"""

#zadatak 2, 2D liste

"""
ormar=[
    ["majica", "kapa", "sal"],
    ["hlace", "carape", "remen"],
    ["jakna", "cipele", "cizme"]
]

print("hlace"ormar[1][0])
print(ormar[0][1])
print(ormar[1][1])
print(ormar[2][1])

for odjeca in ormar:
    print(odjeca[1])

for red in ormar:
    print("sadrzaj reda:", red)

    for element in red:
        print("element:", element)
"""

def pronadji_broj(lista, broj):
    print("Trazim ", broj, "u listi", lista)
    prekidac = False

    for element in lista:
        if element == broj:
            prekidac = True
            break
        else:
            prekidac = False 
    if prekidac:
        print(f"Broj {broj} je pronadjen u listi.")
    else:
        print(f"Broj {broj} nije pronadjen u listi.")

lista = [10, 20, 30, 40, 50]
broj = 30
pronadji_broj(lista, broj)