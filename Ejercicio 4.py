""""El día juliano correspondiente a una fecha es un número entero que indica los días que han 
transcurrido, desde el 1 de enero del año indicado,ademas de que compruebe si la fecha existe o no.
Crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. """

"""Funcion para comprobar si la fecha es validad"""
def Comrpobarfecha(dia,mes,a):
    if dia<1 or dia>Meses(mes,a):
        return False
    else:
        return True



""""Funcion para calcular si es bisiesto o no"""

def Bisiesto(a):
    return (a % 4 == 0 and not (a % 100 == 0)) or a % 400 == 0

"""Funcion para calcular cuantos dias tendra un mes"""

def Meses(mes,a):
    if mes in [1,3,5,7,8,10,12]:
        return 31 
    elif mes in [4,6,9,11]:
        return 30
    elif mes == 2:
        if Bisiesto(a):
            return 29
        else:
            return 28

"""Funciona para calcular el dia juliano"""   

def CalJuliano(dia,mes,a):
    diaj = 0
    for mes in range(1,mes):
        diaj = diaj + Meses(mes,a)
        diaj = diaj + dia
        return diaj        
    
"""Funciona para calcular la fecha""" 

def Fecha():
        while True:
         dia = int(input("Introdusca el día: "))
         mes = int(input("Introdusca el mes: "))
         a = int(input("Introdusca el año: "))
         if not Comrpobarfecha(dia,mes,a):
            print("Fecha no validad") 
         else:
          break
        
        return dia,mes,a
   
"""Calculo del dia juliano comprobando si la fecha existe"""  
d,m,an = Fecha()
print ("El día juliano: ",CalJuliano(d,m,an))
