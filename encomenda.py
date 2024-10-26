import fitz  # PyMuPDF
from datetime import datetime, timedelta

preco = {'Tecido': 7,
         'Algodao': 5.5,
         'Fio': 4.5,
         'Poliester': 10}

def preencher_pdf(input_pdf_path, output_pdf_path, dados):
    try:
        documento = fitz.open(input_pdf_path)
        pagina = documento[0]

        fonte = "helv"
        tamanho_fonte_titulo = 14
        tamanho_fonte_itens = 12

        x_order = 445
        y_order = 220
        text_order = f"{dados['order_number']}"

        rect_order = fitz.Rect(400, 210, 605, 230)
        pagina.draw_rect(rect_order, color=(1, 1, 1), fill=(1, 1, 1))
        pagina.insert_text(
            fitz.Point(x_order, y_order),
            text_order,
            fontsize=tamanho_fonte_titulo,
            fontname=fonte
        )

        x_date = 445
        y_date = 280
        text_date = f"{dados['date']}"

        rect_date = fitz.Rect(400, y_date - tamanho_fonte_titulo, 550, y_date + 5)
        pagina.draw_rect(rect_date, color=(1, 1, 1), fill=(1, 1, 1))
        pagina.insert_text(
            fitz.Point(x_date, y_date),
            text_date,
            fontsize=tamanho_fonte_titulo,
            fontname=fonte
        )

        posicoes_celulas = {
            'Artigo': 75.20,
            'Preço': 183.20,
            'Quantidade': 220.90,
            'Subtotal': 340.61
        }

        larguras_colunas = {
            'Artigo': posicoes_celulas['Preço'] - posicoes_celulas['Artigo'] - 5,
            'Preço': posicoes_celulas['Quantidade'] - posicoes_celulas['Preço'] - 5,
            'Quantidade': posicoes_celulas['Subtotal'] - posicoes_celulas['Quantidade'] - 5,
            'Subtotal': 150.0
        }

        y_header = 340.36
        incremento_y = 20.0
        pos_y_inicial = y_header + incremento_y
        pos_y = pos_y_inicial

        for item in dados['items']:
            text_item = item['item']
            rect_artigo = fitz.Rect(
                posicoes_celulas['Artigo'],
                pos_y - tamanho_fonte_itens,
                posicoes_celulas['Artigo'] + larguras_colunas['Artigo'],
                pos_y + incremento_y
            )
            pagina.insert_textbox(
                rect_artigo,
                text_item,
                fontsize=tamanho_fonte_itens,
                fontname=fonte,
                align=0
            )

            text_price = f"{item['unit_price']:.2f}"
            rect_preco = fitz.Rect(
                posicoes_celulas['Preço'],
                pos_y - tamanho_fonte_itens,
                posicoes_celulas['Preço'] + larguras_colunas['Preço'],
                pos_y + incremento_y
            )
            pagina.insert_textbox(
                rect_preco,
                text_price,
                fontsize=tamanho_fonte_itens,
                fontname=fonte,
                align=2
            )

            text_quantity = str(item['quantity'])
            rect_quantidade = fitz.Rect(
                posicoes_celulas['Quantidade'],
                pos_y - tamanho_fonte_itens,
                posicoes_celulas['Quantidade'] + larguras_colunas['Quantidade'],
                pos_y + incremento_y
            )
            pagina.insert_textbox(
                rect_quantidade,
                text_quantity,
                fontsize=tamanho_fonte_itens,
                fontname=fonte,
                align=2
            )

            text_subtotal = f"{item['subtotal']:.2f}"
            rect_subtotal = fitz.Rect(
                posicoes_celulas['Subtotal'],
                pos_y - tamanho_fonte_itens,
                posicoes_celulas['Subtotal'] + larguras_colunas['Subtotal'],
                pos_y + incremento_y
            )
            pagina.insert_textbox(
                rect_subtotal,
                text_subtotal,
                fontsize=tamanho_fonte_itens,
                fontname=fonte,
                align=2
            )

            pos_y += incremento_y

        x_total_label = 400
        y_total = 603.76
        largura_total_label = 100

        pagina.insert_text(
            fitz.Point(x_total_label, y_total),
            f"{dados['total']:.2f} EUR",
            fontsize=tamanho_fonte_titulo,
            fontname=fonte
        )

        documento.save(output_pdf_path)
        print(f"PDF preenchido guardado em: {output_pdf_path}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        documento.close()

order_no = 1



def create_order(products, date):

    global order_no

    items = []
    price = 0
    for p in products:
        placeholder = dict()
        placeholder['item'] = p['product']
        placeholder['quantity'] = p['qty']
        placeholder['unit_price'] = preco[p['product']]
        placeholder['subtotal'] = preco[p['product']] * p['qty']

        items.append(placeholder)
        price += preco[p['product']] * p['qty']


    dados = {
        'order_number': order_no,
        'date': date.strftime("%d/%m/%Y"),
        'items': items,
        'total': price
    }


    input_pdf_path = "nota.pdf"
    output_pdf_path = f"nota_modificada_{order_no}.pdf"

    preencher_pdf(input_pdf_path, output_pdf_path, dados)

    order_no+= 1


