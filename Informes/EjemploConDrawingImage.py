from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4



guion = []

imagen = Image(400,0,512,233,"foto.jpg")

dibujo = Drawing(50,30)

dibujo.add(imagen)

dibujo.translate(0,0)

guion.append(dibujo)

dibujo.rotate(90)

dibujo.scale(1.5,0.5)

dibujo.translate(-90,300)

guion.append(dibujo)

dibujo = Drawing(50,30)

dibujo.add(imagen)

dibujo.rotate(45)

dibujo.translate(-40,-100)

guion.append(dibujo)

dibujo = Drawing(A4[0],A4[1])

for elemento in guion:
    dibujo.add(elemento)


renderPDF.drawToFile(dibujo,"EjemploConDrawingImage.pdf","Un ejemplo de Drawing con Image")




