# Desenvolvido por Daniel Schinaider de Oliveira
# Exercício número 4

caract = ["s","d","e","t","h","w","a","v","u","i"]
cont = 0
consoante = []
for i in range(0,10):
    if caract[i].lower() != "a" and caract[i].lower() != "e" and caract[i].lower() != "i" and caract[i].lower() != "o" and caract[i].lower() != "u":
        cont = cont + 1
        consoante.append(caract[i])
    else:
        continue

for x in range(0, len(consoante)):
    print(consoante[x])

print("Seu vetor tem" , cont , "consoantes!")