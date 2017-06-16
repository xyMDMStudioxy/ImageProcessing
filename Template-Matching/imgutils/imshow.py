
import cv2
from matplotlib import pyplot as plt

def imshow(img):
    
    if img is None: return
    
    if img.ndim == 3:
        if img.shape[2] == 3: imgDisplay = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        elif img.shape[3] == 4: imgDisplay = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        else: imgDisplay = None
        
        if imgDisplay is not None: 
            plt.imshow(imgDisplay)
            _ = plt.xticks([]), plt.yticks([])
        
    elif img.ndim == 2: 
        imgDisplay = img
        plt.imshow(imgDisplay, cmap = 'gray', interpolation = 'nearest')
        _ = plt.xticks([]), plt.yticks([])
