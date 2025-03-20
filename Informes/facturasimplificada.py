import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, SimpleDocTemplate, Image


def generar_factura(output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # Encabezado
    title_style = styles["Title"]
    title_style.alignment = 2  # 2 es para alinear a la derecha
    elements.append(Paragraph("<b>FACTURA SIMPLIFICADA</b>", title_style))
    elements.append(Spacer(1, 12))

    # Añadir logo y nombre de la empresa en una tabla
    logo = Image("patito3.png")  # Reemplaza con la ruta a tu logo
    logo.drawHeight = 50  # Ajusta el tamaño según sea necesario
    logo.drawWidth = 50
    empresa_nombre = Paragraph("<b>Revevic</b>", styles["Heading1"])

    header_table = Table([[empresa_nombre,logo]], colWidths=[400, 50])
    header_table.setStyle(TableStyle([
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))

    elements.append(header_table)
    elements.append(Spacer(1, 12))

    # Datos de empresa e información de factura en dos columnas
    empresa_info = [
        [Paragraph("<i>Dirección</i>", styles["Normal"])],
        [Paragraph("<i>Ciudad y País</i>", styles["Normal"])],
        [Paragraph("<i>CIF/NIF</i>", styles["Normal"])],
        [Paragraph("<i>Teléfono</i>", styles["Normal"])],
        [Paragraph("<i>Mail</i>", styles["Normal"])]
    ]

    factura_info = [
        ["", ""],  # Espacio vacío para bajar los datos
        ["", ""],
        [Paragraph("<b>Fecha Emisión:</b> DD/MM/AAAA", styles["Normal"]), ""],
        [Paragraph("<b>Número de Factura:</b> A0001", styles["Normal"]), ""]
    ]

    # Convertir en tabla con dos columnas
    empresa_factura_table = Table([
        [empresa_info[0][0], ""],
        [empresa_info[1][0], ""],
        [empresa_info[2][0], ""],
        [empresa_info[3][0], factura_info[2][0]],  # Teléfono | Fecha Emisión
        [empresa_info[4][0], factura_info[3][0]],  # Mail | Número Factura
    ], colWidths=[250, 200])

    empresa_factura_table.setStyle(TableStyle([
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
    ]))

    elements.append(empresa_factura_table)
    elements.append(Spacer(1, 12))

    # Datos de la factura
    data = [
        ["Descripción", "Importe", "Cantidad", "Total"],
        ["Producto 1", "3,2", "5", "16,00"],
        ["Producto 2", "2,1", "3", "6,30"],
        ["Producto 3", "2,9", "76", "220,40"],
        ["Producto 4", "5", "23", "115,00"],
        ["Producto 5", "4,95", "3", "14,85"],
        ["Producto 6", "6", "2", "12,00"],
        ["", "", "TOTAL", "385 €"]
    ]

    # Aumentar altura de la última fila para centrar bien el texto
    table = Table(data, colWidths=[200, 80, 80, 80], rowHeights=[None] * 7 + [40])  # Última fila más alta
    table.setStyle(TableStyle([
        # Cabecera
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

        # Celdas de TOTAL y 385€ más grandes y centradas
        ('BACKGROUND', (-2, -1), (-1, -1), colors.darkgreen),
        ('TEXTCOLOR', (-2, -1), (-1, -1), colors.whitesmoke),
        ('FONTNAME', (-2, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (-2, -1), (-1, -1), 12),  # Texto más grande
        ('ALIGN', (-2, -1), (-1, -1), 'CENTER'),
        ('VALIGN', (-2, -1), (-1, -1), 'MIDDLE'),  # Centrado vertical

        # Fondo para las otras celdas
        ('BACKGROUND', (0, 1), (-1, -2), colors.honeydew),

        # Bordes blancos
        ('GRID', (0, 0), (-1, -1), 1, colors.white),

        # Alineaciones generales
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    elements.append(table)

    # Construcción del documento
    doc.build(elements)
    print(f"Factura generada: {output_filename}")


# Ejecutar la función
generar_factura("factura.pdf")