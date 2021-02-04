
numero = 1376796946
def solucion(N):
    #primer_digito = ""
    espacio_binario = 0
    espacio_binario_mayor = 0
    binario = (bin(N)[2:])
    
    print (binario)
    for digito in binario:
        if digito == "1":
           #primer_digito = "1"
           if espacio_binario > espacio_binario_mayor:
              espacio_binario_mayor = espacio_binario
           espacio_binario= 0  
           
        else:
            espacio_binario = espacio_binario + 1
        
    return espacio_binario_mayor 
    
print(solucion(numero))