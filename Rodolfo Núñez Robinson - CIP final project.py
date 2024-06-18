import tkinter as tk
from tkinter import ttk
from docx import Document

root = tk.Tk()
root.title("Formulario de solicitud de desalojo notarial por vencimiento de plazo")

fields = ["NOMBRE DEL NOTARIO",
          "NOMBRE DEL DEMANDANTE TAL COMO FIGURA EN SU DNI",
          "NÚMERO DE SU DNI",
          "DIRECCIÓN DE SU DOMICILIO",
          "FECHA DE LA ESCRITURA PÚBLICA",
          "DIRECCIÓN DEL INMUEBLE",
          "NÚMERO DE LA PARTIDA REGISTRAL DE SU INMUEBLE",
          "NOMBRE DEL DEMANDADO",
          "FECHA DE TÉRMINO DEL CONTRATO",
          "CLAUSULA EN DONDE FIGURA LA FECHA DE TÉRMINO DEL CONTRATO",
          "TIPO DE DOCUMENTO DEL DEMANDADO",
          "NÚMERO DE DOCUMENTO DEL DEMANDADO",
          "DOMICILIO FISCAL DEL DEMANDADO",
          "PLAZO DEL CONTRATO",
          "FECHA DE INICIO DEL CONTRATO",
          "CLAUSULA DE COMPETENCIA NOTARIAL",
          "CLÁUSULA EN DONDE FIGURA LA INDIVIDUALIZACIÓN DEL BIEN",
          "ÁREA DEL INMUEBLE EN NÚMEROS",
          "ÁREA CONSTRUIDA DEL INMUEBLE EN NÚMEROS",
          "ASIENTO REGISTRAL EN DONDE OBRA EL DETALLE DE LAS MEDIDAS DEL INMUEBLE",
          "CLÁUSULA EN DONDE FIGURA EL SOMETIMIENTO A LA COMPETENCIA NOTARIAL",
          "CLÁUSULA EN DONDE SE ESTABLECE LA MONEDA DEL PAGO",
          "MONEDA",
          "MONTO DE LA RENTA EN NÚMEROS",
          "MONTO DE LA RENTA EN LETRAS",
          "NÚMERO DE LA CUENTA BANCARIA",
          "NOMBRE DEL BANCO",
          "FECHA DE PRESENTACIÓN DEL DOCUMENTO"]

input_values = {}

def generate_document():
    template = """
SEÑOR NOTARIO PÚBLICO DE LIMA {NOMBRE DEL NOTARIO}:

{NOMBRE DEL DEMANDANTE TAL COMO FIGURA EN SU DNI}, con DNI N° {NÚMERO DE SU DNI}, con domicilio {DIRECCIÓN DE SU DOMICILIO}; ante usted me presento y atentamente digo: 

Mediante contrato de arrendamiento elevado a Escritura Pública del {FECHA DE LA ESCRITURA PÚBLICA}, le arrendé el inmueble de mi propiedad sito en {DIRECCIÓN DEL INMUEBLE} que corre inscrito en la Partida N° {NÚMERO DE LA PARTIDA REGISTRAL DE SU INMUEBLE} del Registro de Propiedad Inmobiliaria de Lima, para que {NOMBRE DEL DEMANDADO} lo destine al uso fijado en el contrato. Este tuvo como fecha de término el {FECHA DE TÉRMINO DEL CONTRATO} según la Cláusula {CLAUSULA EN DONDE FIGURA LA FECHA DE TÉRMINO DEL CONTRATO}. 

Habiéndose vencido en exceso el plazo de vigencia del contrato de arrendamiento sin que {NOMBRE DEL DEMANDADO} restituya el inmueble, y siendo que las partes nos hemos sometido a la competencia notarial y a lo regulado por la Ley N° 30933, acudimos a usted para que proceda con el desalojo notarial. 

I. INFORMACIÓN DEL ARRENDATARIO

1.1. {NOMBRE DEL DEMANDADO}, con {TIPO DE DOCUMENTO DEL DEMANDADO} N° {NÚMERO DE DOCUMENTO DEL DEMANDADO}, quien deberá ser notificado en las siguientes direcciones:

- Domicilio fiscal sito en la {DOMICILIO FISCAL DEL DEMANDADO}; y,

- Inmueble ocupado precariamente sito en {DIRECCIÓN DEL INMUEBLE}.

II. ANTECEDENTES RELEVANTES

2.1. Soy propietario del inmueble situado en {DIRECCIÓN DEL INMUEBLE} que corre inscrito en la Partida N° {NÚMERO DE LA PARTIDA REGISTRAL DE SU INMUEBLE} del Registro de Propiedad Inmobiliaria de Lima (en adelante, el “Inmueble”). 

2.2. Como mencioné, el Inmueble fue objeto del contrato de arrendamiento suscrito entre {NOMBRE DEL DEMANDADO} y mi persona, el cual fue elevado a Escritura Pública con fecha {FECHA DE LA ESCRITURA PÚBLICA}. En este acto, se acordó en la Cláusula {CLAUSULA EN DONDE FIGURA LA FECHA DE TÉRMINO DEL CONTRATO} que el plazo de duración del mismo quedaba fijado en {PLAZO DEL CONTRATO} forzosos, comprendidos entre el {FECHA DE INICIO DEL CONTRATO} y el {FECHA DE TÉRMINO DEL CONTRATO}.

2.3. Dentro de los diversos derechos y obligaciones que {DIRECCIÓN DEL DEMANDADO} adquirió sin reserva ni limitación alguna, encontramos la de sometimiento a la Ley N° 30933 y el allanamiento a la restitución del inmueble por vencimiento del plazo del contrato, el cual se encuentra pactado en la Cláusula {CLAUSULA DE COMPETENCIA NOTARIAL} del contrato de arrendamiento:

2.4. Dicho ello, y como indicamos previamente, la Cláusula {CLAUSULA EN DONDE FIGURA LA FECHA DE TÉRMINO DEL CONTRATO} del contrato de arrendamiento dispuso que el mismo culminaba el {FECHA DE TÉRMINO DEL CONTRATO}; sin embargo, a la fecha {NOMBRE DEL DEMANDADO} se rehúsa a abandonar el inmueble, ocupándolo de manera precaria muy por encima del plazo pactado, razón por la cual acudimos a su Despacho para que pueda proceder con el desalojo notarial según fue pactado por las partes. 

III. REQUISITOS DE PROCEDENCIA DEL DESALOJO NOTARIAL: CUMPLIMOS CON TODOS LAS EXIGENCIAS DE LEY

3.1. A continuación, procedemos a acreditar el cumplimiento de todos los requisitos contemplados en los artículos 4, 5 y 6 de la Ley N° 30933, a fin de que se dé trámite a nuestra solicitud de desalojo notarial.

A. Requisitos del artículo 4 de la Ley N° 30933

3.2. Sobre el numeral 1 del artículo 4 de la Ley N° 30933, cumplimos con indicar que el inmueble materia de desalojo notarial se encontrarse individualizado de manera inequívoca en la Cláusula {CLÁUSULA EN DONDE FIGURA LA INDIVIDUALIZACIÓN DEL BIEN}, encontrándose el mismo ubicado en la {DIRECCIÓN DEL INMUEBLE} y consta de un área de {ÁREA DEL INMUEBLE EN NÚMEROS} m2. Asimismo, cuenta con un área construida de {ÁREA CONSTRUIDA DEL INMUEBLE EN NÚMEROS} m2; siendo que el área, linderos y medidas perimétricas corren inscritas en el {ASIENTO REGISTRAL EN DONDE OBRA EL DETALLE DE LAS MEDIDAS DEL INMUEBLE} de la Partida Registral N° {NÚMERO DE LA PARTIDA REGISTRAL DE SU INMUEBLE} del Registro de Propiedad Inmueble de Lima. 

3.3. Sobre los numerales 2 y 3 del artículo 4 de la Ley N° 30933, cumplimos con indicar que el contrato de arrendamiento se encuentra contenido en una Escritura Pública, tal como especificamos previamente.

B. Requisitos del artículo 5 de la Ley N° 30933

3.4. Sobre los numerales 1 y 2 del artículo 5 de la Ley N° 30933, cumplimos con indicar que el contrato de arrendamiento contiene una cláusula de allanamiento a futuro del arrendatario para la restitución del bien inmueble por vencimiento del plazo de contrato o la resolución del arrendamiento por falta de pago de la renta; así como una cláusula de sometimiento expreso e indubitable a lo establecido por la Ley N° 30933 para que el notario constate las causales de vencimiento del plazo del contrato o la resolución por falta de pago de la renta, y el Juzgado de Paz Letrado ordene y ejecute el desalojo. Esta se encuentra en la Cláusula {CLÁUSULA EN DONDE FIGURA EL SOMETIMIENTO A LA COMPETENCIA NOTARIAL} del contrato de arrendamiento.

3.5. Sobre el numeral 3 del artículo 5 de la Ley N° 30933, cumplimos con indicar que el contrato de arrendamiento ha consignado en la Cláusula {CLÁUSULA EN DONDE SE ESTABLECE LA MONEDA DEL PAGO} el número, tipo y moneda de la cuenta de abono abierta en una empresa del sistema financiero o en una cooperativa de ahorro y crédito supervisada por la Superintendencia de Banca, Seguros y Administradoras Privadas de Fondos de Pensiones (SBS) para que {NOMBRE DEL DEMANDADO} abone la renta convenida. Así, se aprecia que la renta fue pactada en {MONEDA} {MONTO DE LA RENTA EN NÚMEROS} ({MONTO DE LA RENTA EN LETRAS}), la cual debía ser depositada en la cuenta {NÚMERO DE LA CUENTA BANCARIA}, del {NOMBRE DEL BANCO}. 

C. Requisitos del artículo 6 de la Ley N° 30933

3.6. Respecto al numeral 1 del artículo 6 de la Ley N° 30933, cumplimos con presentar la presente solicitud de desalojo notarial por escrito, siendo que en el exordio se señalan que soy propietario del inmueble, mi domicilio y mi documento nacional de identidad; encontrándose al final del presente documento mi firma. A su turno, en el acápite I. he cumplido con identificar al arrendatario, así como su domicilio contractual y fiscal en donde deberá ser notificado.

3.7. Respecto al numeral 2 del artículo 6 de la Ley N° 30933, cumplo con adjuntar los siguientes documentos: i) copia legalizada del contrato de arrendamiento elevado a Escritura Pública; y, ii) el original de la carta notarial cursada a {NOMBRE DEL DEMANDADO} en el inmueble materia de desalojo y a su domicilio contractual mediante la cual se le requiere la restitución del bien por vencimiento del plazo contractual.

3.8. Por último, dejo expresa constancia de que el presente desalojo notarial se sustenta en la causal 7.1 de la Ley N° 30933; esto es, desalojo por vencimiento del plazo fijado en el contrato de arrendamiento.

POR TANTO:
Solicito a usted, Señor Notario, que proceda con el desalojo notarial conforme a ley.

OTROSÍ DIGO: Adjunto, en calidad de anexos, los siguientes documentos: 

ANEXO 1-A: Copia de mi documento nacional de identidad. 

ANEXO 1-B: Copia del documento que identifica a {NOMBRE DEL DEMANDADO}. 

ANEXO 1-C: Copia legalizada del contrato de arrendamiento.

ANEXO 1-D: Original de la carta notarial cursada a {NOMBRE DEL DEMANDADO} en el inmueble materia de desalojo y a su domicilio contractual mediante la cual se le requiere la restitución del bien por vencimiento del plazo contractual.

Lima, {FECHA DE PRESENTACIÓN DEL DOCUMENTO}

"""

    document_text = template.format(**{field: input_values[field].get() for field in fields})

    doc = Document()
    doc.add_paragraph(document_text)
    doc.save('Solicitud de desalojo notarial.docx')

for field in fields:
    frame = ttk.Frame(root)
    frame.pack(fill="x")

    label = ttk.Label(frame, text=field)
    label.pack(side="left", padx=(0, 10))

    entry = ttk.Entry(frame)
    entry.pack(side="left", fill="x", expand=True)

    input_values[field] = tk.StringVar()
    entry["textvariable"] = input_values[field]

button = ttk.Button(root, text="Generate Document", command=generate_document)
button.pack(side="left", padx=(10, 0))

root.mainloop()