import json

def carregar_palavras_proibidas(caminho_arquivo='palavras_proibidas.json'):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar palavras proibidas: {e}")
        return []

