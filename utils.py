from pathlib import Path
import json

def extract_route(requisicao):
    return requisicao.split()[1][1:]

def read_file(argumento):
    with open(argumento, "rb") as file:
        return file.read()

def load_data(arquivo):
    op = Path("data")/arquivo
    with open(op, "r") as file:
        return json.load(file)

def load_template(arquivo):
    op = Path("templates")/arquivo
    with open(op, "r") as file:
        return file.read()
