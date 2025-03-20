import os

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.graphics.charts.barcharts import VerticalBarChart, VerticalBarChart3D
from reportlab.graphics.charts.linecharts import LineChart, HorizontalLineChart
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.piecharts import Pie, Pie3d


from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table

from EjemploUsoFlowables import ancho

hojaEstilo = getSampleStyleSheet()

documento = []

cabecera = hojaEstilo['Heading1']
cabecera.pageBreakBefore = 4
cabecera.keepWithNext = 0
cabecera.backColor = colors.blue

parrafo1 = Paragraph("Cabecera del documento", cabecera)

documento.append(parrafo1)

cadena = "vinicius balon de oro, vinicius balon de oro, vinicius balon de oro" * 1000

estiloP = hojaEstilo['BodyText']
parrafo2 = Paragraph(cadena, estiloP)

documento.append(parrafo2)

documento.append(Spacer(0, 20))
imagen = Image(os.path.relpath("/home/dam/Descargas/DAM2/DI/2Trimestre/cocodrilo.jpg"), width=150, height=150)
documento.append(imagen)

documento.append(Spacer(0, 20))
# listas para la tabla
cabeceira = ['', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
manhana = ['Mañana', 'Estudiar', 'Gimnasio', 'Jugar', 'correr', 'ver al madrid', 'cagar', 'descansar']
tarde = ['Tarde', 'Trabajar', 'Trabajar', 'Cagar', 'Trabajar', 'Trabajar', 'descanso', 'cagar']
Noche = ['Noche', 'descanso', 'Trabajar', 'descanso', 'Trabajar', 'salir', 'descanso', 'furbol']

# se crea la tabla añadiendole la lista
tabla = Table([cabeceira, manhana, tarde, Noche])
documento.append(tabla)

# diferentes estilos para la tabla
tabla.setStyle([('BACKGROUND', (1, 1), (-1, -1), colors.lightgrey)])  # fondo de la tabla
tabla.setStyle([('BOX', (1, 1), (-1, -1), 0.5, colors.darkgrey)])  # caja que engloba la tabla
tabla.setStyle([('INNERGRID', (1, 1), (-1, -1), 0.25, colors.white)])  # lineas de la tabla
tabla.setStyle([('TEXTCOLOR', (0, 0), (0, -1), colors.red)])  # texto de la tabña izquierda
tabla.setStyle([('TEXTCOLOR', (1, 0), (-1, 0), colors.pink)])  # texto de la tabla arriba
tabla.setStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')])

documento.append(Spacer(0, 20))

datos = [['Esquina sup', '', '02', '03', '04'],
         ['', '', '12', '13', '14'],
         ['20', '21', '22', 'Esquina inf', ''],
         ['30', '31', '32', '', '']]

estilo = [('LINEABOVE', (0, 0), (4,0), 1, colors.blue),
          ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
          ('BACKGROUND', (0, 0), (1, 1), colors.lavenderblush),
          ('SPAN', (0, 0), (1, 1)),
          ('BACKGROUND', (-2, -2), (-1, -1), colors.bisque),
          ('SPAN', (3, 2), (-1, -1)),
          ('LINEBELOW', (0, -1), (-1, -1), 1, colors.blue),
          ('VALIGN', (0,0), (1,1), 'MIDDLE'),
          ('VALIGN', (-2, -2), (-1,-1), 'MIDDLE'),
          ('ALIGN', (0,0), (-1,-1), 'CENTER')]

tabla2 = Table(data=datos, style=estilo)
documento.append(tabla2)

documento.append(Spacer(0, 20))

temperaturaTablas = [['','Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec'],
                     ['Máximas', 15, 16, 20, 25, 27, 31, 35, 38, 33, 25, 20, 18],
                     ['Mínimas', -3, -4, -1, 5, 7, 9, 12, 15, 16, 10, 2, -1]]


estiloTablaTemperaturas = [('TEXTCOLOR', (0,0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0,1), (0, -1), colors.grey),
                           ('BOX', (1,1), (-1,-1), 1.5, colors.grey),
                           ('INNERGRID', (1,1), (-1, -1), 0.5, colors.grey)]


for i, fila in enumerate(temperaturaTablas):
    for j, valor in enumerate(fila):
        if type(valor) == int:
            if valor > 0:
                estiloTablaTemperaturas.append(('TEXTCOLOR', (j,i), (j,i), colors.black))
                if valor > 30:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j,i), (j,i), colors.red))
                elif 30 >= valor > 20:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j,i), (j,i), colors.orange))
                elif 20 >= valor > 10:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j, i), (j, i), colors.lightpink))
                elif 10 >= valor > 0:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j, i), (j, i), colors.lightblue))
            else:
                estiloTablaTemperaturas.append(('TEXTCOLOR', (j, i), (j, i), colors.blue))
                estiloTablaTemperaturas.append(('BACKGROUND', (j, i), (j, i), colors.lightgrey))

tabla3 = Table(data = temperaturaTablas, style=estiloTablaTemperaturas)
documento.append(tabla3)

#graficos

grafica = VerticalBarChart()
#grafica2 = VerticalBarChart3D()
dibujo = Drawing(400, 200)
dibujo.add(grafica)
documento.append(Spacer(0, 20))
documento.append(dibujo)

grafica.x = 50
grafica.y = 50
grafica.height = 125
grafica.width = 300

grafica.strokeColor = colors.black #esta linea si la dejas en 3D genera error
grafica.valueAxis.valueMin = -10
grafica.valueAxis.valueMax = 50
grafica.valueAxis.valueStep = 5

grafica.categoryAxis.labels.boxAnchor = 'ne'
grafica.categoryAxis.labels.dx = 8
grafica.categoryAxis.labels.dy = -2
grafica.categoryAxis.labels.angle = 30
grafica.categoryAxis.categoryNames = temperaturaTablas[0][1:]
grafica.groupSpacing = 10 #agrupas los 2 como datos, tanto maxima como minima pero los separas de los demás
grafica.barSpacing  = 2 #separacion de unidades de enero, febrero...
grafica.bars[0].fillColor = colors.fidred
grafica.bars[1].fillColor = colors.lightblue #cambiar el color de la barra
grafica.bars[1].strokeColor = colors.pink #color de la lina del grafico
grafica.data = [temperaturaTablas[1][1:], temperaturaTablas[2][1:]] #datos que recibe la gráfica


#grafica de lineas
grafica2 = HorizontalLineChart()
dibujoLineChart = Drawing(400, 200)
dibujoLineChart.add(grafica2)
documento.append(dibujoLineChart)

#propiedades graficos 2
documento.append(Spacer(0, 20))

grafica2.x = 30
grafica2.y = 50
grafica2.height = 125
grafica2.width = 350

grafica2.data = [temperaturaTablas[1][1:], temperaturaTablas[2][1:]]

grafica2.categoryAxis.categoryNames = temperaturaTablas[0][1:]
grafica2.categoryAxis.labels.boxAnchor = 'ne'
grafica2.valueAxis.valueMin = -10
grafica2.valueAxis.valueMax = 50
grafica2.valueAxis.valueStep = 10
grafica2.lines[0].strokeWidth = 2
grafica2.lines[0].symbol = makeMarker('FilledCircle')
grafica2.lines[1].strokeWidth = 1.5
grafica2.lines[0].strokeColor = colors.red
grafica2.lines[1].strokeColor = colors.blue


dibujoPlot = Drawing(400, 200)

etiqueta = Label()
etiqueta.setOrigin(175, 195)
etiqueta.dx = 0
etiqueta.dy = -5
etiqueta.boxStrokeColor = colors.grey
etiqueta.setText("Una grafica\n con 2 series")
dibujoPlot.add(etiqueta)


grafica3 = LinePlot()
dibujoPlot.add(grafica3)

datosPlot = [
    ((1,1), (2,2), (2.5,2), (3,3.5), (4,7)),
    ((1,2), (2,3), (2.5,1), (3.5, 3), (4,2))
]
grafica3.data = datosPlot
grafica3.x = 30
grafica3.y = 50
grafica3.height = 125
grafica3.width = 350

grafica3.joinedLines = 1
grafica3.fillColor = colors.lightsalmon
grafica3.lines[0].symbol = makeMarker('FilledCircle')
grafica3.lines[1].symbol = makeMarker('Triangle')
grafica3.lineLabelFormat = '%2.0f'
grafica3.strokeColor = colors.gray
grafica3.xValueAxis.valueMin = 0
grafica3.xValueAxis.valueMax = 5
grafica3.yValueAxis.valueMin = 0
grafica3.yValueAxis.valueMax = 8
grafica3.yValueAxis.valueSteps = [1,2,3,5,6]
grafica3.lines[0].strokeColor = colors.red
grafica3.lines[1].strokeColor = colors.blue


#lineas de line legend
leyenda = LineLegend()
leyenda.fontName = 'Helvetica'
leyenda.fontSize = 7
leyenda.alignment = 'right'

leyenda.x = 30
leyenda.y = 20
leyenda.columnMaximum = 2
etiquetas = ['Caso 1', 'Caso2']

#leyenda.colorNamePairs = [(grafica3.lines[i].strokeColor, etiquetas[i]) for i in range(len(grafica3.data))]

leyenda.colorNamePairs = [(colors.red, etiquetas[0]), (colors.blue, etiquetas[1])]
dibujoPlot.add(leyenda)
documento.append(dibujoPlot)

documento.append(Spacer(0, 20))

#graficos de tartitas bonitas
dibujotarta = Drawing(300, 200)
#tartita = Pie()
tartita = Pie3d()
tartita.x = 60
tartita.y = 15
tartita.width = 200
tartita.height = 130
tartita.data = [8, 6, 2, 4, 7, 3]
tartita.labels = ["AD", "PMDM", "EIE", "SXE", "DI", "PSP"]


tartita.slices.strokeWidth = 0.5 #en que rodajas se va a dividir la tartita bonita
tartita.slices[4].popout = 10
tartita.slices[4].strokeWidth = 2
tartita.slices[4].strokeDashArray = [2,2] #porcion del dibujo de negro y blanco
tartita.slices[4].labelRadius = 1.75 # se desplaza el trozo de tarta
tartita.slices[4].fontColor = colors.red #destacar las letras de la tarta
tartita.sideLabels = 1 #señala a las letras de las etiquetas
tartita.slices.labelRadius = 2.1


leyendaTartita = Legend()
leyendaTartita.x = 370
leyendaTartita.y = 10
leyendaTartita.dx = 8
leyendaTartita.dy = 8

leyendaTartita.fontName = "Helvetica"
leyendaTartita.fontSize = 7
leyendaTartita.boxAnchor = 'n'
leyendaTartita.columnMaximum = 10
leyendaTartita.strokeWidth = 1
leyendaTartita.strokeColor = colors.black
leyendaTartita.deltax = 75
leyendaTartita.deltay = 10
leyendaTartita.autoXPadding = 5
leyendaTartita.yGap = 0
leyendaTartita.dxTextSpace = 5
leyendaTartita.alignment = 'right'
leyendaTartita.dividerLines = 1|2|4 #cuales son las lineas divisorias
leyendaTartita.dividerOffsY = 4.5
leyendaTartita.subCols.rpad = 30

cores = [colors.red, colors.blue, colors.green, colors.orange, colors.yellow, colors.pink]
for i, color in enumerate(cores):
    tartita.slices[i].fillColor = color

leyendaTartita.colorNamePairs = [(tartita.slices[i].fillColor, (tartita.labels[i][0:20], '%0.2f' %tartita.data[i])) for i in range(len(tartita.data))]



dibujotarta.add(tartita)
dibujotarta.add(leyendaTartita)
documento.append(dibujotarta)


doc = SimpleDocTemplate("EjemploPlatypusTabla.pdf", pagesize=A4, showBoundary=1)
doc.build(documento)
