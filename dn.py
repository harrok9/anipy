import requests

url = 'https://odd-bar-1e6f.zadafrouyatoi-74366729.workers.dev/?file=MTwGNyAoOCAxPDMjATkDRjMzJVgKMyQWOTEzAAsFLhc7IRkWJj8CETsFLAUEPDwUPQchPQoJGDA9Ch0iFD8vGzMpD1kLRlAVJz0gDDoqQxo2BDskAF1eIz09MicPCCtcIi0jOwsoFDUhPj8yOlsZEzo5FVgAAxEdMQMDHyRUMhk3Dwk5Ej4jMCcmMjo9DAUcMj8NUAk6Rxg0MA0hBTk9Qj0wOgcKViMrODwJAD8UMh82ICRUOgQkEDcnOAEyLVwYMCpfDgoIOgc%2BMF1S&rayid=1713038379'

response = requests.get(url)
if response.status_code == 200:
    with open('movie.mkv', 'wb') as f:
        f.write(response.content)
    print('File downloaded successfully as movie.mkv')
else:
    print(f'Failed to download file. Status code: {response.status_code}')
