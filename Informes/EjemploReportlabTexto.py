from reportlab.pdfgen import canvas

cadena = ("Tres tristes tigres",
          "comeron trigo nun trigal ","en que trigal","comeron os tristes" )

aux = canvas.Canvas("probaTexto.pdf")
objetoTexto = aux.beginText()

objetoTexto.setTextOrigin(100,800)
objetoTexto.setFont("Helvetica",12)

for linha in cadena:
    objetoTexto.textLine(linha)
objetoTexto.setFillGray(0.5)
otroTexto = """Este es otro texto de
    mostrar para probar as
    caracteristicas de 
    debujo de texto"""

objetoTexto.textLines(otroTexto)
objetoTexto.textLine("")
objetoTexto.textLine("")
for tipo in aux.getAvailableFonts():
    objetoTexto.setFont(tipo,12)
    objetoTexto.textLine(tipo+": "+cadena[0])

objetoTexto.setFont("Helvetica",12)
objetoTexto.setFillColorRGB(1,0,0,1.0)

for linha in cadena:
    objetoTexto.textOut(linha)
    objetoTexto.moveCursor(20,15)

objetoTexto.setFillColorRGB(0,1,1)
espacioCar = 0

for linha in cadena:
    objetoTexto.setCharSpace(espacioCar)
    objetoTexto.textLine("Espacio %s : %s" % (espacioCar,linha))
    espacioCar += 1

objetoTexto.setFillGray(0.7)
objetoTexto.setWordSpace(8)
objetoTexto.textLines(otroTexto)

aux.drawText(objetoTexto)

aux.showPage()
aux.save()