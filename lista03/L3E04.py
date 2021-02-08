# Criado por Daniel Schinaider de Oliveira

#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

paisA = 80000
paisB = 200000
vezes = 1

while paisA < paisB:
    paisA = int((paisA * 0.03) + paisA)
    paisB = int((paisB * 0.015) + paisB)
    if paisA >= paisB:
        break
    vezes = vezes + 1

print("Populacao pais A: ", paisA)
print("Populacao pais B: " , paisB)
print("Irá levar " , vezes , " anos")