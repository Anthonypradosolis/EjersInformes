import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.pdfgen.canvas import Canvas

follaEstilo = getSampleStyleSheet()
estilo = follaEstilo['BodyText']

parrafo = Paragraph("O texto que imos mostrar con mas longitud para que no entre aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

objetoCanvas = Canvas(os.path.relpath('ejemploFlowable.pdf'))

ancho, alto = 300, 300

anchoAux, altoAux = parrafo.wrap(ancho, alto)
print(str(anchoAux) + " " + str(altoAux))

if anchoAux <= ancho and altoAux <= alto:
    ancho = anchoAux - anchoAux
    parrafo.drawOn(objetoCanvas, 0, altoAux)
    objetoCanvas.save()
else:
    raise ValueError("No hay espacio suficiente")
