def calcularCosto(alto,ancho,profundo):
    # volumen=alto*ancho*profundo
    # costo1=(volumen*5+2000)*1.19
    volumen=alto*ancho*profundo
    costo=volumen*5
            
    if alto>30:
        #costo=costo
        costo=costo+2000
    
    if costo>10000:
        #costo=costo
        costo=costo*.19+costo
    return costo

def costoTotal(listaPaquetes,descuento):
    
    suma=0
    #descuento
    
    for i in listaPaquetes:
     #   print (f"{i['ALTO']}")
      #  print (f"{i['ANCHO']}")
      #  print (f"{i['PROFUNDO']}")

        alto=i['ALTO']
        ancho=i['ANCHO']
        profundo=i['PROFUNDO']  
        costo=calcularCosto(alto,ancho,profundo)
        # volumen=alto*ancho*profundo
        # costo=volumen*5
                
        # if alto>30:
        #     costo=costo
        #     costo=costo+2000
        
        # if costo>10000:
        #     costo=costo
        #     costo=costo*.19+costo
        #suma+=costo*(1-descuento/100) # igual a las dos siguientes
        suma+=costo
    suma*=(1-descuento/100)
      
        #costo=suma # esta instrucción hace copia de otra variable
          
    return suma
#costoTotal=calcularCosto(listaPaquetes)

#import json
#with open ("D:\\1 PROGRAMACIÓN UIS\\CICLO 1\\python\\Visualcode\\PROGRAMACIÓN\\paquetes.json") as documento:

    listaPaquetes=json.load(documento)

print(costoTotal(listaPaquetes["PAQUETES"],10))

