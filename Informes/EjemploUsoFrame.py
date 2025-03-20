import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame, Image, Spacer
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm


objetoCamvas = Canvas(os.path.realpath("EjemploUsoFrame.pdf"))

follaEstilo = getSampleStyleSheet()

estNormal = follaEstilo["Normal"]
estCorpoT = follaEstilo["BodyText"]

documento = []

imaxen = Image(os.path.realpath("foto.jpg"))
documento.append(imaxen)
documento.append(Spacer(0,20))

documento.append(Paragraph("Texto que se vai a repetir multiple veces e facer un voluminoso documento.",estNormal))


frame = Frame(cm, cm, cm*2,cm*2, showBoundary=0)
frame.addFromList(documento,objetoCamvas)


doc2=[]

doc2.append(Paragraph("Texto que se vai a repetir multiple veces e facer un voluminoso documento.",estCorpoT))
doc2.append(Spacer(0,20))

imaxen2 = Image(os.path.realpath("foto.jpg"),32,32)

doc2.append(imaxen2)

frame2 = Frame(350,3*cm, 200, 200,cm, showBoundary=1)

frame2.addFromList(doc2,objetoCamvas)

objetoCamvas.save()


