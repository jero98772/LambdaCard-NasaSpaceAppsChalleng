#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#Sky-eye - by lambdaCard
from PIL import Image,ImageOps
import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpi
import datetime
def noaaResample(name:str,pathwav="",directoryimg=""):
    """
    noaaResample(name:str)->imagefilename 
    with a wav file obteined of noaas satelite generate a png file using hilbert transform,resampled is better cuality, sometimes audio not was resample
    """
    fs, data = wav.read(pathwav+name)  
    data_crop = data[20*fs:21*fs]
    analytical_signal = signal.hilbert(data)
    data_am = np.abs(analytical_signal)
    frame_width = int(0.5*fs)
    w, h = frame_width, data_am.shape[0]//frame_width
    image = Image.new('RGB', (w, h))
    px, py = 0, 0
    for p in range(data_am.shape[0]):
        lum = int(data_am[p]//32 - 32)
        if lum < 0: lum = 0
        if lum > 255: lum = 255
        image.putpixel((px, py), (0, lum, 0))
        px += 1
        if px >= w:
            px = 0
            py += 1
            if py >= h:
                break
    image = image.resize((w, 4*h))
    plt.imshow(image)
    filename=name.replace(".wav",".png")
    plt.imsave(directoryimg+filename,image)
    return filename,image
def noaa(name:str,pathwav="",directoryimg=""):
    """
    noaaResample(name:str)->imagefilename 
    with a wav file obteined of noaas satelite generate a png file using hilbert transform
    """
    imgpix=[]
    fs, data = wav.read(pathwav+name)  
    data_crop = data[20*fs:21*fs]
    resample = 4
    data = data[::resample]
    fs = fs//resample
    analytical_signal = signal.hilbert(data)
    data_am = np.abs(analytical_signal)
    frame_width = int(0.5*fs)
    w, h = frame_width, data_am.shape[0]//frame_width
    image = Image.new('RGB', (w, h))
    px, py = 0, 0
    for p in range(data_am.shape[0]):
        lum = int(data_am[p]//32 - 32)
        if lum < 0: lum = 0
        if lum > 255: lum = 255
        image.putpixel((px, py), (0, lum, 0))
        px += 1
        if px >= w:
            px = 0
            py += 1
            if py >= h:
                break
    image = image.resize((w, h))
    #print(imgpix)
    image=ImageOps.grayscale(image)
    plt.imshow(image)
    filename=name.replace(".wav",".png")
    plt.imsave(directoryimg+filename,image)
    return filename,image
def imgload(file):
    datos = mpi.imread(file)
    return datos
def grayScale(imagen):
    height = imagen.shape[0]
    width = imagen.shape[1]
    img = np.zeros((height,width,3),dtype=int)
    for i in range(height):
        for j in range(width):
            elemento1 = imagen[i][j][0]
            elemento2 = imagen[i][j][1]
            elemento3 = imagen[i][j][2]
            prom = elemento1+elemento2+elemento3/imagen.shape[2]
            for k in range(3):
                img[i][j][k] = prom*100
    return img
def save(path,image):
    #print(type(path),type(image),path,image)
    img=Image.fromarray(image)
    img.save(path)
    #plt.savefig(path,image)
def genMap():
    import folium
    m = folium.Map(location=[6.256405968932449, -75.59835591123756])
    folium.Marker([6.176375,-75.5600386], popup="<i>kit 0</i>", tooltip="kit 0").add_to(m)
    folium.Marker([38.8978272,-77.9703665], popup="<i>next kit</i>", tooltip="next kit").add_to(m)
    m.save("index.html")
def writetxt(name,content):
    """
    writetxt(name,content) , write in txt file something  
    """
    content =str(content)
    with open(name, 'w') as file:
        file.write(content)
        file.close()
def getData():
    from data.data import data
    return data 
def sdrIsConected():
    try:
        from rtlsdr import RtlSdr
        sdr = RtlSdr()
        val=True
    except:
        val=False
    return val
def id2frec(id):
    if (id == "15"):
        return 137.620,"NOAA-15"
    elif (id == "18"):
        return 137.9125,"NOAA-18"
    elif (id == "19"):
        return 137.1,"NOAA-19"
def pred(url="https://noaasis.noaa.gov/cemscs/polrschd.txt"):
    from pyorbital.orbital import Orbital
    import urllib
    orbitalNOAA15 = Orbital("NOAA-15")
    orbitalNOAA18 = Orbital("NOAA-18")
    orbitalNOAA19 = Orbital("NOAA-19")
    satinfo=[]#start,end,frecuency
    i=-1
    for line in urllib.request.urlopen(url): # download txt, read each line
        text = line.decode('utf-8')
        text = text[:-1] 
        date = text[0:17] 
        dateParsed = datetime.datetime.strptime(date, '%Y/%j/%H:%M:%S') # parse date from weird format YYYY/DDD/HH:MM:SS
        satID = text[23:25]
        if "PBK,START,GAC" in text:#start pass in...
            satinfo.append(["","","",""])
            i+=1
            satinfo[i][0]=str(dateParsed)
        elif "PBK,END,GAC" in text:#end pass in..
            satinfo[i][1]=str(dateParsed)
            frec,sat=id2frec(satID)
            satinfo[i][2]=frec
            satinfo[i][3]=sat
        else:
            eventType = "other"
        #if satinfo[i][0]!=0 and satinfo[i][1]!=0 and satinfo[i][2]!=0:
    return satinfo
        #yield eventType
def formatSatData(data):
    txt=""
    #data=pred()
    for i in data:
        txt=txt+"Satelite: "+i[3]+" pass at "+i[0]+" to "+i[1]+" on "+str(i[2])+"Mhz \n"
    return txt