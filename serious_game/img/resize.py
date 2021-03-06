import cv2 as cv                                                                                                                                                                                    
import os                                                                                                                                                                                           

target_height = 250

for filename in os.listdir('.'):
  if (not filename.endswith('.jpg')) or filename.endswith('_fit.jpg'):
    continue

  new_filename = filename[:-4] + '_fit.jpg' 
  img = cv.imread(filename) 
  h, w, c = img.shape 
  print(f'Image {filename} has shape {img.shape}')

  resized = cv.resize(img, (w*target_height//h, target_height))
  cv.imwrite(new_filename, resized)
