num1 = int(input("De qual número deseja ver a tabuada:  "))

print("Tabuado do" , num1 , ":")
for i in range(1,11):
    print(num1 , " x " , i , " = " , num1 * i)