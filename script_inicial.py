''' 2. Entradas de cine:
Un cine cobra diferentes precios de entradas según la edad de una
persona. Si una persona es menor de 3 años, la entrada es gratuita; si
está entre 3 y 12 años el ticket cuesta $ $5.000; y si son mayores de 12
años el ticket cuesta $7.000. Escriba un loop que pregunte a los usuarios
su edad y luego informe el costo de su ticket de cine. '''
res1 ="s"
while res1 == "s":  
    edad = str(input("Ingrese la edad de una persona : "))  
    if(int(edad) < 3):
        print("El ticket es gratis!!!")
    elif(int(edad)>=3 and int(edad)<=12):
        print("El ticket cuesta $5.000")
    elif(int(edad)>12):
        print("El ticket cuesta $7.000")
    res = str(input("Desea un nuevo ingreso de entrada? s/n : "))    
    res1 = res.lower()
    if(res=="n"):
        print("Gracias por preferirnos")
        break