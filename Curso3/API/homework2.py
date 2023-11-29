import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
urlService = 'http://py4e-data.dr-chuck.net/json?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    
    params = {}
    params['address'] = address
    params['key'] = api_key
    url = urlService + urllib.parse.urlencode(params)
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'status' not in js or js['status'] != 'OK':
        print('*' * 10 ,'ERROR TO RETRIEVE', '*' * 10)
        print(data)
        continue
    
    place_id = js['results'][0]['place_id']
    print('Place id', place_id)
    
    # print(json.dumps(js, indent=4))   
    
    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('latitud', lat, 'longitud', lng)
    # location_type = js['results'][0]['geometry']['location_type']
    # print('Location type:', location_type)
    
    
    break
    