import requests
from google.cloud import storage

def store_data(request):
    # URL da API que você deseja consumir
    api_url = 'https://api.example.com/data'
    
    # Faça uma solicitação HTTP GET para a API
    response = requests.get(api_url)
    
    # Verifique se a resposta foi bem-sucedida
    if response.status_code != 200:
        raise ValueError('Não foi possível acessar a API.')
    
    # Crie um objeto Blob no Google Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket('seu-bucket')
    blob = bucket.blob('caminho/para/pasta/nome-do-arquivo.json')
    
    # Escreva o conteúdo da resposta no objeto Blob
    blob.upload_from_string(response.content)
    
    return 'Dados armazenados com sucesso!'
