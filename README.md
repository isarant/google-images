## Google Images
Google images is a project tha you give a easy way to download images from google images \
With help of selenium pretend a Chrome browsher and Search in google for images and download them in your pc

## Parameters

-f Folder Name to save image \
-t The text that used in search \
-n The max number of downloaded images \
-s Images size in google search Any=1 Large=2 Medium=3 Icon=4

### example
google_images -f'dog' -t='dog' -n=10 -s=4 \
Create a folder 'dog' \
Search in google images for 'dog' in Icon size and save first 10 images
\
\
google_images -f'cat' -t='cat' -n=400 -s=1 \
Create a folder 'cat' \
Search in google images for 'cat' in Any size and save first 400 images


## Requirements

Python 3.6+. \
Selenium 
>
