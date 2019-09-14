#Stephen Duncanson

import os
import os.path
import tkinter as tk
from tkinter import ttk
import webbrowser
GOOGLE_API_KEY = ''
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic

FOLDER_DIR = "X:/Stephen/Things I've worked on/Aerial Survey Program/"

def get_i_1974():
    coords = open(FOLDER_DIR+"/i_1974/i1974_coords.txt",'r')
    links = open(FOLDER_DIR+"/i_1974/i1974_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))

def get_i_1980():
    coords = open(FOLDER_DIR+"/i_1980/i1980_coords.txt",'r')
    links = open(FOLDER_DIR+"/i_1980/i1980_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))

def get_i_1981():
    coords = open(FOLDER_DIR+"/i_1981/i1981_coords.txt",'r')
    links = open(FOLDER_DIR+"/i_1981/i1981_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))
    
def get_i_1986():
    coords = open(FOLDER_DIR+"/i_1986/i1986_coords.txt",'r')
    links = open(FOLDER_DIR+"/i_1986/i1986_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))

def get_i_1990():
    coords = open(FOLDER_DIR+"/i_1990/i1990_coords.txt",'r')
    links = open(FOLDER_DIR+"/i_1990/i1990_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))



def get_i_1995():
    coords = open(FOLDER_DIR+"/i_1995/i1995_coords.txt",'r')
    links = open(FOLDER_DIR+"/i_1995/i1995_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))


def get_i_2000():
    coords = open(FOLDER_DIR+"/i_2000/i2000_coords.txt",'r')
    links = open(FOLDER_DIR+"/i_2000/i2000_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))


    
def get_1934():
    coords = open(FOLDER_DIR+"/1934/1934_coords.txt",'r')
    links = open(FOLDER_DIR+"/1934/1934_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))


def get_1952():
    coords = open(FOLDER_DIR+"/1952/1952_coords.txt",'r')
    links = open(FOLDER_DIR+"/1952/1952_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))  

def get_1965():
    coords = open(FOLDER_DIR+"/1965/1965_coords.txt",'r')
    links = open(FOLDER_DIR+"/1965/1965_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))


    
def get_1970():
    coords = open(FOLDER_DIR+"/1970/1970_coords.txt",'r')
    links = open(FOLDER_DIR+"/1970/1970_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))


def get_1985():
    coords = open(FOLDER_DIR+"/1985/1985_coords.txt",'r')
    links = open(FOLDER_DIR+"/1985/1985_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))  


def get_1990():
    coords = open(FOLDER_DIR+"/1990/1990_coords.txt",'r')
    links = open(FOLDER_DIR+"/1990/1990_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))  

def get_1995():
    coords = open(FOLDER_DIR+"/1995/1995_coords.txt",'r')
    links = open(FOLDER_DIR+"/1995/1995_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))  


def get_2004():
    coords = open(FOLDER_DIR+"/2004/2004_coords.txt",'r')
    links = open(FOLDER_DIR+"/2004/2004_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))  

def get_2006():
    coords = open(FOLDER_DIR+"/2006/2006_coords.txt",'r')
    links = open(FOLDER_DIR+"/2006/2006_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))  


def get_2008():
    coords = open(FOLDER_DIR+"/2008/2008_coords.txt",'r')
    links = open(FOLDER_DIR+"/2008/2008_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))  
    

def get_2010():
    coords = open(FOLDER_DIR+"/2010/2010_coords.txt",'r')
    links = open(FOLDER_DIR+"/2010/2010_links.txt",'r')
    l = []
    c = []

    for line in coords:
        c.append(line)
    for line in links:
        l.append(line)
     
    coords.close()
    links.close()

    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
    location = geolocator.geocode(loc_entry_var.get())
    e_coords = (location.latitude,location.longitude)

    closest_index = 0
    distance = 999999999999
    for ll in c:
        lat = ll.split(',')[1]
        lon = ll.split(',')[0]
        t_coords = (lat,lon)
        t_distance = geodesic(e_coords,t_coords).miles
        if t_distance < distance:
            distance = t_distance
            closest_index = c.index(ll)

    webbrowser.open_new((l[closest_index]))

    
root = tk.Tk()                                      #Create the window 
root.title("SAP")       #Set the titlebar

adr = ttk.Labelframe(root,text="Address")
adr.grid(column=1,row=0,columnspan=6)
loc_entry_var = tk.StringVar()
loc_entry = tk.Entry(adr,textvariable=loc_entry_var)
loc_entry.grid(column=1,row=0)
loc_entry.config(font=("Consolas",9))




ap = ttk.Labelframe(root,text="Aerial Photography")
ap.grid(column=1,row=1,columnspan=8)

button1934 = tk.Button(ap,text='1934',command=get_1934)
button1934.grid(row=2,column=1)

button1952 = tk.Button(ap,text='1952',command=get_1952)
button1952.grid(row=2,column=2)

button1965 = tk.Button(ap,text='1965',command=get_1965)
button1965.grid(row=2,column=3)

button1985 = tk.Button(ap,text='1985',command=get_1985)
button1985.grid(row=2,column=4)

button1990 = tk.Button(ap,text='1990',command=get_1990)
button1990.grid(row=3,column=1)

button1995 = tk.Button(ap,text='1995',command=get_1995)
button1995.grid(row=3,column=2)

button2004 = tk.Button(ap,text='2004',command=get_2004)
button2004.grid(row=3,column=3)

button2006 = tk.Button(ap,text='2006',command=get_2006)
button2006.grid(row=3,column=4)

button2008 = tk.Button(ap,text='2008',command=get_2008)
button2008.grid(row=4,column=1)

button2010 = tk.Button(ap,text='2010',command=get_2010)
button2010.grid(row=4,column=2)

###########################################################
ip = ttk.Labelframe(root,text="Coastal Infrared")
ip.grid(column=1,row=2,columnspan=8)
i_button1974 = tk.Button(ip,text='1974',command=get_i_1974)
i_button1974.grid(row=2,column=1)

i_button1980 = tk.Button(ip,text='1980',command=get_i_1980)
i_button1980.grid(row=2,column=2)

i_button1981 = tk.Button(ip,text='1981',command=get_i_1981)
i_button1981.grid(row=2,column=3)

i_button1986 = tk.Button(ip,text='1986',command=get_i_1986)
i_button1986.grid(row=2,column=4)

i_button1990 = tk.Button(ip,text='1990',command=get_i_1990)
i_button1990.grid(row=3,column=1)

i_button1995 = tk.Button(ip,text='1995',command=get_i_1995)
i_button1995.grid(row=3,column=2)

i_button2000 = tk.Button(ip,text='2000',command=get_i_2000)
i_button2000.grid(row=3,column=3)


root.mainloop()
