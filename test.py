#rječnik (dictionary)
kosarica = {}
print(f"prazna košarica: {kosarica}")
print(f"tip: {type(kosarica)}")

#dodavanje elemenata u rječnik
kosarica['jabuka'] = 15
kosarica['kreke'] = 23
kosarica['mandarine'] = 3

#ispis
print(f"napunjena košarica:{kosarica} ")

kosarica['jabuka'] = kosarica['jabuka']+5
print(f"ažurirana košarica: {kosarica}")

broj_mandarina = kosarica['mandarine']
print(f"broj mandarina {broj_mandarina}")
try:
    broj_krusaka = kosarica['kruska']
    print(f"broj krusaka {broj_krusaka}")
except Exception as e:
    print(f"greška: {e}")

trazim_voce = 'kreke'
if trazim_voce in kosarica:
    print(f"imamo {kosarica[trazim_voce]} komada voća '{trazim_voce}.")
else:
    print(f"nažalost, nemamo '{trazim_voce}', u kosarici.")