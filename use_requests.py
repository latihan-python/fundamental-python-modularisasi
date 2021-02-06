import requests

url = 'https://google.com'

try:
    response = requests.get(url)
    print(f'SUKSES : {response.status_code}')

except Exception as e:
    print(f'there is an error : {e}')
