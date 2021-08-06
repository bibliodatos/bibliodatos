import sqlite3
from math import cos, asin, sqrt, pi

# Populate the distance_to_avg field in or_county_seats table in Sqlite

def distance(lat1, lon1):
    # distance between to points in kilometers
    # https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula

    lat2 = 44.384378853315
    lon2 = -122.587318476599

    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a)) #

conn = sqlite3.connect('capstone.db')
cur = conn.cursor()
up_cur = conn.cursor()

cur.execute('''
SELECT county, lat, long 
FROM or_county_seats
''')

for or_row in cur:
    distance_km = distance(or_row[1], or_row[2])

    print(or_row[0], or_row[1], or_row[2], distance_km)

    up_cur.execute('UPDATE or_county_seats SET distance_to_avg = ? WHERE county = ?',
                       (distance_km, or_row[0])
                       )
    conn.commit()

cur.close()
up_cur.close()

