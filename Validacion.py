#Proyecto de Validacion en PYTHON, este puede ser modificable sin problemas. By TACO.

opc = 0
nombre = ''
edad = 0
genero = ''
correo = ''
grn = True


while grn:

    print('|-----------------------------------------------|')
    print('|---------- VALIDACION DE INFORMACION ----------|')
    print('|------------¿QUE QUIERES HACER?----------------|')
    print('| 1)           PONER TU NOMBRE                  |')
    print('| 2)           PONER TU EDAD                    |')
    print('| 3)           PONER TU GENERO                  |')
    print('| 4)           PONER TU CORREO                  |')
    print('| 5)           MOSTRAR LA INFORMACION TUYA      |')
    print('| 6)           SALIR DEL REGISTRO               |')
    print('|-----------------------------------------------|')

    opc = int(input('Opciones: '))

    if opc == 1:
        nombre = input('Agrega tu nombre:')
        while not nombre.isspace() and nombre.isalpha():
            print('Ingrese LETRAS en su nombre, no NUMEROS.')
            nombre =input ('Ingrese su nombre:')
            
    elif opc ==2:
        edad = input('Ingrese su Edad:')
        while not edad.isnumeric():
            print('Le pedimos que ingrese Numeros, reintentelo Nuevamente')
            edad = input('Ingrese su Edad:')
    
    elif opc ==3:       
        while grn:
            print('|-----------------------------------------------|')
            print('|------------- ¿CUAL ES TU GENERO? -------------|')
            print('| 1)           FEMENINO                         |')
            print('| 2)           MASCULINO                        |')
            print('| 3)           NO BINARIO                       |')
            print('|-----------------------------------------------|')
            genero = input('¿Cual es tu Genero?')
            while not nombre.isspace() and genero.isalpha():
                print('Ingrese una de estas opciones en NUMERO')
                genero = input('¿Cual es tu genero?: ')
                

                
    elif opc ==4:
        correo = input('Ingrese su Correo Electronico:')
        while True:
            print('Ingrese el "@" para poder continuar')
            correo =input('Ingrese su Correo Electronico:')
            
    elif opc ==5:
            print('|------------------------------------------------|')
            print('|------------- INFORMACION PERSONAL -------------|')
            print('| 1)           NOMMBRE:                          |', nombre)
            print('| 1)           EDAD:                             |', edad)
            print('| 1)           GENERO:                           |', genero)
            print('| 1)           CORREO:                           |', correo)
            print('|------------------------------------------------|')
    elif opc ==6:
        break
