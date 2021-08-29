




def isOctal(num):
    num = str(num)

    for elem in num:
        if (elem == "."):
            continue

        temp = int(elem)
        if temp > 7:
            return False

    return True




def convertir(num):

    if not (isOctal(num)):
        return None

    
    num = str(num)

    decimal = octal_to_decimal(num)
    binario = decimal_to_binary(decimal)
    hexa = decimal_to_hexa(decimal)
    return [decimal, binario, hexa]


#-------------------------- Octal a decimal --------------------------------


def octal_to_decimal_after_coma(num):

    n = len(num)
    exp = -1 
    res = 0
    for i in range(0, n):

        res += int(num[i])*(8**exp)
        exp -= 1  
    return res

        
def octal_to_decimal_before_coma(num):

    n = len(num)
    exp = n - 1 
    res = 0
    for i in range(0, n):

        res += int(num[i])*(8**exp)
        exp -= 1

    return res



def octal_to_decimal(num):

    val_after_coma = 0

    if("." in num):
        coma_index = num.index(".")
        val_after_coma = octal_to_decimal_after_coma(num[coma_index + 1:])
        num = num[:coma_index]
        
    val_before_coma = octal_to_decimal_before_coma(num)

    return str(round(val_before_coma + val_after_coma, 3))
    



def get_decimal(num): 
    num = int(num)
    while num > 1:
        num /= 10
    return num


#------------------ decimal a hexadecimal ---------------------------------


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



def decimal_to_hexa_before_coma(num):
    return hexa(int(num))



def decimal_to_hexa(num):

    val_after_coma = ""

    if ("." in num):
        num, decimal = num.split(".")
        val_after_coma = "."

        for i in range(0, 3):

            ent, decimal = str((get_decimal(decimal))* 16).split(".")
            decimal = int(decimal)
            val_after_coma += hexa(int(ent))  

    return decimal_to_hexa_before_coma(num) + val_after_coma


print(decimal_to_hexa("122232.3232"))


    




  



#--------------------------------- decimal a binario ------------------------


def decimal_to_binary_before_coma(num):
    return str(decimal_to_binary_before_coma_aux(int(num), 0))


def decimal_to_binary_before_coma_aux(num, exp):
        if (num==0):
            return 0
        else:
            return decimal_to_binary_before_coma_aux(num//2,exp+1) + (num%2)*10**exp


def decimal_to_binary(num):

    val_after_coma = ""
  
    if ("." in num):
        num, decimal = num.split(".")
        val_after_coma = "."
        num = int(num)
        decimal = int(decimal)

        for i in range(0, 3):

            ent, decimal = str((get_decimal(decimal))* 2).split(".")
            decimal = int(decimal)
            val_after_coma += ent  

    return decimal_to_binary_before_coma(num) + val_after_coma



print(convertir(13435))
print(convertir(3256712.34532))
print(convertir(12221.22356))
print(convertir(97832))
