#utilizando pdfgen
#objeto canvas

from reportlab.pdfgen import canvas

#creamos el canva y le metemos el nombre del pdf
papel = canvas.Canvas("primerDocumento.pdf")

#metodo para dibujar un String
papel.drawString(0, 0, "Posición original (x,y) = (0, 0)")
papel.drawString(50, 100, "Posición original (x,y) = (50, 100)")
papel.drawString(500, 700, "Posición original (x,y) = (500, 700)")

papel.drawImage("/home/dam/Descargas/DAM2/DI/2Trimestre/NileCrocodile.jpg", 100, 300, 200,200)
papel.drawImage("/home/dam/Descargas/DAM2/DI/2Trimestre/NileCrocodile.jpg", 320, 300, 250, 220)

papel.showPage()
papel.save()