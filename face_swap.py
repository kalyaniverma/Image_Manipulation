import cv2
model=cv2.CascadeClassifier('opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

photo1=cv2.imread('man1.png')
face1=model.detectMultiScale(photo1)

x1_m1=face1[0][0]
y1_m1=face1[0][1]
x2_m1=x1_m1+face1[0][2]
y2_m1=y1_m1+face1[0][3]

photo2=cv2.imread('man2.jpg')
face2=model.detectMultiScale(photo2)

x1_m2=face2[0][0]
y1_m2=face2[0][1]
x2_m2=x1_m2+379
y2_m2=y1_m2+379

# Displaying first picture
cv2.imshow('pic1',photo1)
cv2.waitKey()
cv2.destroyAllWindows

# Displaying second picture
cv2.imshow('pic2',photo2)
cv2.waitKey()
cv2.destroyAllWindows

# Swapping face of photo2 with photo1
photo1[y1_m1:y2_m1,x1_m1:x2_m1]=photo2[y1_m2:y2_m2,x1_m2:x2_m2]

# Swapped face of photo1
cv2.imshow('pic1',photo1)
cv2.waitKey()
cv2.destroyAllWindows

# Swapping face of photo1 with photo2
photo1=cv2.imread('man1.png')
photo2[y1_m2:y2_m2,x1_m2:x2_m2]=photo1[y1_m1:y2_m1,x1_m1:x2_m1]

# Swapped face of photo2
cv2.imshow('pic2',photo2)
cv2.waitKey()
cv2.destroyAllWindows
