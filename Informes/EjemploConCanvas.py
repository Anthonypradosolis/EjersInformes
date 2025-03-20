# Utilizando pdfgen
# Objeto Canvas

from reportlab.pdfgen import canvas


papel = canvas.Canvas("primerDocumento.pdf")

papel.drawString(0, 0, "Posicion 0,0 = (0,0)")
papel.drawString(50, 100, "Posicion 50,100 = (50,100)")
papel.drawString(500, 700, "Posicion 500,700 = (500,700)")

papel.drawImage("python-logo.png", 100, 100, width=100, height=100)

papel.save()
