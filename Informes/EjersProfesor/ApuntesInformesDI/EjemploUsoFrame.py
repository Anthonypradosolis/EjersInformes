import os

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Frame, Image, Spacer

from EjemploPlatypus import hojaEstilo

objectoCanvas = Canvas(os.path.relpath("ejemploUsoFrame.pdf"))
follaEstilo = getSampleStyleSheet()

estNormal = follaEstilo["Normal"]
estCorpot = follaEstilo["BodyText"]

documento = []

imagen = Image(os.path.relpath("/home/dam/Descargas/DAM2/DI/2Trimestre/cocodrilo.jpg"))
documento.append(imagen)
documento.append(Spacer(0, 20))

documento.append(Paragraph("Si me dices tonto, eres racista. Soy el balón de oro", estNormal))

frame = Frame(cm, cm,  cm*13, cm*13, showBoundary=1)
frame.addFromList(documento, objectoCanvas)

docs2 = [Paragraph("Segundo frame, distinto al anterior"), Spacer(0, 20)]
imagen2 = Image(os.path.relpath("/home/dam/Descargas/DAM2/DI/2Trimestre/cocodrilo1.jpeg"))

frame2 = Frame(100, 3*cm, cm*20, cm*20, cm, showBoundary=1)
docs2.append(imagen2)

frame2.addFromList(docs2, objectoCanvas)


objectoCanvas.save()


