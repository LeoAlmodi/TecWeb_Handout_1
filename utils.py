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

def add(anotacao):
    op = Path("data")/"notes,json"
    if op.exists():
        with open(op, "r") as file:
            data = json.load(file)
    else:
        data = []
    data.append(anotacao)
    with open(op, 'w') as file:
        json.dump(data, file)

def build_response(body="", code=200, reason="OK", headers=""):
    if headers == "":
        string = f"HTTP/1.1 {code} {reason}\n\n{body}"
    else:
        string = f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}"
    return string.encode()