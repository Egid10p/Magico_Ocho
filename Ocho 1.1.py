print("\t =======================")
print("\t\tMagico Ocho")
print("\t =======================")
import random
while True:
    while True:
        print("Escribe tu pregunta para que Ocho te de la respuesta")
        pregunta = input("")
        if len(pregunta) > 0:
            break
        else:
            print("Error: Debe introducir una pregunta")
    pre_respuestas = (["Es Cierto","Es decididamente así","Sin lugar a dudas",
                       "Sí, definitivamente","Puedes confiar en ello",
                       "Como yo lo veo, sí","Lo más probable es que sí",
                       "Perspectiva buena","Sí","Las señales apuntan a que sí",
                       "Respuesta confusa vuelve a intentarlo","Vuelve a preguntar más tarde",
                       "Mejor no decirte ahora","No se puede predecir ahora",
                       "Concéntrate y vuelve a preguntar","No cuentes con ello",
                       "Mi respuesta es que no","Mis fuentes dicen que no",
                       "Las perspectivas no son muy buenas","Muy dudoso"])
    numlist = len(pre_respuestas)
    respuesta = pre_respuestas [random.randint(0, numlist-1)]
    print(respuesta)
    while True:
        restart = input("¿Quieres volver a ejecutar el programa?(s/n): ")
        if restart.lower() == "s" or restart.lower() == "n":
            break
        else:
            print("Error")
    if restart.lower() == "n":
        break
print("Gracias por usar este programa :)")