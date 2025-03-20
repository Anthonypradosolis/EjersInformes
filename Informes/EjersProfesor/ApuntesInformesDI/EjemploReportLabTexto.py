from reportlab.pdfgen import canvas

#lista para las lineas
cadena = ["Tres tristes tigres",  "comen trigo en un trigal", "en que trigal", "comieron los tristes tigres"]

aux = canvas.Canvas("probandoTexto.pdf")

#comenzamos a escribir
objetoTexto = aux.beginText()

#inicio de la escritura
objetoTexto.setTextOrigin(100,500)

#tipo de fuente
objetoTexto.setFont("Helvetica", 12)

#recorremos la lista e insertamos los datos en el objeto
for linea in cadena:
    objetoTexto.textLine(linea)

#cambiamos el tipo del color
objetoTexto.setFillGray(0.5)

otroTexto = """Este es otro texto de muestra para probar las características del dibujo del texto"""

objetoTexto.textLines(otroTexto)

objetoTexto.textLines("")
objetoTexto.textLines("")

#obtenemos el tipo de fuente disponible
for tipo in aux.getAvailableFonts():
    objetoTexto.setFont(tipo, 12)
    objetoTexto.textLine(tipo + ": " + cadena[0])

objetoTexto.setFont("Helvetica", 12)

#cambios de color
objetoTexto.setFillColorRGB(0, 0, 1, 1.0)
for linea in cadena:
    objetoTexto.textOut(linea) #saltos de linea
    objetoTexto.moveCursor(20, 15)

objetoTexto.setFillColorRGB(0, 1, 1)
espazoCar = 0
for linea in cadena:
    objetoTexto.setCharSpace(espazoCar)
    objetoTexto.textLine("Espacio %s : %s" %(espazoCar, linea))
    espazoCar += 1

objetoTexto.setFillGray(0.7)
objetoTexto.setCharSpace(0)
objetoTexto.setWordSpace(8)
objetoTexto.textLines(otroTexto)

aux.drawText(objetoTexto)

aux.showPage()
aux.save()