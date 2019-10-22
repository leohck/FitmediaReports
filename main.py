#  Copyright (c) 2019. Leonardo Black

import os
import json
from filemanager import FileManager
from datatoexcel import datatoexcel


fmanager = FileManager("arquivos/")


def filewithjson(behavior, file, *data):
    path = "originais/" if behavior == "r" else "filtrados/"
    _file = fmanager.verificar_arquivo(os.path.join(path, file))
    with open(_file, behavior) as __file:
        if behavior == "r":
            return json.load(__file)
        elif behavior == "w":
            json.dump(data[0], __file)


def filtrardados(data_dict, tipo, *args):
    novo_dict = {tipo: []}
    for x in data_dict[args[0]]:
        novo_dict[tipo].append({
            "nome": x["name"],
            tipo: x[args[1]],
            "bids": x['bids'],
            "imps": x['imps'],
            "clicks": x['clicks'],
            "ctr": x['ctr'],
        })
    return novo_dict


#                            CONSOLIDADO
# ----------------------------------------------------------------------------#
dados_consolidados = filewithjson('r', "campanhaconsolidado.json")

dados_consolidados_dict = {
    "campanha": dados_consolidados['name'],
    "bids": dados_consolidados['activity']['bids'],
    "imps": dados_consolidados['activity']['imps'],
    "clicks": dados_consolidados['activity']['clicks'],
    "ctr": dados_consolidados['activity']['ctr'],
}

filewithjson('w', 'dados_consolidado.json', dados_consolidados_dict)
# datatoexcel(1)
# ----------------------------------------------------------------------------#


#                                DIA
# --------------------------------------------------------------------------- #
dados_dia = filewithjson('r', 'campanhadia.json')

dados_dia_dict = filtrardados(dados_dia, "dia", "results", "breakout_value")

filewithjson('w', 'dados_dia.json', dados_dia_dict)

# datatoexcel(2)
# --------------------------------------------------------------------------- #

