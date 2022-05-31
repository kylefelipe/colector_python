from unicodedata import name
import requests
from dotenv import load_dotenv
from os import environ as ENV

load_dotenv()

URL = f'{ENV["BASE_URL"]}/people'


def getData(url=URL):
    """
    Pega pega os dados da url padrão ou de uma url passada como parametro
    PARAMS:
    - url: string, URL da API a ser buscada
    """
    response = requests.get(url=url).json()
    return response
