# numero da pocao 
# entrada
# saida, numero total, somando os pratos * a pocao

curupiraGramas = 300
boitataGramas = 1500
boto = 600
mapinguari = 1000
iara = 150

qntPocaoCurupira = int(input())
qntPocaoBoitata = int(input())
qntPocaoBoto = int(input())
qntPocaoMapinguari = int(input())
qntPocaoIara = int(input())

calculoTotalCurupira = curupiraGramas * qntPocaoCurupira
calculoTotalBoitata = boitataGramas * qntPocaoBoitata
calculoTotalBoto = boto * qntPocaoBoto
calculoTotalMapinguari = mapinguari * qntPocaoMapinguari
calculoTotalIara = iara * qntPocaoIara

somaTotal =  (calculoTotalCurupira + calculoTotalBoitata + calculoTotalBoto + calculoTotalMapinguari + calculoTotalIara)
print(somaTotal)