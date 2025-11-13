import json

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo {nome_arquivo}.")
        return None

def escrever_json(nome_arquivo, pessoa):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    # Exemplo de dados de uma pessoa
    pessoa = {
        "nome": "Ana",
        "idade": 28,
        "cidade": "São Paulo"
    }

    nome_arquivo = 'pessoa.json'

    # Escreve os dados no JSON
    escrever_json(nome_arquivo, pessoa)
    print("Dados gravados com sucesso.")

    # Lê os dados do JSON
    dados_lidos = ler_json(nome_arquivo)
    if dados_lidos:
        print("Dados lidos do arquivo:")
        print(dados_lidos)