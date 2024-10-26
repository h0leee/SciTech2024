import re

tipos_dict = {
    "Tshirt": 0,
    "Calcoes": 1,
    "Camisola": 2,
    "Calcas": 3
}

tamanhos_dict = {
    "XS": 0,
    "S": 1,
    "M": 2,
    "L": 3,
    "XL": 4
}

def parse_txt(filename):
    file = open(filename, mode = 'r', encoding = 'utf-8-sig')
    file_content = file.read()

    return parse_content(file_content)


def parse_content(file_content):
    items = []
    if re.match(r"^\d+\w+\s\w+", file_content.splitlines()[0]):
        for line in file_content.splitlines():
            partes = line.split()
            quantidade, tipo, tamanho = partes[0], partes[1], partes[2]
            items.append({"type": tipos_dict[tipo], "qty": int(quantidade), "size": tamanhos_dict[tamanho]})

    elif re.match(r"^\d+\w+[XSML]+", file_content.splitlines()[0]):
        pattern = "(\d+)(\w+?)([XSML]+)"
        matches = re.findall(pattern, file_content)

        for quantidade, tipo, tamanho in matches:
            items.append({"type": tipos_dict[tipo], "qty": int(quantidade), "size": tamanhos_dict[tamanho]})

    else:
        pattern = "(.*?)(\d+)(\s)(\w+)(.*?)([XSML]+)"
        matches = re.findall(pattern, file_content)

        for lixo1, quantidade, lixo2, tipo, lixo3, tamanho in matches:
            items.append({"type": tipos_dict[tipo], "qty": int(quantidade), "size": tamanhos_dict[tamanho]})

    return items
