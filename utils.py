import json

def save_sales(file_name, list_sales):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            sales = list_sales
            json.dump(sales, file_name, ensure_ascci=False, indent=4)
        return f'Dados salvo com sucesso em {file_name}'
    except Exception as e:
        return f'Erro ao salvar o arquivo\n \
                Error name: {e}'
    
def load_sales(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            list_sales = json.load(file)
        return list_sales
    except FileNotFoundError:
        return 'Arquivo não encontrado!'