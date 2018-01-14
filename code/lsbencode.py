# -*- coding: UTF-8 -*-
from PIL import Image

def plus(str):
    return str.zfill(8)

def get_key(strr):
    tmp = strr
    f = file(tmp,"rb")
    str = ""
    s = f.read()
    for i in range(len(s)):
        str = str+plus(bin(ord(s[i])).replace('0b',''))
    f.closed
    return str

def mod(x,y):
    return x%y;

def func(str1,str2,str3):#str1 is bmp path  #str2 is file path  #str3 is filesave
    im = Image.open(str1)
    width = im.size[0]
    height = im.size[1]
    count = 0
    key = get_key(str2) #key is the message
    keylen = len(key)
    strkey = bin(keylen).replace('0b','')#隐藏的是strkey
    keystrlen = len(strkey)

    if width*height*3-10 < keylen:
        return 0
    else:
        for h in range(0,height):
            for w in range(0,width):
                pixel = im.getpixel((w,h))
                a=pixel[0]
                b=pixel[1]
                c=pixel[2]
                if count == keylen:
                    break
                a= a-mod(a,2)+int(key[count])
                count+=1
                if count == keylen:
                    im.putpixel((w,h),(a,b,c))
                    break
                b =b-mod(b,2)+int(key[count])
                count+=1
                if count == keylen:
                    im.putpixel((w,h),(a,b,c))
                    break
                c= c-mod(c,2)+int(key[count])
                count+=1
                if count == keylen:
                    im.putpixel((w,h),(a,b,c))
                    break
                if count % 3 == 0:
                    im.putpixel((w,h),(a,b,c))
    #隐藏密钥
        count = 0
        for h in range(height-1,0,-1):
            for w in range(width-1,0,-1):
                pixel = im.getpixel((w,h))
                a=pixel[0]
                b=pixel[1]
                c=pixel[2]
                if count == keystrlen:
                    break
                if count%3==0:
                    a= a-mod(a,2)+int(strkey[count])
                elif count%3==1:
                    b =b-mod(b,2)+int(strkey[count])
                else:
                    c= c-mod(c,2)+int(strkey[count])
                im.putpixel((w,h),(a,b,c))
                count += 1
                if count == keystrlen:
                    break
        im.save(str3)
        return keylen