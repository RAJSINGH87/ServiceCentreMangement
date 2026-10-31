import cv2
import os
from datetime import datetime

def click_photo(prefix='photo'):
    os.makedirs('photos', exist_ok=True)
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)   
    res, img = cam.read()
    cam.release()                              
    if res:
        name = f"photos/{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(name, img)
        return name                            
    return None