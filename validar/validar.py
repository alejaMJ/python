#nombre del archivo: validar.py
#AUNTOR: alejandra montoya jaramillo
#fecha: marzo 18/2023
#Descripcion: programa que valida nombre, edad y correo
#========================================================
while True:
    menu="""
    Bienvenidos al registro de usuarios, llene los campos que le soliciten y seleccione un numero del 1 al 3:
    [1] Digitar su nombre
    [2] Digitar su edad
    [3] Dijitar su correo electronico
    [4] Salir
    """
    print(menu)
    opcion=input('entre la opcion 1, 2, 3 o 4 : ')
    if opcion == '1':
        nombre= input('dijite su nombre')
        if nombre.isalpha():
            print("su nombre es: ",nombre)
            break
        else:
            print('su nombre esta mal dijitado')

    elif opcion== '2':
        edad= input('ingrese su edad: ')
        if edad.isnumeric():
            print('su edad es: ', edad )
            break
        else:
            print('no ingresate bien tu edad')

    elif opcion== '3':
        correo= input('ingresa tu correo: ')
        if correo.find('@')>=0 and correo.find('.')>=0:
            print('tu correo es...', correo)
            break
        else:
            print('correo incorrecto ')

    elif opcion == '4':
       break
