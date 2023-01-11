
numeropaquetes=int(input())
costototal=0


for i in range (numeropaquetes):
    alto=float(input())
    ancho=float(input())
    profundo=float(input())
    iva=float(.19)
    mayorque30=+2000

    volumen=alto*ancho*profundo
    costo=volumen*5

    if alto>30:
        costo=costo
        costo=costo+2000

    if costo>10000:
        costo=costo
        costo=costo*.19+costo
        

    print (volumen)
    print (costo)
    costo+i
    costototal+=costo

    

print(costototal)


