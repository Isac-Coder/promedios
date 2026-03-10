"""desarrollo = 60%
ingles = 20%
HSE = 20%
regular, bueno, excelente
"""

while True:

    emocionales = int(input("Ingrese su calificación en habilidades emocionales (0-100):\n "))
    
    if emocionales > 100:
        print("El puntaje no puede ser superior a 100. Por favor, ingrese un valor válido.\n")
        continue
    elif emocionales < 0:
        print("El puntaje no puede ser inferior a 0. Por favor, ingrese un valor válido.\n")
        continue
    elif emocionales < 10:
        print("El puntaje no puede ser inferior a 10. Por favor, ingrese un valor válido.\n")
        continue
    else:
        emocionales = emocionales * 0.2
        
    ingles = int(input("Ingrese su calificación en inglés (0-100):\n "))
    
    if ingles > 100:
        print("El puntaje no puede ser superior a 100. Por favor, ingrese un valor válido.\n")
        continue
    elif ingles < 0:
        print("El puntaje no puede ser inferior a 0. Por favor, ingrese un valor válido.\n")
        continue
    elif ingles < 10:
        print("El puntaje no puede ser inferior a 10. Por favor, ingrese un valor válido.\n")
        continue
    else:
        
        ingles = ingles * 0.2
    
    desarrollo = int(input("Ingrese su calificación en desarrollo (0-100):\n "))

    if desarrollo > 100:
        print("El puntaje no puede ser superior a 100. Por favor, ingrese un valor válido.\n")
        continue
    elif desarrollo < 0:
        print("El puntaje no puede ser inferior a 0. Por favor, ingrese un valor válido.\n")
        continue
    elif desarrollo < 10:
        print("El puntaje no puede ser inferior a 10. Por favor, ingrese un valor válido.\n")
        continue
    else:
        
        desarrollo = desarrollo * 0.6


    puntaje = ((emocionales) + (ingles) + (desarrollo ))

    if puntaje <= 70:
        print("Su puntaje final es BUENO:", int(puntaje), "y ha aprobado.")
        
    elif puntaje <= 30:
        print("Su puntaje final es: REGULAR", int(puntaje), "y no ha aprobado.")
        
    else:
        print("Su puntaje final es: EXCELENTE", int(puntaje), "y ha aprobado con éxito.")