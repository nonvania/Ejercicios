#ejercicio 1
name=input("¿Cómo te llamas? ")
print("Hola ",name)




#ejercicio 2
name=input("¿Cuál es tu nombre? ")
surn=input("¿Cuál es tu apellido? ")
print("Hola ",name , surn)




#ejercicio 3
print("¿Cómo llamas a un oso sin dientes?")
print("¡Un osito de goma!")
#a ese no le entendí la instrucción




#ejercicio 4
num1 = int(input ('introduzca 1 número: '))
num2 = int(input ('introduzca otro número: '))
suma=num1+num2
print(suma)




#ejercicio 5
num1 = int(input ('introduzca 1er número: '))
num2 = int(input ('introduzca 2do número: '))
num3 = int(input ('introduzca 3er número: '))
total= (num1+num2)*num3
print('el total es ',total)




#ejercicio 6
rebs1= int(input ('¿cuántas rebanadas tiene la pizza?'))
rebs2=int(input('¿cuántas rebanadas de pizza has comido?'))
sobrantes=rebs1-rebs2
print('sobra/n ', sobrantes, ' pedazo/s de pizza')





#ejercicio 7
name = str(input('¿cómo te llamas? '))
age =int (input('¿cuántos años tienes? '))
suma= age+1
print('el próximo año tendrás ', suma, 'años')





#ejercicio 8
cuenta = int(input ('total de la cuenta '))
cuenta = int(input ('total de la cuenta $'))
n = int(input ('número de platillos: '))
division= cuenta/n
print('cada persona deberá pagar $',division)




#ejercicio 9
dias = int(input ('escribe una cantidad de días: '))
horas= dias*24
minutos= 60*horas
segundos= 60*horas
segundoa= 60*minutos
minutos=1440*horas
segundos=86400*horas
print('en ', dias, 'días hay ', horas, ' horas', ',', minutos, ' minutos', ' y ', segundos, 'segundos')




#ejercicio 10
peso = float(input ('escriba peso en kilogramos: '))
libras= 2.204*peso
print(peso, ' kilogramos son igual a ',libras)






#ejercicio 11
num = int(input ('ingrese un número mayor a 100: '))
n = int(input ('ingrese un número menor a 10: '))
div=num/n
print(n, ' cabe ', div, 'veces en el ',num)
