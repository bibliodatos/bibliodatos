import sqlite3
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import time


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_county(fl_lat, fl_long):
    time.sleep(1)

    # https://geo.fcc.gov/api/census/block/find?latitude=43.390723&longitude=-124.263982&format=json
    serviceurl = 'https://geo.fcc.gov/api/census/block/find?'

    parms = dict()
    parms['format'] = 'json'
    parms['latitude'] = fl_lat
    parms['longitude'] = fl_long

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    # print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        return ''

    # print(json.dumps(js, indent=4))
    # print(json.dumps(js['County']['name'], indent=4))
    return js['County']['name'].upper()



conn = sqlite3.connect('capstone.db')
cur = conn.cursor()
up_cur = conn.cursor()

cur.execute('''
SELECT id, lat, long 
FROM or_vehicles
WHERE county IS NULL
ORDER BY id ASC
LIMIT 100000
''')

for or_row in cur:
    print(or_row[0], or_row[1], or_row[2])
    upper_county = get_county(or_row[1], or_row[2])

    if upper_county != '':
        print(upper_county)
        #cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
        #            (org,))
        up_cur.execute('UPDATE or_vehicles SET county = ? WHERE id = ?',
                       (upper_county, or_row[0])
                       )
        conn.commit()

cur.close()
up_cur.close()

