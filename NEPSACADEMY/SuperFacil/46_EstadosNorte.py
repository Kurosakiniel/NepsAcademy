regiaoNorte = ["Roraima","Acre","Amapa","Amazonas","Para","Rondonia","Tocantins"]
estado = input()
RegiaoNorte = False

for regiaoNorte in regiaoNorte:
    if estado.lower() in regiaoNorte.lower() == estado.lower():
        RegiaoNorte = True
        break
if RegiaoNorte == True:
    print("Regiao Norte")
else:
    print("Outra regiao")