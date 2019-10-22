#  Copyright (c) 2019. Leonardo Black

import json
from filemanager import FileManager
from datatoexcel import datatoexcel


fmanager = FileManager("arquivos/")

#                            CONSOLIDADO
# ----------------------------------------------------------------------------#
arquivo_consolidado = fmanager.verificar_arquivo("campanhaconsolidado.json")
with open(arquivo_consolidado, 'r') as arq:
    dados_consolidados = json.load(arq)

# id_c = dados_consolidados['id']
# name_c = dados_consolidados['name']
# imps_c = dados_consolidados['activity']['imps']
# bids_c = dados_consolidados['activity']['bids']
# clicks_c = dados_consolidados['activity']['clicks']
# conv_c = dados_consolidados['activity']['conversions']
# ctr_c = dados_consolidados['activity']['ctr']
dados_consolidados_dict = {
    "Campanha": dados_consolidados['name'],
    "Bids": dados_consolidados['activity']['bids'],
    "Imps": dados_consolidados['activity']['imps'],
    "Clicks": dados_consolidados['activity']['clicks'],
    "Ctr": dados_consolidados['activity']['ctr'],
}

arquivo_dadosconsolidado = fmanager.verificar_arquivo("dados_consolidado.json")
with open(arquivo_dadosconsolidado, 'w') as arq:
    json.dump(dados_consolidados_dict, arq)

# datatoexcel(1)
# ----------------------------------------------------------------------------#


#                                DIA
# ----------------------------------------------------------------------------#
arquivo_dia = fmanager.verificar_arquivo("campanhadia.json")
with open(arquivo_dia, 'r') as arq:
    dados_dia = json.load(arq)

dados_dia_dict = {
    "dia": []
}

for e, day in enumerate(dados_dia["results"]):
    dados_dia_dict["dia"].append({
        "nome": day["name"],
        "dia": day['breakout_value'],
        "bids": day['bids'],
        "imps": day['imps'],
        "clicks": day['clicks'],
        "ctr": day['ctr'],
    })

arquivo_dadosdia = fmanager.verificar_arquivo("dados_dia.json")
with open(arquivo_dadosdia, 'w') as arq:
    json.dump(dados_dia_dict, arq)

# datatoexcel(2)
# ----------------------------------------------------------------------------#


#                               HORA DIA
# ----------------------------------------------------------------------------#
arquivo_horadia = fmanager.verificar_arquivo("campanhahoradia.json")
with open(arquivo_horadia, 'r') as arq:
    dados_horadia = json.load(arq)

dados_horadia_dict = {
    "horasdia": []
}

for e, horadia in enumerate(dados_horadia["results"]):
    dados_horadia_dict["horasdia"].append({
        "nome": horadia["name"],
        "hora": horadia['breakout_value'],
        "bids": horadia['bids'],
        "imps": horadia['imps'],
        "clicks": horadia['clicks'],
        "ctr": horadia['ctr'],
    })

arquivo_dadoshoradia = fmanager.verificar_arquivo("dados_horadia.json")
with open(arquivo_dadoshoradia, 'w') as arq:
    json.dump(dados_horadia_dict, arq)


def filewithjson(behavior, arquivo):
    _file = fmanager.verificar_arquivo(arquivo)
    with open(_file, behavior) as __file:
        if behavior == "r":
            response = json.load(_file)
        elif behavior == "w":
            json.dump(arquivo, __file)
    return response if response else None
