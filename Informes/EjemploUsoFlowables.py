import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.pdfgen.canvas import Canvas

follaEstilo = getSampleStyleSheet()

estilo = follaEstilo["BodyText"]

parragrafo = Paragraph("O texto  que imos mostrar")

objetoCanvas = Canvas(os.path.realpath("EjemploUsoFlowables.pdf"))

ancho, alto = 300,300

anchoAux, altoAux = parragrafo.wrap(ancho,alto)
print()

if anchoAux <= ancho and altoAux <= alto:
    ancho = ancho-altoAux
    parragrafo.drawOn(objetoCanvas,0,altoAux)
    objetoCanvas.save()
else:
    raise ValueError("O texto non cabe na folla")
