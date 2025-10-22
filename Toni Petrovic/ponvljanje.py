"""
broj = 10 #integer
ime = "Pero" #string
znak = 'a' #character
cijena = 10.5 #float
ispravno = True #bool

if broj > 5:
    print("broj je veci od 5")
elif broj == 5:
    print("broj je jednak 5")
else:
    print("broj nije veci od 5")

if ispravno:
    print("true")
else:
    print("false")
"""

#zadatak 2

"""
a=int(input("unesi temp: "))

if a<=0:
    print("ledenica")
elif a>0 and a<=15:
    print("hladno")
elif a>15 and a<=25:
    print("ugodno")
else:
    print("vruce")
"""

#petlje

"""
for i in range(10):
    print(i)

for slovo in "bok":
    print(slovo)

brojac = 0
while brojac < 11:
    print(brojac)
    brojac += 1
"""

#zatadak 3 parni brojevi od 2 do 20

for i in range (2, 21):
    if i %2 ==0:
        print(i)
    else:
        continue

a=2
while a <= 20:
    print(a)
    a += 2
