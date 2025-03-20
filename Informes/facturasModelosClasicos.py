from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Spacer
from reportlab.lib import colors
from reportlab.pdfgen import canvas

from conexionBd import ConexionBD

base = ConexionBD("modelosClasicos.dat")
base.conectaBD()
base.creaCursor()

#consultas
consultaDatoCliente = base.consultaConParametros("SELECT nomeCliente, apelidosCliente FROM clientes WHERE numeroCliente = ?", 1)

consultaDatoAlbaran = base.consultaConParametros("SELECT numeroAlbara, dataAlbara FROM ventas WHERE numeroCliente = ?", 1)

consultaDatoFechaClienteAlbaran = base.consultaConParametros("SELECT numeroCliente, dataEntrega FROM ventas WHERE numeroAlbara = ?", 1)

consultaTablaUltimaFila1 = base.consultaConParametros("SELECT c.codigoProduto AS cpro, c.nomeProduto AS npro, c.cantidade AS cant FROM produtos c LEFT JOIN detalleVentas v ON v.codigoProduto = c.codigoProduto where c.codigoProduto = ?", 1)

#tabla_albara

#datos que poner en la tabla
def checkConsultaCliente(consulta):
    if consulta:
        nome = consulta[0][0]
        apelidos = consulta[0][1]
        return nome, apelidos
nome, apelidos = checkConsultaCliente(consultaDatoCliente)

def checkNumeroAlabara(consulta):
    if consulta:
        numeroAlbara = consulta[0][0]
        fecha = consulta[0][1]
        return numeroAlbara, fecha

numeroAlabara, fecha = checkNumeroAlabara(consultaDatoAlbaran)

def checkfechaClienteAlbara(consulta):
    if consulta:
        nCliente =consulta[0][0]
        data_entrega = consulta[0][1]
        print(nCliente, data_entrega)
        return nCliente, data_entrega

numeroCliente, dataEntrega = checkfechaClienteAlbara(consultaDatoFechaClienteAlbaran)



#elementos
elemento1 = ["Número albará", numeroAlabara, "Data", fecha]
elemento2 = ["Número cliente", numeroCliente, "Data entrega", dataEntrega]
elemento3 = ["Nome cliente", nome, "Apelidos", apelidos]

tabla_datos1 = Table(
    [elemento1, elemento2, elemento3],
    colWidths=[80, 80, 80],
    rowHeights=25
)

tabla_datos1.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (0, 0), colors.black),

    #ultimas 2 filas de la primera celda
    ('BACKGROUND', (-2, 0), (-1, 0), colors.blue),
    ('TEXTCOLOR', (-2, 0), (-1, 0), colors.white),

    #ultimas 2 celdas de la segunda fila
    ('BACKGROUND', (-2, 1), (-1, 1), colors.blue),
    ('TEXTCOLOR', (-2, 1), (-1, 1), colors.white),

    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centrado
    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.darkgrey),
]))

#DATOS A METER
def checkProducto1(consulta):
    if consulta:
        cp = consulta[0][0]
        desc = consulta[0][1]
        cant = consulta[0][2]
        return cp, desc, cant

codigo, descripcion, cantidade = checkProducto1(consultaTablaUltimaFila1)

#tabla detalle
elemento_detalle_1 = ["Código producto", "descripción", "Cantidade", "Prezo unitario"]
elemento_detalle_2 = [codigo, descripcion, cantidade, "10500"]
elemento_detalle_3 = [2, "Casco retro", 2, "45"]

tabla_detalle = Table(
    [elemento_detalle_1, elemento_detalle_2, elemento_detalle_3],
    colWidths=[82, 80, 80, 80],
    rowHeights=25
)



tabla_detalle.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),  # Fondo azul claro en la cabecera
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Texto negro en la cabecera
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Texto en negrita
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Fondo blanco para el resto de filas
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),  # Texto negro en el resto de filas
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.darkgrey),
]))


# Estilos
estilo_padre = ParagraphStyle(
    name="padre",
    fontSize=14,
    textColor=colors.black,
    fontName="Helvetica-Bold",
)

estilo_hijo = ParagraphStyle(
    name="hijo",
    fontSize=12,
    textColor=colors.white,
    fontName="Helvetica-Bold",
)

estilo_hijo2 = ParagraphStyle(
    name="hijo2",
    fontSize=12,
    textColor=colors.black,
    fontName="Helvetica-Bold",
)

estilo_detalle = ParagraphStyle(
    name="detalle",
    fontSize=10,
    textColor=colors.blue,
    fontName="Helvetica"
)

estilo_albaran = ParagraphStyle(
    name="albaran",
    fontSize=10,
    textColor=colors.blue,
    fontName="Helvetica"
)

# Contenido
#contenido_padre = [Paragraph("", estilo_padre), Spacer(0, 0)]
contenido_hijo = [Paragraph("MODELOS", estilo_hijo)]
contenido_hijo2 = [Paragraph("CLASICOS", estilo_hijo2)]
contenido_detalle = [Paragraph("Detalles",estilo_detalle)]
contenido_albaran = [Paragraph("Albaran",estilo_albaran)]
contenido_tabla_albaran = [tabla_datos1, Spacer(0,10)]
contenido_tabla_detalle = [tabla_detalle, Spacer(0, 10)]


# Frames
frame_padre = Frame(x1=200, y1=750, width=150, height=40, showBoundary=1)
frame_hijo = Frame(x1=205, y1=760, width=75, height=25, showBoundary=0)
frame_hijo2 = Frame(x1=275, y1=760, width=75, height=25, showBoundary=0)
frame_albaran = Frame(x1=75, y1=660, width=60, height=25, showBoundary=0)
frame_detalle = Frame(x1=75, y1=500, width=60, height=25, showBoundary=0)
frame_tabla_albaran = Frame(x1=175, y1=550, width=100, height=100, showBoundary=0)
frame_tabla_detalles = Frame(x1=175, y1=400, width=100, height=100, showBoundary=0)

# Método para generar contenido
def generar_contenido(canvas, doc):
    # Dibujar fondo del frame padre
   # canvas.setFillColor(colors.darkblue)
   # canvas.rect(100, 10, 300, 150, fill=1, stroke=0)  # Frame Padre (x, y, width, height)

    # Dibujar fondo del frame hijo
    canvas.setFillColor(colors.black)
    canvas.rect(205, 755, 75, 30, fill=1, stroke=0)  # Frame Hijo

    # Agregar contenido sobre los fondos
    #frame_padre.addFromList(contenido_padre, canvas)
    frame_hijo.addFromList(contenido_hijo, canvas)
    frame_hijo2.addFromList(contenido_hijo2, canvas)
    frame_detalle.addFromList(contenido_detalle,canvas)
    frame_tabla_detalles.addFromList(contenido_tabla_detalle, canvas)
    frame_albaran.addFromList(contenido_albaran, canvas)
    frame_tabla_albaran.addFromList(contenido_tabla_albaran,canvas)


# Plantilla de página
doc = BaseDocTemplate("facturasModelosClasicos1.pdf", pagesize=A4)
plantilla = PageTemplate(id="AnidadoConFondos", frames=[frame_padre, frame_hijo], onPage=generar_contenido)
doc.addPageTemplates([plantilla])

# Construcción del documento
doc.build([Spacer(0, 1)])