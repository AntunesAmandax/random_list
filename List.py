import random

notas = []
alunos = 14
cont = 0
media = 7
acimaDaMedia = []
namedia = []
abaixomedia = []

while cont<=alunos:
   nota = random.randint(0,10)
   notas.append(nota)
   cont = cont + 1

for item in notas:
   if item>media:
      acimaDaMedia.append(item)
   else:
      if item==7:
         namedia.append(item)
      else:
         if item<media:
            abaixomedia.append(item)

print("Temos ",len(acimaDaMedia),"alunos acima da média.")
print("Temos ",len(namedia), "alunos na média.")
print("Temos ",len(abaixomedia), "alunos abaixo da média.")
print("A maior nota é",max(notas))
print("A menor nota é",min(notas))

