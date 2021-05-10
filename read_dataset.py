def read_dataset(filename: str = "", sep: str = "", header: list = []) -> dict:

    # Carregar arquivo do dataset

    f = open(filename, "r", encoding='latin-1')
    dataset = f.read().split("\n")

    # Remover ultima linha (linha vazia)

    while dataset[-1] == "":
        dataset.pop()

    # Construir dicionário com nomes das colunas

    dict_dataset = {}

    for name in header:
        dict_dataset[name] = []

    # Popular dicionario

    for instancia in dataset:
        for idx, col in enumerate(instancia.split(sep)):
            dict_dataset[header[idx]].append(col)

    return dict_dataset
