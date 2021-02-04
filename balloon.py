#s = "BAONXXOLL" # Resultado 1
#s = "BAOOLLNNOLOLGBAX" # Resultado 2
#s = "QAWABAWONL" # Resultado 0
#s = "ONLABLABLOON" # Resultado 1
s = "BALLOON" # 0
#s = "BALLOONBALLOON" # 0

word_list = ["B", "A", "L", "L", "O", "O", "N"]
def solucion(s):
    s_list = list(s)
    completed_word = True
    for letra in word_list:
        try:
            posicion_letra = s_list.index(letra)
            s_list.pop(posicion_letra)
        except ValueError:
            completed_word = False
    resultado = 0
    if completed_word:
        elementos_a_eliminar=len(s_list)
        resultado = (elementos_a_eliminar/7)
        if resultado > 0 and resultado < 1:
            resultado = 1
        else:
            resultado = int(resultado)
            if resultado % 2 == 1:
               resultado = resultado+1

    return resultado


       
print(solucion(s))
   
