print('''
                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
 pb  /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)
''')

print("Bienvenidx al Estado de México.")
print("Tu misión es escapar de este estado de kk.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

con1 = "Acabas de entrar a Ecatepec. Te balasiaron los municipales. Perdiste."

con2 = "Un tipo se te acerca para pedirte la hora. Perdiste."

con3_1 = "Has entrado más en el EdoMex, ahora nunca podrás escapar. Obvio perdiste."

con3_2 = "Acabas de entrar a un terreno baldío. Perdiste."

con3_3 = "Acabas de confundir al mototaxista, ahora procederá a asaltarte. Perdiste."

con_fin = "Acabas de ver una estación del Mexibús. Ahora podrás salir de ese lugar abandonado por Dios. ¡Ganaste!"

#########################################

fase1 = input('Estás en un puesto de tacos, por ahora estás seguro, pero debes avanzar, ¿A dónde quieres ir?\nEscribe "izquierda" o "derecha".\n')

if fase1 == "izquierda":
  print('\n¡Buena elección! Continúa con tu odisea.\n')
  fase2 = input('Acabas de llegar a un paradero. Puedes seguir caminando o en mototaxi, sólo recuerda que el pasaje es muy caro.\nEscribe "caminar" para irte caminando o "mototaxi" para subirte a un mototaxi.\n')

  if fase2 == "mototaxi":
    print("\nMuy prudente de tu parte. A pesar del precio de los pasajes, nada vale más que nuestras vidas.\n")
    fase3 = input('Ya estás en el mototaxi, ahora estás en un cruce, ¿a dónde debe ir el mototaxista?\n\nEscribe "derecha" o "izquierda" para dar vuelta, "adelante" para seguir todo derecho o "detenerse" para quedarse en el cruce.\n')

    if fase3 == "detenerse":
      print(con_fin)
    elif fase3 == "izquierda":
      print(con3_1)
    elif fase3 == "derecha":
      print(con3_2)
    else:
      print(con3_3)
  else:
    print(con2)
else:
  print(con1)