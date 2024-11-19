horastrabajadas = float(input("ingrese el número de horas trabajadas ", )) #permite al usuario ingresar el numero de horas
salario = float(input("ingrese el valor de la hora ", )) # permite al usuario ingresar el valor de cada hora
porcretenfuente = float(input("ingrese el valor de la retefuente en numeros decimales, separado por un punto",)) #permite al usuario ingresar el valor de la retefuente en decimal

salariobruto = float(salario*horastrabajadas)
retenfuente = float(salariobruto*porcretenfuente)
salarioneto = float(salariobruto-retenfuente)

print("el valor del salario bruto es ", salariobruto)
print("el valor de la retefuente es ", retenfuente)
print("el valor del salario neto es ", salarioneto)
