from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

#lista para almacenar los objetos
guion = []

#objeto de tipo imagen
imaxe = Image(400, 0, 100, 100, "/home/dam/Descargas/DAM2/DI/2Trimestre/cocodrilo1.jpeg")

#ponemos un dibujo y metemos la imagen
dibujo = Drawing(50, 30)
dibujo.add(imaxe)
dibujo.translate(-00, 300)

guion.append(dibujo)

dibujo2 = Drawing(50,30)
dibujo2.add(imaxe)
dibujo2.scale(1.5, 0.5)
dibujo2.translate(-0, -500)
dibujo2.rotate(10)

guion.append(dibujo2)

dibujo3 = Drawing(50,30)
dibujo3.add(imaxe)
dibujo3.rotate(45)

dibujo3.translate(-100, -0)
guion.append(dibujo3)

dibujo4 = Drawing(A4[0], A4[1])
for elemento in guion:
    dibujo4.add(elemento)

renderPDF.drawToFile(dibujo4, "pruebasConDrawImage.pdf")