#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#labdaOrbit - by lambdaCard
import matplotlib.image as mpi
import numpy as np
import matplotlib.pyplot as plt
import cv2
def noaaResample(name:str):
    """
    noaaResample(name:str)->imagefilename 
    with a wav file obteined of noaas satelite generate a png file using hilbert transform,resampled is better cuality, sometimes audio not was resample
    """
    import scipy.io.wavfile as wav
    import scipy.signal as signal
    import numpy as np
    from PIL import Image,ImageOps
    import matplotlib.pyplot as plt
    import datetime
    fs, data = wav.read(name)  
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
    plt.savefig(filename)
    return filename
def noaa(name:str):
    """
    noaaResample(name:str)->imagefilename 
    with a wav file obteined of noaas satelite generate a png file using hilbert transform
    """
    import scipy.io.wavfile as wav
    import scipy.signal as signal
    import numpy as np
    from PIL import Image,ImageOps
    import matplotlib.pyplot as plt
    import datetime
    imgpix=[]
    fs, data = wav.read(name)  
    data_crop = data[20*fs:21*fs]
    resample = 4
    data = data[::resample]
    fs = fs//resample
    analytical_signal = signal.hilbert(data)
    data_am = np.abs(analytical_signal)
    frame_width = int(0.5*fs)
    w, h = frame_width, data_am.shape[0]//frame_width
    image = Image.new('L', (w, h))
    px, py = 0, 0
    for p in range(data_am.shape[0]):
        lum = int(data_am[p]//32 - 32)
        if lum < 0: lum = 0
        if lum > 255: lum = 255
        image.putpixel((px, py),  lum)
        px += 1
        if px >= w:
            px = 0
            py += 1
            if py >= h:
                break
    image = image.resize((w, h))

    #print(imgpix)
    image=ImageOps.grayscale(image)
    filename=name.replace(".wav",".png")
    plt.imsave(filename,image)
    #plt.imshow(image)
    return filename
    #return image
def img2asciiart(img,size = 15,intensity = 255,replaceItem = 0,items = ["@"," "]):
    """
    img2asciiart(img,size = 15,intensity = 255,replaceItem = 0,items = ["@"," "]) ,return a  matrix img as str
    """
    import cv2
    from numpy import asarray 
    dataFile = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    imgresized  = dataFile #cv2.resize(dataFile , (size, size))
    imgstr = ""
    #imgstr = asarray(imgresized , dtype= str)
    for count in range(len(imgresized)):
        for cont in range(len(imgresized[count]))  :
                if imgresized[count,cont]//intensity == replaceItem:
                    #imgstr[count,cont]= items[0]
                    imgstr += items[0]
                else:
                    #imgstr[count,cont] = items[1]
                    imgstr += items[1]
        imgstr += "\n"
    outfig = [imgresized,imgstr]
    print(imgresized)
    return outfig 
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
			print(prom)
			for k in range(3):
				img[i][j][k] = prom*100
	return img
def show(datos):

    #plt.imsave("1.png",datos)
    f = plt.figure()
    #print("show")
    #f.add_subplot(1,2,1)
    plt.imshow(datos)
    plt.show()

def save(filename,image):
    plt.imsave(filename,image)

def main():
    #img2asciiart("1.png",size = 500,intensity = 255,replaceItem = 0,items = ["@"," "])
    i=noaa("1.wav")
    im=img(i)
    im2=grayScale(im)
    #plt.imsave("3.png",im2)
    #show(im2)
    save(im2)
    #save(im2)


    #noaaResample("1.wav")

    #im2=grayScale(i)
    #show(im2)
main()