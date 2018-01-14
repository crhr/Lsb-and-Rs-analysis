# -*- coding:UTF-8 -*-
from PIL import Image

def mod(x,y):
    return x%y;

def toasc(strr):
    return int(strr, 2)

def func(le,str1,str2):#le is keylen  #str1 is image_path  #str2 is file_save_path
    a=""
    b=""
    im = Image.open(str1)
    lenth = le*8
    width = im.size[0]
    height = im.size[1]

#提取密钥并对比
    key = bin(lenth).replace('0b','')
    keylen = len(key)
    count = 0

    for h in range(height-1,0,-1):
        for w in range(width-1,0,-1):
            pixel = im.getpixel((w,h))
            if count == keylen:
                break
            if count%3==0:
                a=a+str((mod(int(pixel[0]),2)))
            elif count%3==1:
                a=a+str((mod(int(pixel[1]),2)))
            else:
                a=a+str((mod(int(pixel[2]),2)))
            count+=1
            if count == keylen:
                break
    if cmp(a, key)==0:
        count = 0
    else:
        count = 1

#提取文件
    for h in range(0, height):
        for w in range(0, width):
            pixel = im.getpixel((w, h))
            if count%3==0:
                count+=1
                b=b+str((mod(int(pixel[0]),2)))
                if count ==lenth:
                    break
            if count%3==1:
                count+=1
                b=b+str((mod(int(pixel[1]),2)))
                if count ==lenth:
                    break
            if count%3==2:
                count+=1
                b=b+str((mod(int(pixel[2]),2)))
                if count ==lenth:
                    break
        if count == lenth:
            break
    with open(str2,"wb") as f:
        for i in range(0,len(b),8):
            stra = toasc(b[i:i+8])
            f.write(chr(stra))
            stra =""
    f.closed
