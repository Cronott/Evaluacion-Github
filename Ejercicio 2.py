"""Programa que calcule el IVA de una compra,siendo el IVA del 19% sobre el valor total de compra"""

def CIVA(C):
    IVA = C * 0.19
    return IVA

compra = float(input("Ingrese el valor de la compra: "))
IVA = CIVA(compra)
print("El valor de la compra es: ",compra)
print("El valor del IVA de la compra es: ",IVA)
print("El total a pagar incluido el IVA es: ",compra+IVA)