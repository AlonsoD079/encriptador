
# Programa para identificar el pago de entrada al Museo del Oro
# Si es menor 12 años paga $10.000
# Si la edad está entre 12 y 17 años paga $20.000
# Si es adulto mayor, paga $30.000  => a partir de 60 años
# Los demás pagan $60.000   =>   mayor de edad (18) y menor de 60 años
# Si el visitante tiene una estura mayor a metro y medio, incrementa el costo en $3.000
# Si es fin de semana o festivo el costo de la entrada incrementa en 30%


# Al iniciar el programa
fds = input("\nEs fin de semana o festivo (S/N): ")
if fds == "S" or fds == "s":
    fds = True
else:
    fds = False


# Entrada(s)
precEntrMuseo = "Error al seleccionar precio..."
# edad = 6
edad = int(input("\nDigite la edad del visitante al Museo: "))
estatura = float(input("Digite la estatura del visitante (m): "))


# Transformación
if edad < 12:
    precEntrMuseo = 10000
    # if estatura > 1.50:
    #     precEntrMuseo = precEntrMuseo + 3000
        

# elif edad >= 12 and edad < 18:
elif edad < 18:
    precEntrMuseo = 20000
    # if estatura > 1.50:
    #     precEntrMuseo = precEntrMuseo + 3000

# elif edad >= 18 and edad < 60:
elif edad < 60:
    precEntrMuseo = 60000
    # if estatura > 1.50:
    #     precEntrMuseo = precEntrMuseo + 3000

# elif edad >= 60:
else:
    precEntrMuseo = 30000
    # if estatura > 1.50:
    #     precEntrMuseo = precEntrMuseo + 3000

# else:
#     print("Otro caso... digito esdad:", edad)

if estatura > 1.50:
        # precEntrMuseo = precEntrMuseo + 3000
        precEntrMuseo += 3000 


# if fds == True:
if fds:
        # precEntrMuseo = precEntrMuseo + (precEntrMuseo * (30 / 100))
        # precEntrMuseo = precEntrMuseo * (1 + 0.30)
        # precEntrMuseo = precEntrMuseo * (1.30)
        precEntrMuseo *= 1.30



# Salida(s)

print("\nEl costo de la entra al museo es: ", precEntrMuseo, "\n")




