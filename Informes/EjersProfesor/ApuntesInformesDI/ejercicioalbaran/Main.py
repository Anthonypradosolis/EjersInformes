import os
from reportlab.graphics.shapes import Drawing, Line
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from conexionBD import ConexionBD

#base de datos
base = ConexionBD("modelosClasicos.dat")
base.conectaBD()
base.creaCursor()

#consultas
consulta_primera_tabla = base.consultaConParametros("select  a.numeroAlbara as nalb, a.dataAlbara, a.numeroCliente as numcliente, a.dataEntrega as dataent, c.nomeCliente as nomcliente, c.apelidosCliente as apecliente from ventas a left join clientes c on c.numeroCliente = a.numeroCliente where c.numeroCliente = 1 LIMIT 1")

consultaTablaUltimaFila1 = base.consultaConParametros("SELECT c.codigoProduto AS cpro, c.nomeProduto AS npro, c.cantidade AS cant FROM produtos c LEFT JOIN detalleVentas v ON v.codigoProduto = c.codigoProduto where c.codigoProduto = ?", 1)

consultaTablaUltimaFila2 = base.consultaConParametros("SELECT c.codigoProduto AS cpro, c.nomeProduto AS npro, c.cantidade AS cant FROM produtos c LEFT JOIN detalleVentas v ON v.codigoProduto = c.codigoProduto where c.codigoProduto = 2")

#estilos parrafos
albaraEstilo = ParagraphStyle(
    name="albaraEstilo",
    fontName="Helvetica",
    textColor=colors.blue,
    fontSize=12
)

detalleEstilo = ParagraphStyle(
    name="detalleEstilo",
    fontName="Helvetica",
    textColor=colors.blue,
    fontSize=12
)

#parrafos
parrafoAlbara = Paragraph("Albará", albaraEstilo)
parrafodetalle = Paragraph("Detalle", detalleEstilo)

# Tabla Inicial
cabecera = ["MODELOS", "CLASICOS"]

tabla_inicio = Table(
    data=[cabecera],
    colWidths=[80, 80],
    rowHeights=29,
)



tabla_inicio.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), colors.black),  # Primera celda con fondo negro
    ('TEXTCOLOR', (0, 0), (0, 0), colors.white),   # Texto blanco en la primera celda

    ('BACKGROUND', (1, 0), (1, 0), colors.white),  # Segunda celda con fondo blanco
    ('TEXTCOLOR', (1, 0), (1, 0), colors.black),   # Texto negro en la segunda celda

    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Texto en negrita para ambas celdas
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centrado
    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.darkgrey),  # Borde exterior
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white),  # Rejilla interna
]))

#tabla_albara

#datos que poner en la tabla

def checkPrimeraConsulta(consulta):
    if consulta:
        nAlb = consulta[0][0]
        dat = consulta[0][1]
        ncliente = consulta[0][2]
        datent = consulta[0][3]
        nomec = consulta[0][4]
        apecli = consulta[0][5]
        return nAlb, dat, ncliente, datent, nomec, apecli

numeroAlbaran, dataAlbaran, numeroCliente, dataEntrega, nomeCliente, apelidoCliente = checkPrimeraConsulta(consulta_primera_tabla)


#elementos
elemento1 = ["Número albará", numeroAlbaran, "Data", dataAlbaran]
elemento2 = ["Número cliente", numeroCliente, "Data entrega", dataEntrega]
elemento3 = ["Nome cliente", nomeCliente, "Apelidos", apelidoCliente]

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

def checkProducto2(consulta):
    if consulta:
        cp = consulta[0][0]
        desc = consulta[0][1]
        cant = consulta[0][2]
        return cp, desc, cant

codigo2, descripcion2, cantidade2 = checkProducto2(consultaTablaUltimaFila2)

#tabla detalle
elemento_detalle_1 = ["Código producto", "descripción", "Cantidade", "Prezo unitario"]
elemento_detalle_2 = [codigo, descripcion, cantidade, "10500"]
elemento_detalle_3 = [codigo2, descripcion2, cantidade2, "45"]

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

#contenidos

contenido_tablaInicio = [tabla_inicio, Spacer(0, 10)]
contenido_parrafo_albara = [parrafoAlbara, Spacer(0, 10)]
contenido_tabla_albara = [tabla_datos1, Spacer(0, 10)]
contenido_parrafo_detalle = [parrafodetalle, Spacer(0, 10)]
contenido_tabla_detalle = [tabla_detalle, Spacer(0, 10)]

frame_tabl1_inicio = Frame(x1=220, y1=650, width=165, height=43, showBoundary=1)
frame_parrafo_albara = Frame(x1=120, y1=620, width=70, height=30, showBoundary=0)
frame_tabla_albara = Frame(x1=120, y1=530, width=320, height=100, showBoundary=0)
frame_contenido_parrafo_detalle = Frame(x1=120, y1=510, width=100, height=30, showBoundary=0)
frame_tabla_detalle = Frame(x1=121, y1=420, width=320, height=100, showBoundary=0)

def generar_contenido(canvas, doc):
    frame_tabl1_inicio.addFromList(contenido_tablaInicio, canvas)
    frame_parrafo_albara.addFromList(contenido_parrafo_albara, canvas)
    frame_tabla_albara.addFromList(contenido_tabla_albara, canvas)
    frame_contenido_parrafo_detalle.addFromList(contenido_parrafo_detalle, canvas)
    frame_tabla_detalle.addFromList(contenido_tabla_detalle, canvas)

doc = BaseDocTemplate("EjercicioAlbaran.pdf", pagesize=A4)
plantilla = PageTemplate(id="Albaran", frames=[frame_tabl1_inicio], onPage=generar_contenido)
doc.addPageTemplates([plantilla])

doc.build([Spacer(0, 1)])
