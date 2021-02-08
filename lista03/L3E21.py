#21
import sympy

valor = int(input("Informe o valor: "))
print("Primo" if sympy.isprime(valor) == True else "Não é primo")
