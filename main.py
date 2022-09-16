import time
print("Bienvenido a mi trivia sobre el imperio incaico")
print("Pondremos a prueba tus conocimientos\n")
print(
    "Iniciaremos con 0 puntos por cada pregunta  bien contestada tedaremos 5 puntos y por cada  mal contestada te quitaremos 2 puntos \n "
)
intentos = int = 0
iniciar_trivia = True
while iniciar_trivia == True:
  intentos += 1
  puntos = int = 0

  print(" Ingresa tu nombre:")
  nombre = input()


  print("\n", nombre, "tienes", 
 puntos, "puntos.")


  print(
    "\n", nombre,
    "Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n"
)

  print("1) ¿Quién fue el fundador del imperio inca?\n")
  print("a) Pachacutec")
  print("b) Manco Capac")
  print("c) Sinchi Roca")

  respuesta = input("\n Ingresa tu respuesta:")

  while respuesta not in("a", "b", 
"c" ):     
    respuesta = input("Solo puedes ingresar a, b, o c. Ingresa nuevamente tu respuesta\n").lower()

  if (respuesta == "a"):
    print("!Incorrecto¡", nombre, "\n")
    puntos -= 2
  elif (respuesta == "b"):
    print("!Muy bien¡", nombre, "\n")
    puntos += 5
  elif (respuesta == "c"):
    print("!Incorrecto¡", nombre, "\n")
    puntos -= 2

  print(nombre, "tienes", puntos, "puntos.\n")

  print(
    "2) El imperio inca o tahuantinsuyo fue el mas grande de America.¿Sabes que territorios abarco?\n"
)

  print("a) Perú, Colombia,Chile,Bolivia,Ecuador y Argentina")
  print("b) Ecuador,perú y Bolivia")
  print("c) Perú y Bolivia")

  respuesta_1 = input("\nIngresa tu respueta:")

  while respuesta_1 not in ("a", "b", "c"):
    respuesta_1 = input("Solo puedes ingresar a, b, o c. Ingresa nuevamente tu respuesta\n"
    ).lower()

  if (respuesta_1 == "a"):
    print("!Muy Bien¡", nombre, "\n")
    puntos += 5
  elif (respuesta_1 == "b"):
    print("!Incorrecto¡", nombre, "\n")
    puntos -= 2
  elif (respuesta_1 == "c"):
    print("!Incorrecto¡", nombre, "\n")
    puntos -= 2

  print(nombre, "tienes", puntos, "puntos.\n")

  print(
    "3) Los gobernadores incas eran considerados hijos del sol ¿sabes el nombre de esta divinidad?\n"
)

  print("a) Viracocha")
  print("b) Pachacamac")
  print("c) Inti")

  respuesta_2 = input("\nIngresa tu respueta:")

  while respuesta_2 not in ("a", "b", "c"):
    respuesta_2 = input("Solo puedes ingresar a, b, o c. Ingresa nuevamente tu respuesta\n"
    ).lower()

  if (respuesta_2 == "a"):
    print("!Incorrecto¡", nombre, "\n")
    puntos -= 2
  elif (respuesta_2 == "b"):
    print("!Incorrecto¡", nombre, "\n")
    puntos -= 2
  elif (respuesta_2 == "c"):
    print("!Muy Bien¡", nombre, "\n")
    puntos += 5

  print(nombre, "tienes", puntos, "puntos.\n")

  print(
    "4) ¿Sabes como trataban los incas alas momias de sus gobernantes muertos.?\n "
)

  print("a) Los embalsamaban,los momificaban y los tiraban al mar")
  print("b) No recibian ningun trato en especial")
  print("c) Los trataban como si estuvieran vivos y los hacian participar en multiples actividades sociales")

  respuesta_3 = input("\nIngresa tu respueta:")

  while respuesta_3 not in ("a", "b", "c"):
    respuesta_3 = input("Solo puedes ingresar a, b, o c. Ingresa nuevamente tu respuesta\n"
    ).lower()

  if (respuesta_3 == "a"):
    print("!Incorrecto¡", nombre, "\n")
    puntos -= 2
  elif (respuesta_3 == "b"):
    print("!Incorrecto¡", nombre, "\n")
    puntos -= 2
  elif (respuesta_3 == "c"):
    print("!Muy Bien¡", nombre, "\n")
    puntos += 5 

  print(nombre, "tienes", puntos, "puntos.\n")

  print("Cargando resultados")
  time.sleep(2)

  if(puntos <= 0):
    print(nombre,"tu puntaje es de ",puntos,"puntos.")
    print(nombre,"Sos re malo pero te invito a practicar y  que lo vuelvas a intentar.\n")
    
  elif(puntos >= 1 and puntos <= 10):
   print(nombre,"tu puntaje es de",puntos,"puntos.")
   print(nombre,"Te invito a practicar  y que lo vuelvas  a intentar.\n") 
  elif(puntos >= 11 and puntos <= 19):
   print(nombre,"tu puntaje es de",puntos,"puntos.")
   print(nombre,"!MUY BIEN¡ vuelve a intentarlo para conseguir el maximo puntaje. \n")
  elif(puntos >= 20):
   print(nombre,"tu  puntaje es de",puntos,"puntos")
   print(nombre,"!RE BIEN¡ Felicitaciones conseguiste el puntaje maximo. ")

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  
  if (repetir_trivia != "si"):
   print(" Gracias por jugar mi trivia",nombre," espero que la hayas pasado bien vuelve a intentarlo cuando lo desees")
  iniciciar_trivia = False
    
   

  

  
