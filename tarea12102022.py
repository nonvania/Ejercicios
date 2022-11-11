#ejercicio 12
num = int (input("introduzca dos números: "))
num2 = int (input(" "))
if num>num2 :
    print(num","num2)
else:
    print(num2","num)





#ejercicio 13
num= int(input("introduzca número menor que 20: "))
if num<20:
    print("Gracias")
else:
    print("número muy grande")





#ejercicio 14
num=int(input("introduzca un número entre 10 y 20: "))
if num<=20 and num>=10:
    print("Gracias")
else:
    print("Respuesta Incorrecta")






#ejercicio 15
color= input("Ingresa tu color favorito: ") #text=str.lower(text)
if color=="rojo" or color=="Rojo" or color=="ROJO":
    print("También me gusta el color rojo")
else:
    print("No me gusta el color",color,"prefiero el rojo")






#ejercicio 16
ans=str.lower (input("¿está lloviendo? si/no "))
if ans!="si":
     print("disfruta tu día")
elif ans=="si":
    an= input("¿es un día ventoso?")
    if an=="si":
        print("está muy ventoso para una sombrilla")
    else:
        print("toma una sombrilla")






#ejercicio 17
edad=int(input("introduzca su edad: "))
if edad>=18:
    print("puedes votar")
elif edad==17:
    print("puedes aprender a manejar")
elif edad==16:
    print("puedes comprar un boleto de lotería")
elif edad<16:
    print("puedes pedir dulce o truco")






#ejercicio 18
num=int(input("escriba un número: "))
if num<10:
    print("muy bajo")
elif num<10 and num>20:
    print("correcto")
else:
    print("muy alto")






#ejercicio 19
ans=int(input("introduzca 1, 2 o 3: "))
if ans==1:
    print("Gracias")
elif ans==2:
    print("Bien hecho")
elif ans==3:
    print("Correcto")
else:
    print("Mensaje error")
