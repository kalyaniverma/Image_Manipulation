import cv2
import numpy

cn=numpy.zeros((780,1500,3))
cn.fill(255)

brown=[29,60,116]
silver=[192,192,192]

# left
photo=cv2.line(cn,(500,630),(500,300),4)
# right
photo=cv2.line(cn,(1000,630),(1000,300),4)
# top left
photo=cv2.line(cn,(750,150),(500,300),brown,15)
# top right
photo=cv2.line(cn,(750,150),(1000,300),brown,15)

# left line gate
photo=cv2.line(cn,(550,630),(550,480),1)
# right line gate
photo=cv2.line(cn,(650,630),(650,480),1)
def tri(cn,x1,y1,x2,y2,x3,y3):
    photo=cv2.line(cn,(x1,y1),(x2,y2),brown,5)
    photo=cv2.line(cn,(x2,y2),(x3,y3),brown,5)
    photo=cv2.line(cn,(x1,y1),(x3,y3),1)
tri(cn,550,480,600,430,650,480)

# window frame
photo=cv2.rectangle(cn,(720,530),(920,380),brown,3)
# window horizontal
photo=cv2.line(cn,(720,450),(920,450),brown,3)
# window vertical
photo=cv2.line(cn,(820,530),(820,380),brown,3)
# window bottom
photo=cv2.line(cn,(720,530),(920,530),brown,10)

# top window frame
photo =cv2.ellipse(cn,(750,275),(40,80),180,0,180,brown,3)
# top window horizontal
photo=cv2.line(cn,(715,235),(785,235),brown,3)
# top window vertical
photo=cv2.line(cn,(750,195),(750,275),brown,3)
# top window bottom
photo=cv2.line(cn,(710,275),(790,275),brown,10)

# left inner gate
photo =cv2.line(cn, (575, 630), (575, 505),1)
# right inner gate
photo=cv2.line(cn,(625,630),(625,505),1)
# top inner gate
photo=cv2.line(cn,(575,505),(625,505),1)

# door
photo=cv2.line(cn,(600,630),(600,505), brown,1)
# left door handle
photo=cv2.circle(cn, (595,567),5,brown,1)
# right door handle
photo=cv2.circle(cn, (605,567),5,brown,1)

# bottom
photo=cv2.line(cn,(500,630),(1000,630),brown,10)

# Moon
photo=cv2.circle(cn, (1250,110),70,silver,1)

cv2.imwrite("image.jpg",photo)

from PIL import Image, ImageDraw
img = Image.open(R"image.jpg")
img1=img.convert("RGB")

blue=(136,196,255)
yellow=(255,255,60)
brown=(116,60,29)
orange=(255,128,0)
purple=(128,0,128)
dark_blue=(0,0,62)
silver=(192,192,192)

# window left bottom
ImageDraw.floodfill(img, (815,460) , blue, thresh=50)
# window right bottom
ImageDraw.floodfill(img, (830,460) , blue, thresh=50 )
# window left top
ImageDraw.floodfill(img, (815,440) , blue, thresh=50)
# window right top
ImageDraw.floodfill(img, (830,440) , blue, thresh=50)

# top window left bottom
ImageDraw.floodfill(img, (720,240) , blue, thresh=50)
# top window right bottom
ImageDraw.floodfill(img, (760,240) , blue, thresh=50)
# top window left top
ImageDraw.floodfill(img, (720,230) , blue, thresh=50)
# top window right top
ImageDraw.floodfill(img, (760,230) , blue, thresh=50)

# Bg color
ImageDraw.floodfill(img, (510,250) ,dark_blue , thresh=50)
# hut
ImageDraw.floodfill(img, (900,620) , yellow, thresh=50)
# outer gate
ImageDraw.floodfill(img, (574,504) , brown, thresh=50)

# left inner gate
ImageDraw.floodfill(img, (576,506) , orange, thresh=50)
# right inner gate
ImageDraw.floodfill(img, (620,506) , orange, thresh=50)

# left door handle
ImageDraw.floodfill(img, (596,568),purple, thresh=50)
# right door handle
ImageDraw.floodfill(img, (606,568),purple, thresh=50)

# triangle
ImageDraw.floodfill(img, (600,440),orange, thresh=50)

# Moon
ImageDraw.floodfill(img, (1250,110),silver, thresh=50)

# Displaying Image
img.show()
