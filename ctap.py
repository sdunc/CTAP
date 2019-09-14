#Stephen Duncanson
#cTAP

import os
import os.path
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic

FILE_PATH      = 'txts/'
GOOGLE_API_KEY = ''
YEARS_NUMBER   = ['1934','1952','1965','1985','1990','1995','2004','2006','2008','2010']
years 		   = []

print('Building database...')
l1934 = []
t1934 = open(FILE_PATH+"1934.txt",'r')
for line in t1934:
	l1934.append(((line.split(' ')[0], line.split(' ')[1].strip('\n'))))
t1934.close()
years.append(l1934)

l1952 = []
t1952 = open(FILE_PATH+"1952.txt",'r')
for line in t1952:
	l1952.append(((line.split(' ')[0], line.split(' ')[1].strip('\n'))))
t1952.close()
years.append(l1952)

l1965 = []
t1965 = open(FILE_PATH+"1965.txt",'r')
for line in t1965:
	l1965.append(((line.split(' ')[0], line.split(' ')[1].strip('\n'))))
t1965.close()
years.append(l1965)

l1985 = []
t1985 = open(FILE_PATH+"1985.txt",'r')
for line in t1985:
	l1985.append(((line.split(' ')[0], line.split(' ')[1].strip('\n'))))
t1985.close()
years.append(l1985)

l1990 = []
t1990 = open(FILE_PATH+"1990.txt",'r')
for line in t1990:
	l1990.append(((line.split(' ')[0], line.split(' ')[1].strip('\n'))))
t1990.close()
years.append(l1990)

l1995 = []
t1995 = open(FILE_PATH+"1995.txt",'r')
for line in t1995:
	l1995.append(((line.split(' ')[0], line.split(' ')[1].strip('\n'))))
t1995.close()
years.append(l1995)

l2004 = []
t2004 = open(FILE_PATH+"2004.txt",'r')
for line in t2004:
	l2004.append(((line.split(' ')[0], line.split(' ')[1].strip('\n'))))
t2004.close()
years.append(l2004)

l2006 = []
t2006 = open(FILE_PATH+"2006.txt",'r')
for line in t2006:
	l2006.append(((line.split(' ')[0], line.split(' ')[1].strip('\n'))))
t2006.close()
years.append(l2006)

l2008 = []
t2008 = open(FILE_PATH+"2008.txt",'r')
for line in t2008:
	l2008.append(((line.split(' ')[0], line.split(' ')[1].strip('\n'))))
t2008.close()
years.append(l2008)

l2010 = []
t2010 = open(FILE_PATH+"2010.txt",'r')
for line in t2010:
	l2010.append(((line.split(' ')[0], line.split(' ')[1].strip('\n'))))
t2010.close()
years.append(l2010)

geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
address_input = input("Enter an address: ")
address = geolocator.geocode(address_input)
address_lat_lon = (address.latitude,address.longitude)
distance = 999
for year in years:
	for e in year:
		lat, lon = e[0].split(',')[1],e[0].split(',')[0]
		test_lat_lon = (lat,lon)
		t_distance = geodesic(address_lat_lon,test_lat_lon).miles
		if t_distance < distance:
			distance = t_distance
			closest_index = year.index(e)
	print(YEARS_NUMBER[years.index(year)]+":\t"+year[closest_index][1])
	closest_index = 0
	distance = 999
