def calcularCosto(alto,ancho,profundo):
    volumen=alto*ancho*profundo
    costo1=(volumen*5+2000)*1.19
    return costo1

def costoTotal(numeropaquetes,descuento):
    
    suma=0
    descuento
    for i in range (numeropaquetes):
          
        alto=float(input())
        ancho=float(input())
        profundo=float(input())
        volumen=alto*ancho*profundo
        costo=volumen*5
                
        if alto>30:
            costo=costo
            costo=costo+2000
        
        if costo>10000:
            costo=costo
            costo=costo*.19+costo
        suma+=costo*(1-descuento/100)
       # suma+=costo*50/100 ESTA FORMA ME ARROJÓ LOS RESULTADOS PERO EN ROJO EL CODE RUNNER
       # suma-=costo*(descuento/100) ESTA FORMA TAMBIÉN ES CORRECTA
        costo=suma
          
    return costo
print(calcularCosto(35,10,5))
print(costoTotal(2,50))

