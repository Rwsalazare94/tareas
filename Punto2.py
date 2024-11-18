suma = float(input("Añade el valor de 1 de la suma",)) #Permite al usuario ingresar el valor 1 de la operacion
x = float(input("Añade el valor 2 de la suma",)) #Permite al usuario ingresar el valor 2 de la operacion
y = float(input("Añade eñ valor 3 de la operacion",)) #Permite al usuario ingresar el valor 3 de la operacion
suma = suma + x #Al valor que tiene la variable suma le añade el valor de x y actualiza la variable
x = x+y**2 #Al valor de x le suma la variable y al cuadrado y actualiza el valor
suma = suma + x/y #Realiza la divison entre las variables x e y y les añade la variable suma
print("el valor de la suma es", suma)