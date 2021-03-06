# -*- coding: UTF-8 -*-
from PIL import Image
import rsu
import numpy

def rsmain(str):
    
    fig = Image.open(str)
    fig = fig.resize((256, 256),Image.ANTIALIAS)
    figimage = Image.open(str).convert('L')
    
    if fig.mode == "RGB":
        pix = fig.load()
        w = fig.size[0]
        h = fig.size[1]
        imagesize = w*h
        r= [0 for x in range(0,imagesize)]
        g= [0 for x in range(0,imagesize)]
        b= [0 for x in range(0,imagesize)]
        i = 0
        for x in range(w):
            for y in range(h):
                r[i],g[i],b[i] = pix[x,y]
                i = i+1
        i = 0
        for x in range(w):
            for y in range(h):
                figimage.putpixel((x,y),r[i])
                i = i + 1
                  
    
    x = fig.size[0]
    y = fig.size[1]
    bufsize = x*y
    
    res1 = rsu.RSU(figimage)

    for i in range(0,x):
        for j in range(0,y):
            figimage.putpixel((i,j),figimage.getpixel((i,j))^1)
    res2 = rsu.RSU(figimage)

#................................
    d0 = res1[0] - res1[1] #Rm(p/2) - Sm(p/2)
    d1 = res2[0] - res2[1] #Rm(1-p/2) - Sm(1-p/2)
    d10 = res1[3] - res1[4] #R-m(p/2) - S-m(p/2)
    d11 = res2[3] - res2[4] #R-m(1-p/2) - S-m(1-p/2)
    
    a = 2*( d0 + d1 )
    b = d10 - d11 -d1 -3*d0
    c = d0 - d10

    root = [a,b,c]
    res =numpy.roots(root)
    
    if abs(res[0]) >= abs(res[1]):
        final = res[1]/(res[1] - 0.5)
    else:
        final = res[0]/(res[0] - 0.5)
    return round(final,3)