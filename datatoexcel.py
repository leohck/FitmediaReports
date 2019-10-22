#  Copyright (c) 2019. Leonardo Black

from oauth2client.service_account import ServiceAccountCredentials
from filemanager import FileManager
import gspread
import json
# import time


def datatoexcel(tipo="padrao"):
    fm = FileManager("arquivos/")

    # use creds to create a client to interact with the google drive api
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("arquivos/credentials.json", scope)
    client = gspread.authorize(creds)

    # enviar dados consolidado
    if tipo == 1:
        sheet_dados_consolidado = client.open("Teste Data Studio Black").worksheet("Prog Display - Consolidado")
        arquivo_consolidado = fm.verificar_arquivo("dados_consolidado.json")
        with open(arquivo_consolidado, 'r') as arq:
            dados_consolidado = dict(json.load(arq))
            for e, value in enumerate(dados_consolidado.values()):
                sheet_dados_consolidado.update_cell(2, e+1, value)

    # -------------------------------------------------------

    # enviar dados dia
    if tipo == 2:
        sheet_dados_dia = client.open("Teste Data Studio Black").worksheet("Prog Display - Dia")
        arquivo_dia = fm.verificar_arquivo("dados_dia.json")
        with open(arquivo_dia, 'r') as arq:
            dados_dia = dict(json.load(arq))
            days = dados_dia["dia"]
            for d, day in enumerate(days, 2):
                for v, value in enumerate(day.values(), 1):
                    sheet_dados_dia.update_cell(d, v, value)
    # -------------------------------------------------------
