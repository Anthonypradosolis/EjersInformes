import os

from reportlab.graphics.shapes import Drawing, Line
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Frame, PageTemplate, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table

hojaEstilo = getSampleStyleSheet()

#estilos parrafos
estiloParrafoTitulo = ParagraphStyle(
    name="titulo",
    fontName="Times-Roman",
    fontSize=18,
    textColor=colors.black
)

#Imagenes
imagenEmpresa = Image(os.path.relpath("/home/dam/Descargas/DAM2/DI/2Trimestre/logo2.jpg"),100,20)

#frames
frame_titulo = Frame(
    x1=100, y1=760,
    width=150, height=50,
    showBoundary=1
)

frameImagenEmpresa = Frame(
    x1=300, y1=750,
    width=160, height=60,
    showBoundary=1
)


#parrafos
parrafor_titulo = Paragraph("Factura Proforma", estiloParrafoTitulo)

#templates
plantilla = PageTemplate(id="Factura2", frames=[frame_titulo, frameImagenEmpresa])

doc = SimpleDocTemplate("EjercicioFactura2.pdf", pagesize=A4, showBoundary=0)

doc.addPageTemplates([plantilla])


contenido_factura_titulo = [parrafor_titulo]
contenidoImagenEmpresa = [Spacer(0,20),imagenEmpresa]

doc.build(contenido_factura_titulo + contenidoImagenEmpresa)




