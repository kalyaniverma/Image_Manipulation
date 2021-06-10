# Image_Manipulation

In *image_create(hut).py*, a hut is created and floodfill function is used for coloring it.

In *face_swap.py*, 1st picture is of Mr. Bean and 2nd one is of Charlie Chaplin. Haar Cascade Model is used for detecting the faces and using their faces' dimensions, the faces are swapped with each other.

In *image_combine.py*, 1st picture is of Nobita and 2nd one is of Doraemon. First the vertical pixels of 1st image was cropped so that both the images have same length. Using hconcat() function of cv2 module, these 2 pictures are combined.

**Library Used:-**
  *OpenCV*
