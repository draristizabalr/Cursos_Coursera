import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    cuenta = input('Ingresa una cuenta de Twitter: ')
    if (len(cuenta) < 1): break
    url = twurl.aumentar(TWITTER_URL,
                         {'screen_name': cuenta, 'count': '5'})
    print('Recuperando', url)
    conexion = urllib.request.urlopen(url)
    data = conexion.read().decode()
    print('Recuperados', len(data), 'caracteres')

    js = json.loads(data)
    print(json.dumps(js, indent=4))

    cabeceras = dict(conexion.getheaders())
    print('Restantes', cabeceras['x-rate-limit-remaining'])