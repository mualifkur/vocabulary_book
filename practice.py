import requests

api_key = '1ceb2c59-ac76-4a2e-8b9a-374cf5b25bc9'
word = 'voluminous'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)