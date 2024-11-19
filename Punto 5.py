import math #importamos la librería math con la cual trabajaremos para el uso de pi
Radio = float(input("ingrese el radio", )) #Permite que el usuario ingrese el valor del radio

Areacirc = math.pi*(Radio**2) #Calcula el área de la circunferencia
Circun = 2*math.pi*Radio #Calcula el perímetro de la circunferencia

print("el valor del area del circulo es", Areacirc)
print(" el valor del perimetro del circulo es", Circun)
