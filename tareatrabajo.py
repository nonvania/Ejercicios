
#ejercicio 35
print("______________________________________________")
nombre=input("introduzca su nombre: ")
for i in range(0,3):
    print(nombre)
print("______________________________________________")


#ejercicio 36
nombre=input("escriba su nombre: ")
num=int(input("introduzca un número: "))
for i in range(0,num):
    print(nombre)
print("______________________________________________")


#ejercicio 37
nombre=input("escriba su nombre: ")
for i in nombre:
    print(i)
print("______________________________________________")


#ejercicio 38 
nombre=input("escriba su nombre: ")
num=int(input("escriba un número: "))
for x in range(0,num):
    for i in nombre:
         print(i)
print("______________________________________________")



#ejercicio 39
num=int(input("escriba un número entre 1 y 12: "))
for i in range (1,11):
    m= i*num
    print(i,"x", num, "=", m)
print("______________________________________________")



#ejercicio 40
n=int(input("ingrese un número debajo del 50: "))
for i in range (50,n-1, -1):
    print(i)
print("______________________________________________")


#ejercicio 41
name=input("escriba su nombre: ")
num=int(input("introduzca un número: "))
if num<10:
    for x in range(0,num):
        for i in nombre:
            print(i)
else:
    n="MUY ALTO"
    for i in range(0,3):
        print(n)
print("______________________________________________")




#ejercicio 42
t=0
for i in range (0,5):
    num=int(input("ingrese un número: "))
    n= input("quieres incluir este número? ")
    n=n.lower()
    if a=="si":
        t=t+num
print(t)
print("______________________________________________")



#ejercicio 43
d=d.lower(input("desea contar hacia arriba o hacia abajo? "))
if direction == "arriba":
    num = int(input ("cual es el numero superior? "))
    for i in range (1, num+1):
        print (i)
elif d == "abajo":
    num = int(input ("ingrese un numero menor a 20: "))
    for i in range (20, num-1, -1):
        print (i)
else: print ("no entiendo")
print("______________________________________________")




#ejercicio 44
num= int(input ("cuántos amigos quiere invitar a la fiesta? "))
if num < 10:
    for i in range (0, num):
        name input ("escriba un nombre: ")
        print (name, "ha sido invitado")
else:
    print ("demasiada gente")