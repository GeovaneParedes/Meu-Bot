import json
import os

CURSOS_FILE = 'cursos_devprogramador.json'

def carregar_cursos():
    if not os.path.exists(CURSOS_FILE):
        return []
    with open(CURSOS_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_cursos(cursos):
    with open(CURSOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(cursos, f, ensure_ascii=False, indent=4)

def adicionar_curso(linguagem, nome_curso, link):
    cursos = carregar_cursos()
    novo_curso = {
        linguagem: nome_curso,
        "link": link
    }
    cursos.append(novo_curso)
    salvar_cursos(cursos)

def buscar_cursos(termo_busca):
    termo = termo_busca.lower()
    cursos = carregar_cursos()
    resultados = []

    for curso in cursos:
        for chave, valor in curso.items():
            if chave == 'link':
                continue
            if termo in chave.lower() or termo in valor.lower():
                resultados.append({
                    'linguagem': chave,
                    'nome': valor,
                    'link': curso.get('link')
                })
                break

    return resultados

