import cv2

nobita=cv2.imread('nobita.png')
doraemon=cv2.imread('doraemon.png')

cv2.imshow('nobita',nobita)
cv2.waitKey()
cv2.destroyAllWindows

cv2.imshow('doraemon',doraemon)
cv2.waitKey()
cv2.destroyAllWindows

nobita=nobita[ :859 ,:]
comb_img=cv2.hconcat([nobita, doraemon])

# Displaying Combined Image
cv2.imshow('pic',comb_img)
cv2.waitKey()
cv2.destroyAllWindows
