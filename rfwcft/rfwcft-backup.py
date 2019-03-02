import PIL
import glob
import os
from PIL import Image
import os.path, sys

path = "C:\\Users\\CXXX\\Pictures\\102"
dirs = os.listdir(path)#corrected
'''
donepath = "C:\\Users\\CXXX\\Pictures\\102\\169"
if not os.path.exists(donepath):
    os.makedirs(donepath, "donepath")
'''
def crop():
    for item in dirs:
        fullpath = os.path.join(path,item)#corrected#corrected    
        if os.path.isfile(fullpath):#corrected#corrected
            im = Image.open(fullpath)#corrected#corrected
            f, e = os.path.splitext(fullpath)#corrected
            imCrop = im.crop((0, 0, 1600, 900)) #corrected#corrected
            imCrop.save(f + '_done.jpeg', "JPEG") #HUEVO#corrected
            print(item + ' cropped')
            os.syslem('cls')            
def res():
    for item in dirs:
        fullpath = os.path.join(path,item)
        if os.path.isfile(fullpath):    
            basewidth = 1600
            img = Image.open(fullpath)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
            img.save(fullpath) 

#res()
#crop()
ans=True
while ans:
    os.system('cls')
    print ("""
    1. Crop photos to 1600 x 900 in folder 102 
    2. Delete photos without prefix _doen folder 102
    3.
    4. Exit/Quit
    """)
    an = input("What would you like to do? ") 
    if an == "1":
      print("\n LOADING ... ")
      os.system('pause')
      res()
      crop()
      print("\n COMPLETED ... ")
      os.system('pause')
    elif an == "2":
      print("\n Student Deleted") 
    elif an == "3":
      print("\n Student Record Found") 
    elif an == "4":
      print("\n Goodbye")
      ans = False
    elif an != "":
      print("\n NOT VALID CHOICE, PLEASE TRY AGAIN")
      
os.system('pause')
os.system('exit')

