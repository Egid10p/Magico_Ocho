print("========================================")
print("Ocho")
print("========================================")
print("")
import random
nom_completo = input("Para empezar introduce tu nombre: ")
nom_completo = nom_completo.title()
nom = nom_completo.split()[0]
print(f"Hola {nom.split()[0]}")
opc = "s"
while opc == 's' or opc == 'S':
    pregunta = input(f'{nom} escribe tu pregunta para que Ocho te de la respuesta: ')
    prenum = len(pregunta)
    while prenum == 0:
        print("Hubo un error.")
        pregunta = input(f'{nom} escribe tu pregunta de nuevo: ')
        prenum = len(pregunta)
    random_num = random.randint(1, 20)
    respuesta = 0
    respuesta += random_num
    if respuesta == 1:
        print("Es cierto.")
    elif respuesta == 2:
        print("Es decididamente así.")
    elif respuesta == 3:
        print("Sin lugar a dudas.")
    elif respuesta == 4:
        print("Sí, definitivamente.")
    elif respuesta == 5:
        print("Puedes confiar en ello.")
    elif respuesta == 6:
        print("Como yo la veo, sí.")
    elif respuesta == 7:
        print("Lo más probable.")
    elif respuesta == 8:
        print("Perspectiva buena.")
    elif respuesta == 9:
        print("Sí.")
    elif respuesta == 10:
        print("Las señales apuntan a que sí.")
    elif respuesta == 11:
        print("Respuesta confusa, vuelve a intentarlo.")
    elif respuesta == 12:
        print("Vuelve a preguntar más tarde.")
    elif respuesta == 13:
        print("Mejor no decirte ahora.")
    elif respuesta == 14:
        print("No se puede predecir ahora.")
    elif respuesta == 15:
        print("Concéntrate y vuelve a preguntar.")
    elif respuesta == 16:
        print("No cuentes con ello.")
    elif respuesta == 17:
        print("Mi respuesta es no.")
    elif respuesta == 18:
        print("Mis fuentes dicen que no.")
    elif respuesta == 19:
        print("Las perspectivas no son muy buenas.")
    elif respuesta == 20:
        print("Muy dudoso.")
    else:
        print("Hubo un error vuelve a intentarlo más tarde")
    opc = input("Si escribes S el programa volvera a ejecutarse si no quieres eso escribe N: ")
while not opc == "n" or opc != "n":
     print("Hubo un error vuelve a intentarlo")
     opc = input("Si escribes S el programa volvera a ejecutarse si no quieres eso escribe N: ")
print("Muchas gracias por usar el programa ocho")