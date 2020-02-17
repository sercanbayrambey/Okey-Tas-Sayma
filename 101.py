from cv2 import cv2
import numpy as np
from PIL import ImageGrab 
import threading
import time
import keyboard
import math
temp_sol_ust=np.array
temp_sol_alt=np.array
temp_sag_ust=np.array
temp_sag_alt = np.array
sol_alt = np.array
sol_ust=np.array
sag_alt=np.array
sag_ust = np.array
taslar = np.array
i = 0
widthCounter=10
sayac = 0
heightCounter=0
tursayisi=0
eklenecek_tas = np.array
durum = 5
sleepTime = 0.1
sonEklenenTas = 5
eklenecekMi = False
tasWindowHeight = 290
tasWindowWidth = 955

leftX=23
topY=45
rightX=leftX+790
bottomY=topY+320

tasWidth = 38
tasHeight = 50


def main():
  global i,widthCounter,sayac,tursayisi,eklenecek_tas
  global sag_alt,sag_ust,sol_alt,sol_ust,temp_sag_alt,temp_sag_ust,temp_sol_alt,temp_sol_ust
  global taslar,durum

  threading.Timer(0.1, KeyPress).start()
  threading.Timer(0.1, Tarama).start()

     
def Tarama():

  while(True):
    global i,widthCounter,sayac,tursayisi,eklenecek_tas
    global sag_alt,sag_ust,sol_alt,sol_ust,temp_sag_alt,temp_sag_ust,temp_sol_alt,temp_sol_ust
    global taslar,durum
    global leftX,topY,rightX,bottomY,tasWidth,tasHeight,sonEklenenTas
    window = np.array(ImageGrab.grab(bbox=(0,230,851,750))) # X1,Y1,X2,Y2
    window[0:700,leftX+50:rightX] = 0,0,0
    window[topY+tasWidth+10:bottomY,0:955] = 0,0,0
    window[0:topY,0:955] = 0,0,0 
    window[bottomY+tasWidth+10:800,0:955] = 0,0,0 

    if(i==0):
        taslar = np.zeros((tasWindowHeight,tasWindowWidth,3), np.uint8)
        taslar[tasWindowHeight-20:tasWindowHeight,0:tasWindowWidth-math.floor(tasWindowWidth/1.3)] = 255,0,0
        i=1
    cv2.imshow("Taslar",cv2.cvtColor(taslar,cv2.COLOR_BGR2RGB)) 
    cv2.setWindowProperty("Taslar",cv2.WND_PROP_VISIBLE,cv2.WINDOW_NORMAL)

    cv2.rectangle(window,(leftX,topY),(leftX+tasWidth,topY+tasHeight),(255,0,255)) # sol üst 
    cv2.rectangle(window,(rightX,topY),(rightX+tasWidth,topY+tasHeight),(255,0,255)) #sag üst
    cv2.rectangle(window,(leftX,bottomY),(leftX+tasWidth,bottomY+tasHeight),(255,0,255)) #sol alt
    cv2.rectangle(window,(rightX,bottomY),(rightX+tasWidth,bottomY+tasHeight),(255,0,255)) #sağ alt
    temp_sol_ust = window[topY:topY+tasHeight,leftX:leftX+tasWidth]
    temp_sol_alt = window[bottomY:bottomY+tasHeight,leftX:leftX+tasWidth]
    temp_sag_ust = window[topY:topY+tasHeight,rightX:rightX+tasWidth]    #Karsilastir fonksiyonu, tum seyleri karsilastirsin ayni olmayanları return donsun 
    temp_sag_alt = window[bottomY:bottomY+tasHeight,rightX:rightX+tasWidth]  
    ## ARAMAYI BAŞLAT 

    if(durum != 5):
      durum = Karsilastir()
    eklenecekMi = False
    if(durum == 0 and sonEklenenTas != 0):
      print("Sol ust tas degisti")
      eklenecek_tas = sol_ust
      sonEklenenTas = 0
      eklenecekMi = True
      
    elif(durum == 1 and sonEklenenTas != 1):
      print("Sol alt tas degisti")
      eklenecek_tas = sol_alt
      sonEklenenTas = 1
      eklenecekMi = True
      
    elif(durum == 2 and sonEklenenTas != 2):
      print("Sag Ust tas degisti")
      eklenecek_tas = sag_ust
      sonEklenenTas = 2
      eklenecekMi = True

    elif(durum == 3 and sonEklenenTas != 3):
      print("Sag Alt tas degisti")
      eklenecek_tas = sag_alt 
      sonEklenenTas = 3
      eklenecekMi = True
  

    if(durum != -1 and durum != 5 and eklenecekMi):
      Ekle()
        
    
  
    cv2.imshow("Ana Pencere",cv2.cvtColor(window,cv2.COLOR_BGR2RGB))
    
   
    """ cv2.resizeWindow("Taslar",200,700)
    cv2.resizeWindow("Ana Pencere",200,700) """
      

    if(cv2.waitKey(25) & 0xFF == ord('q')): 
        cv2.destroyAllWindows()

    if(durum==5):
          time.sleep(0.05)
    else:
          time.sleep(1.3)

          



def KeyPress():
  while True:
    global i,widthCounter,sayac,tursayisi,eklenecek_tas,heightCounter,durum,taslar
    if(keyboard.is_pressed('f3')): 
      print("reset")
      widthCounter = 10
      tursayisi = 0
      sayac = 0
      heightCounter = 0
      i = 0
      sonEklenenTas = 5
    if(keyboard.is_pressed('f1') and durum==5): 
      print("Arama başlatıldı.")
      durum = -1
      taslar[tasWindowHeight-20:tasWindowHeight,0:tasWindowWidth-math.floor(tasWindowWidth/1.3)] = 0,255,0
      

    if(keyboard.is_pressed('f2') and durum != 5):
      print("Arama durduruldu") 
      durum = 5
      taslar[tasWindowHeight-20:tasWindowHeight,0:tasWindowWidth-math.floor(tasWindowWidth/1.3)] = 255,0,0


    time.sleep(0.2)



def Karsilastir():
  global sag_alt,sag_ust,sol_alt,sol_ust,temp_sag_alt,temp_sag_ust,temp_sol_alt,temp_sol_ust
  if (np.array_equal(sol_ust, temp_sol_ust) == False) :
    sol_ust = temp_sol_ust
    return 0 #sol ust degisti
  elif(np.array_equal(sol_alt, temp_sol_alt) == False):
    sol_alt = temp_sol_alt
    return 1
  elif(np.array_equal(sag_ust, temp_sag_ust) == False):
    sag_ust = temp_sag_ust
    return 2
  elif(np.array_equal(sag_alt, temp_sag_alt) == False):
    sag_alt = temp_sag_alt
    return 3

  return -1

def Ekle():
  global taslar,eklenecek_tas,widthCounter,sayac,heightCounter,tursayisi
  global leftX,topY,rightX,bottomY,tasWidth,tasHeight
  taslar[10+heightCounter:heightCounter+tasHeight+10,widthCounter+10:widthCounter+tasWidth+10] = eklenecek_tas 
  widthCounter = widthCounter+38 #y 55 x 40
  sayac+=1
  if(sayac == math.floor(tasWidth/2)):
    sayac = 0
    tursayisi+=1
    heightCounter = (tasHeight+10)*tursayisi 
    widthCounter = 10


main()