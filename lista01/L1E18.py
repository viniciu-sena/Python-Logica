#18
arquivo = float(input("Tamanho do arquivo MB: "))
vel = float(input("Velocidade do link Mbps: "))

vel02 = (vel/8)
tbaixar = (arquivo/vel02)

print("O arquivo sera baixado em ", (tbaixar/60), " minutos")
