# Feito por Vinícius Silva Sena
#10
msg = ".."

print("Turnos: M-matutino, V-vespertino e N-noturno")
turno = input("Informe o turno em que voce estuda: ")

if turno in "mM":
  msg = "Bom dia"
elif turno in "vV":
  msg = "Boa tarde"
elif turno in "nN":
  msg = "Boa noite"
else:
  msg = "Valor invalido"

print(msg)
