import urllib.request
import json
from datetime import datetime, timedelta
import time  # Import the time module for adding delays between retries

def download_json(url, max_retries=3, retry_delay=5):
    for attempt in range(1, max_retries + 1):
        try:
            with urllib.request.urlopen(url) as response:
                json_data = json.loads(response.read().decode('utf-8'))
            return json_data
        except Exception as e:
            print(f'Failed to download JSON (Attempt {attempt}/{max_retries}). Error: {e}')
            if attempt < max_retries:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
    
    raise Exception(f"Failed to download JSON after {max_retries} attempts.")

def backup(var):
    url = var

    try:
        # Use the download_json function with retries
        json_data = download_json(url)

        # Save the JSON content to a file
        with open(r'C:\Users\yoann.wiss\Desktop\python\Site_web\output.json', 'w', encoding='utf-8') as file:
            json.dump(json_data, file, indent=2)

    except Exception as e:
        print(f'Failed to download JSON. Error: {e}')

# r'C:\Users\yoann.wiss\Desktop\python\Site_web\output.json'

    with open(r'C:\Users\yoann.wiss\Desktop\python\Site_web\output.json') as mon_fichier:
        data = json.load(mon_fichier)


    n = 0
    x = 0
    time_now = datetime.now()
    today = time_now.replace(hour=0, minute=0, second=0, microsecond=0)
    veille = time_now - timedelta(days=1)
    yesterday = veille.replace(hour=0, minute=0, second=0, microsecond=0)

    while datetime.fromisoformat(data[x]['backup_start']) > datetime.fromisoformat(str(today)) :
        x += 1

    while datetime.fromisoformat(data[n]['backup_start']) > datetime.fromisoformat(str(yesterday)):
        n += 1



    variables = {}

    # Populate the dictionary with dynamic variable names
    for n in range(0, n):
        variable_name = f'status{n}'
        variables[variable_name] = data[n + x]['status']
    # print(variables['status1'])

    x = 0
    for key, value in variables.items():
        if value == "OK":
            x += 1
        elif value == 'ERROR':
            print(f"The backup named {data[int(key[6:])]['backup_name']} in {var} has an Error")
        else:
            print(f"The backup named {data[int(key[6:])]['backup_name']} in {var} is still Running")
    if x == n+1:
        print(f"everything is OK for {var}")



backup('http://srvbackup-d67.mcc.ad.culture.fr:8080/backups.json')

backup('http://srvbackup2-d67.mcc.ad.culture.fr:8080/backups.json')

backup('http://srvbackup-u68.mcc.ad.culture.fr:8080/backups.json')

backup('http://srvbackup-d57.mcc.ad.culture.fr:8080/backups.json')

backup('http://srvbackup2-d57.mcc.ad.culture.fr:8080/backups.json')

backup('http://srvbackup-u54.mcc.ad.culture.fr:8080/backups.json')

backup('http://srvbackup-u55.mcc.ad.culture.fr:8080/backups.json')

backup('http://srvbackup-u88.mcc.ad.culture.fr:8080/backups.json')

backup('http://143.126.155.247:8080/backups.json')

backup('http://srvbackup-d51.mcc.ad.culture.fr:8080/backups.json')

backup('http://143.126.151.206:8080/backups.json')

backup('http://srvbackup-u08.mcc.ad.culture.fr:8080/backups.json')

backup('http://srvbackup-u10.mcc.ad.culture.fr:8080/backups.json')

backup('http://srvbackup-u51.mcc.ad.culture.fr:8080/backups.json')

backup('http://srvbackup-u52.mcc.ad.culture.fr:8080/backups.json')