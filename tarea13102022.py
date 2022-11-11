#ejercicio 20
print("--------------------------------------------------")
name=input("introduzca su primer nombre: ")
print("la longitud de su nombre es: ", len(name))
print("--------------------------------------------------")



#ejercicio 21
nombre=input("introduzca su nombre: ")
apellido=input("introduzca su apellido: ")
print("nombre: ",nombre,apellido, " longitud: ", len(nombre + apellido))
print("--------------------------------------------------")



#ejercicio 22
name=str.lower (input("introduzca su nombre: "))
surname=str.lower (input("introduzca su apellido: "))
print(name.title(), surname.title())
print("--------------------------------------------------")



#ejercicio 23
c=input("Escriba la primera línea de una canción de cuna: ")
print("Longitud:", len(c))
n=int(input("Inserte un número inicial: "))
m=int(input("Inserte un número final:"))
print(c[n:m])
print("--------------------------------------------------")




#ejercicio 24
nose=input("Escriba cualquier palabra: ")
print(nose.upper())
print("--------------------------------------------------")



#ejercicio 25
na=input("Escriba su nombre: ")
if len(na) < 5:
    a=input("Escriba su apellido: ")
    up= na+a
    print(up.upper())
else:
    print(na.lower())
print("--------------------------------------------------")




#ejercicio 26
w=input("Introduzca una palabra: ")
o= w[O]
l=len(w)
s=w[1:l]
if o!= "a" and o!="e" and o!="i" and o!="o" and o!="u":
    nuevo= s + o + "ay"
else:
    new= w + "way"
print(new.lower())