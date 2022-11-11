#import math  #para utilizar la libreria se coloca al inicio 
#num=4
#print(num**(1/2))
#es igual a 
#print(math.sqrt(num))
#decimal= 3.1415169264

#print(round(decimal,6))
#print(math.pi)



import math
#Ejercicio 27
print("--------------------------------------------")
num=float(input("introduzca un número con muchos decimales: "))
m= num*2
print("el resultado es: ",m)
print("....................")

#ejercicio 28
print("en base a lo anterior")
print("el resultado es: ",round(m,2))
print("--------------------------------------------")

#ejercicio 29
num= int(input("introduzca un número mayor a 500: "))
raiz= num**(1/2)
print("la raíz de", num, "es", round(raiz,2))
print("--------------------------------------------")

#ejercicio 30
print(math.pi)
print(round(math.pi,5))
print("--------------------------------------------")

#ejercicio 31
radio= int(input("ingrese radio del circulo: "))
n=(math.pi)*(radio**2)
print("resultado: ",n)
print("--------------------------------------------")


#ejercicio 32
print("                 CILINDRO")
radio= int(input("introduzca el radio: "))
dep= int(input("introduzca profundidad: "))
totalvolumen= ((math.pi)*(radio**2))*(dep)
print("el resultado es: ",round(totalvolumen,3))
print("-------------------------------------------")

#ejercicio 33
print("introduzca dos números")
num1=float(input(" "))
num2=float(input(" "))
o= num1//num2
p= num1%num2
print(num1,"dividido entre ",num2," es ",o," con ",p," de residuo ")
print("-------------------------------------------")


#ejercicio 34
print("1) Cuadrado")
print("2) Triángulo")
num=int(input("Introduzca un número: "))
if num==1:
    log=int(input("escriba la longitud de uno de sus lados: "))
    area= log*log
    print("el área del cuadrado es: ",area)
elif num==2:
    base=int(input("escriba la base del triángulo: "))
    h= int(input("escriba la altura: "))
    a= ((base*h)/2)
    print("el área del triángulo es: ",a)
else:
    print("ERROR")

print("-------------------------------------------")


