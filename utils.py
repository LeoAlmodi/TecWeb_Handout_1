def extract_route(requisicao):
    return requisicao.split()[1][1:]

def read_file(argumento):
    with open(argumento, "rb") as file:
        return file.read()
