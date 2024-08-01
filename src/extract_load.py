
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os



#import de variaveis de ambiente
commodities = ['CL=F', 'GC=F', 'SI=F'] #ativos da bolsa de valores (dados de cotacao)

def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)


if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities(commodities)
    #salvar_no_postgres(dados_concatenados, schema='public')
    print(dados_concatenados)


#salvar no banco de dados