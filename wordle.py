print("Bienvenido a WORDLE")
wordle = "ZORRO"
oportunidades = 0 # va a contar la cantdad de palabras ingresadasa correctamente 
while oportunidades < 6: #tenemos 6 oportunidades
    print("-----------------------------------------")
    print(f"Oportunidad #{oportunidades+1}")
    palabra = input("Ingrese una palabra en mayuscula")
#   primero vamos a verificar si es que la palabra ingresada tiene 5 letras
    if len(palabra) == 5: #En caso que coincida entramos al juego 
        aciertos = 0 #asignamos un contador que si llega a 5 es porque se gano el juego
        m = 0 #indicador de posición de palabra
        for letra_palabra in palabra :
            caracter = False
            posicion = False
            #print(letra_palabra,m)
            n = 0 #indicador de posición en wordle
            for letra_wordle in wordle :
                #print(letra_wordle,n)
                if letra_palabra == letra_wordle:
                    caracter = True
                    #print("coicide la letra")
                    if m == n:
                        posicion = True
                        #print ("coicide posición") 
                n = n+1
            if caracter == False:
                print(letra_palabra," No existe el caracter")
            elif caracter == True and posicion == False:
                print(letra_palabra," El caracter existe, pero no esta en la posicieon correcta")
            else:
                print(letra_palabra," El caracter existe, y esta en la posición correcta")
                aciertos = aciertos+1    
            m = m+1
        print(f"Te quedan {aciertos} aciertos")
        if aciertos == 5:
            print("Ganaste!")
            break        
        oportunidades = oportunidades + 1
        if oportunidades > 5:
            print("Perdiste")
            break
    else:
        print("La palabra que ingresaste no es valida, debe ser de 5 caracteres") 
print("Gracias por jugar")  