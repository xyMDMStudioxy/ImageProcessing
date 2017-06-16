#!/usr/bin/env python

import numpy as np
import cv2
    
####################################
#              Program             #
####################################

# Zu untersuchendes Image wird als Grauwertbild geladen.
img = cv2.imread('FlascheTM/Flasche00.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Template Image wird als Grauwertbild geladen.
templateImg = cv2.imread('FlascheTM/Pfand_sw.jpg')
templateImg = cv2.cvtColor(templateImg, cv2.COLOR_BGR2GRAY)

# Correlation coefficient mit Normalization um Beleuchtungseinfluss zu reduzieren.
resultImg = cv2.matchTemplate(img, templateImg, cv2.TM_CCOEFF_NORMED)
min, max, minL, maxL = cv2.minMaxLoc(resultImg)
top_left = maxL
# Höhe und Breite des Template Images.
w = 126
h = 148
bottom_right = (top_left[0] + w, top_left[1] + h)
# Zeichnet weißes (255) Rechteck mit Pixelbreite 6 um gefundenes Objekt.
cv2.rectangle(img, top_left, bottom_right, 255, 6)

# Window Fenster werden aufgebaut...
# ... zu untersuchendes Image mit dem gefundenen Objekt.
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.moveWindow('Image', 0, 0)
cv2.imshow('Image', img)

# ... Vorlage Image das gesucht wird.
cv2.namedWindow('Template Image', cv2.WINDOW_NORMAL)
cv2.moveWindow('Template Image', 600, 0)
cv2.imshow('Template Image', templateImg)

# ... Correlation coefficient Ergebnis Image.
cv2.namedWindow('Result Image', cv2.WINDOW_NORMAL)
cv2.moveWindow('Result Image', 900, 0)
cv2.imshow('Result Image', resultImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
