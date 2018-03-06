# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Print Multiple images in the same figure, pyplot
def show_images(images, cols = 1, titles = None):
    assert((titles is None)or (len(images) == len(titles)))
    n_images = len(images)
    if titles is None: titles = ['Image (%d)' % i for i in range(1,n_images + 1)]
    fig = plt.figure()
    for n, (image, title) in enumerate(zip(images, titles)):
        a = fig.add_subplot(cols, np.ceil(n_images/float(cols)), n + 1)
        if image.ndim == 2:
            plt.gray()
        plt.imshow(image)
        a.set_title(title)
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
    plt.show()

#from skimage import io, data

# Using skimage io
#lena = data.imread('lena.png', as_grey=True)
#io.imshow(lena)

# Load an color image in grayscale OpenCV
img = cv.imread('lena.png', 1)

# Display image for Windows
#cv.imshow('Lena',img)
#cv.waitKey(0)
#cv.destroyAllWindows()

# Display for Ubuntu, using pyplot
plt.figure(1)
plt.imshow(img, cmap="gray")
plt.title("Gray Lena")

# Saving image to disk with OpenCV
cv.imwrite("Lena_gray.png", img)

# Changing color spaces
# BGR -> Gray flag is cv.COLOR_BGR2GRAY
# BGR -> HSV flag is cv.COLOR_BGR2HSV
# cv.cvtColor(img, flag)

bgr_img = cv.imread('lena.png')

b,g,r = cv.split(bgr_img)       # get b,g,r
rgb_img = cv.merge([r,g,b])     # switch it to rgb

gray_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2GRAY)

hsv_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)

show_images([rgb_img, gray_img, hsv_img], titles=['RGB', 'Gray', 'HSV'])

# Transformations cv.warp_____

## Scaling
# fx and fy are resizing factors, 0.5 will result in half the size
half_img = cv.resize(rgb_img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
show_images([rgb_img, half_img], titles=['Full','Half'])

## Rotation
rows, cols, dims = rgb_img.shape
M = cv.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rot_img = cv.warpAffine(rgb_img, M, (cols, rows))
show_images([rgb_img, rot_img], titles=['Original', 'Rotated'])

## Affine Transformation
### This process takes three points from the image and their desired position
### after transformation
pts1 = np.float32([[50, 30], [200, 50], [5, 200]])
pts2 = np.float32([[10, 100], [200, 50], [50, 250]])

M = cv.getAffineTransform(pts1, pts2)
trans_img = cv.warpAffine(rgb_img, M, (cols, rows))

show_images([rgb_img, trans_img], titles=['Orginal', 'Transformed'])

## Perspective Transformation
### This transformation is useful to focus the image in just one section of it
### It needs four points, and another four that will be their positions in the
### output.
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0,0], [rows, 0], [0, cols], [rows, cols]])

M = cv.getPerspectiveTransform(pts1, pts2)
zoom_img = cv.warpPerspective(rgb_img, M, (rows, cols))

show_images([rgb_img, zoom_img], titles=['Originial', 'Zoomed and Rectified'])

# Thresholding
## Some of the types for thresholds are
ret, thresh1 = cv.threshold(rgb_img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(rgb_img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(rgb_img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(rgb_img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(rgb_img, 127, 255, cv.THRESH_TOZERO_INV)

show_images([rgb_img, thresh1, thresh2, thresh3, thresh4, thresh5],
            titles=['Original', 'BINARY', 'BINARY_INV', 'TRUNC',
                    'TOZERO', 'TOZERO_INV'],
            cols=1)

## And prebuild adaptive thresholds are
