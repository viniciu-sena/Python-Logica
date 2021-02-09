# Feito por Vinícius Silva Sena
#06
from statistics import mean

aluno = []
media = []

alunos = 10
notas = 4
cont = 1

for i in range(alunos):
  for x in range(notas):
    aluno.append(float(input("Informe a nota do "+str(cont)+"° aluno: ")))
  media.append(mean(aluno))
  aluno.clear()
  int(cont)
  cont += 1

aprovados = 0
for i in range(len(media)):
  if media[i] >= 7:
    aprovados += 1
print("Numero de alunos aprovados: ",aprovados)
