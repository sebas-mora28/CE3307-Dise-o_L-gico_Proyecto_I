

'''
Esta funcion verifica si un numero es octal

Entradas:
            - num : Dato de tipo entero que representa el numero que se desea verificar 

Salidas: 
            - True en caso de que el numero sea octal, False en caso contrario 

'''
def isOctal(num):
    num = str(num)

    for elem in num:
        if (elem == "."):
            continue

        temp = int(elem)
        if temp > 7:
            return False

    return True



'''
Esta funcion recibe un numero en base octal y devuelve el equivalente del respectivo numero en
binario, hexadecimal y decimal

Entradas:
            - num : Dato de tipo entero que representa el numero que se desea verificar 

Salidas: 
            - Lista con los equivalente en decimal, hexadecimal y binario 
            
'''
def convertir(num):

    #Se verifica que el numero sea octal
    if not (isOctal(num)): 
        return None

   
    num = str(num)

    #Se obtiene los equivalentes del numero dado por el usuario en decimal, binario y hexadecimal
    decimal = octal_to_decimal(num)
    binario = decimal_to_binary(decimal)
    hexa = decimal_to_hexa(decimal)
    return [decimal, binario, hexa]


#-------------------------- Octal a decimal --------------------------------


'''
Esta funcion se encarga de convertir un los numeros que se encuentran despues de la comma de octal a decimal

Entradas:
            - num : Dato de tipo entero que se desea convertir

Salidas: 
            - Entero con el equivalente del numnero ingreso en octal    
'''

def octal_to_decimal_after_comma(num):

    n = len(num)
    exp = -1 
    res = 0
    for i in range(0, n):

        res += int(num[i])*(8**exp)
        exp -= 1  
    return res


'''
Esta funcion se encarga de convertir un los numeros que se encuentran antes de la comma de octal a decimal

Entradas:
            - num : Dato de tipo entero que se desea convertir

Salidas: 
            - Entero con el equivalente del numnero ingreso en octal    
'''
def octal_to_decimal_before_comma(num):

    n = len(num)
    exp = n - 1 
    res = 0
    for i in range(0, n):

        res += int(num[i])*(8**exp)
        exp -= 1

    return res



'''
Esta funcion encarga de convertir un numero en octal a decimal. En caso de que el numero contenga decimales, se procede a dividir el 
numero en aquellos que se encuentran antes y despues de la coma y se realiza el procedimiento del calculo por separado. 

Entradas:
            - num : Dato de tipo entero que se desea convertir

Salidas: 
            - String que representa el equivalente del numero en octal ingresado en decimal    
'''
def octal_to_decimal(num):

    num_after_comma = 0

    if ("." in num):
        comma_index = num.index(".")
        num_after_comma = octal_to_decimal_after_comma(num[comma_index + 1:])
        num = num[:comma_index]
        
    num_before_comma = octal_to_decimal_before_comma(num)

    return str(round(num_before_comma + num_after_comma, 3))
    


#------------------ decimal a hexadecimal ---------------------------------

'''
Esta funcion encarga de convertir un numero dado en decimal a su equivalente en hexadecimal
Entradas:
            - num : Dato de tipo entero que se desea convertir

Salidas: 
            - String que representa el equivalente del numero en octal ingresado en decimal    
'''
def hexa(num):
    if (num%16 >= 10):
        if (num%16==10):
            return  hexa(num//16)+ "A"
        if (num%16==11):
            return hexa(num//16) + "B"
        if (num%16==12):
            return hexa(num//16) + "C"
        if (num%16==13):
            return hexa(num//16) + "D"
        if (num%16==14):
            return hexa(num//16) + "E"
        if (num%16==15):
            return hexa(num//16) +"F" 
    elif (num < 9):
        if (num==0):
            return ""
        else:
            return str(num)
    else:
        return hexa(num//16) + str(num%16)



'''
Esta funcion recibe un numero y devuelve los digitos decimales en caso de que los contenga

Entradas:
            - num : Dato de tipo entero 

Salidas: 
            - Flotante que representa los decimales del numero dado 
'''
def get_decimals(num): 
    num = int(num)
    while num > 1:
        num /= 10
    return num




'''
Esta funcion se encarga de convertir un los numeros que se encuentran antes de la comma de decimal a hexadecimal

Entradas:
            - num : Dato de tipo entero que se desea convertir

Salidas: 
            - Entero con el equivalente del numnero ingreso en octal    
'''
def decimal_to_hexa_before_comma(num):
    return hexa(int(num))




'''
Esta funcion encarga de convertir un numero en decimal a hexadecimal. En caso de que el numero contenga decimales, se procede a dividir el 
numero en aquellos que se encuentran antes y despues de la coma y se realiza el procedimiento del calculo por separado. 

Entradas:
            - num : Dato de tipo entero que se desea convertir

Salidas: 
            - String que representa el equivalente del numero en octal ingresado en decimal    
'''
def decimal_to_hexa(num):

    num_after_comma = ""

    if ("." in num):
        num, decimal = num.split(".")
        num_after_comma = "."

        for i in range(0, 3):

            ent, decimal = str((get_decimals(decimal))* 16).split(".")
            decimal = int(decimal)
            num_after_comma += hexa(int(ent))  

    return decimal_to_hexa_before_comma(num) + num_after_comma


#--------------------------------- decimal a binario ------------------------



'''
Esta funcion se encarga de convertir un los numeros que se encuentran antes de la comma de decimal a binario

Entradas:
            - num : Dato de tipo entero que se desea convertir

Salidas: 
            - Entero con el equivalente del numnero ingreso en octal    
'''
def decimal_to_binary_before_comma(num):
    return str(decimal_to_binary_before_comma_aux(int(num), 0))


def decimal_to_binary_before_comma_aux(num, exp):
        if (num==0):
            return 0
        else:
            return decimal_to_binary_before_comma_aux(num//2,exp+1) + (num%2)*10**exp


'''
Esta funcion encarga de convertir un numero en decimal a binario. En caso de que el numero contenga decimales, se procede a dividir el 
numero en aquellos que se encuentran antes y despues de la coma y se realiza el procedimiento del calculo por separado. 

Entradas:
            - num : Dato de tipo entero que se desea convertir

Salidas: 
            - String que representa el equivalente del numero en octal ingresado en decimal    
'''
def decimal_to_binary(num):

    num_after_comma = ""
  
    if ("." in num):
        num, decimal = num.split(".")
        num_after_comma = "."
        num = int(num)
        decimal = int(decimal)

        for i in range(0, 3):

            ent, decimal = str((get_decimals(decimal))* 2).split(".")
            decimal = int(decimal)
            num_after_comma += ent  

    return decimal_to_binary_before_comma(num) + num_after_comma


##print(convertir(13435))
##print(convertir(3256712.34532))
##print(convertir(12221.22356))
##print(convertir(97832))
