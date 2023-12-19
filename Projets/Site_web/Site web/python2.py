import urllib.request
import json
from datetime import datetime, timedelta


url = 'http://srvbackup-d67.mcc.ad.culture.fr:8080/backups.json'

try:
    # Open the URL and read its content
    with urllib.request.urlopen(url) as response:
        # Parse the JSON content
        json_data = json.loads(response.read().decode('utf-8'))

    # Save the JSON content to a file
    with open(r'C:\Users\yoann.wiss\Desktop\python\Site web\output.json', 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=2)
except Exception as e:
    print(f'Failed to download JSON. Error: {e}')


with open(r'C:\Users\yoann.wiss\Desktop\python\Site web\output.json') as mon_fichier:
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
        print(f"The backup named {data[int(key[6:])]['backup_name']} has an Error")
    else:
        print(f"The backup named {data[int(key[6:])]['backup_name']} is still Running")
if x == n+1:
    print("everything is OK")

