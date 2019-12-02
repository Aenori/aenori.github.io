import cv2 as cv                                                                                                                                                                                    
import os                                                                                                                                                                                           

for filename in os.listdir('.'):
  if (not filename.endswith('.jpg')) or filename.endswith('_fit.jpg'):
    continue

  new_filename = filename[:-4] + '_fit.jpg' 
  img = cv.imread(filename) 
  h, w, c = img.shape 
  print(f'Image {filename} has shape {img.shape}')

  resized = cv.resize(img, (w*400//h, 400))
  cv.imwrite(new_filename, resized)
