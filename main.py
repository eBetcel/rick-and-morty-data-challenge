import json
import requests
from google.cloud import storage
import datetime


def get_data(request):
    date_now = datetime.datetime.now()
    formatted_date = date_now.strftime('%Y%m%d')

    api_url = 'https://rickandmortyapi.com/api/episode'
    total_results = []
    response = requests.get(api_url)
    if response.status_code != 200:
        raise ValueError('Não foi possível acessar a API.')

    else:
        data = response.json()

        total_results += data.get('results')
        api_url = data.get('info').get('next')

        while api_url:
            response = requests.get(api_url)
            data = response.json()
            total_results += data.get('results')
            api_url = data.get('info').get('next')

        bucket_name = 'jerry_bucket_challenge'

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(f'episodes/episodes?extract-date={formatted_date}')
        json_bytes = json.dumps(total_results).encode('utf-8')
        blob.upload_from_string(json_bytes)