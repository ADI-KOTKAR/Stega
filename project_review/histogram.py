from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src_base = cv.imread("test_images/sample_image.jpeg")
src_test1 = cv.imread("test_images/encrypted_text_image.png")
src_test2 = cv.imread("encoded_images/encoded_rotate.png")
src_test3 = cv.imread("encoded_images/encoded_flip.png")


if src_base is None or src_test1 is None or src_test2 is None:
    print('Could not open or find the images!')
    exit(0)
## [Load three images with different environment settings]

## [Convert to HSV]
hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
hsv_test1 = cv.cvtColor(src_test1, cv.COLOR_BGR2HSV)
hsv_test2 = cv.cvtColor(src_test2, cv.COLOR_BGR2HSV)
hsv_test3 = cv.cvtColor(src_test3, cv.COLOR_BGR2HSV)
## [Convert to HSV]

## [Convert to HSV half]
hsv_half_down = hsv_base[hsv_base.shape[0]//2:,:]
## [Convert to HSV half]

## [Using 50 bins for hue and 60 for saturation]
h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]

# hue varies from 0 to 179, saturation from 0 to 255
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges # concat lists

# Use the 0-th and 1-st channels
channels = [0, 1]
## [Using 50 bins for hue and 60 for saturation]

## [Calculate the histograms for the HSV images]
hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
plt.plot(hist_base)
plt.title("Histogram - Cover Image")
plt.show()

hist_half_down = cv.calcHist([hsv_half_down], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_half_down, hist_half_down, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

hist_test1 = cv.calcHist([hsv_test1], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test1, hist_test1, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
plt.plot(hist_test1)
plt.title("Histogram - Traditional LSB Steganography Image")
plt.show()

hist_test2 = cv.calcHist([hsv_test2], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test2, hist_test2, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
plt.plot(hist_test2)
plt.title("Histogram - Rotational LSB Steganography Image")
plt.show()

hist_test3 = cv.calcHist([hsv_test3], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test3, hist_test3, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
plt.plot(hist_test3)
plt.title("Histogram - Flipping LSB Steganography Image")
plt.show()
## [Calculate the histograms for the HSV images]


## [Apply the histogram comparison methods]
for compare_method in range(4):
    base_base = cv.compareHist(hist_base, hist_base, compare_method)
    base_half = cv.compareHist(hist_base, hist_half_down, compare_method)
    base_test1 = cv.compareHist(hist_base, hist_test1, compare_method)
    base_test2 = cv.compareHist(hist_base, hist_test2, compare_method)
    base_test3 = cv.compareHist(hist_base, hist_test3, compare_method)

    print('Method:', compare_method, 'Perfect, Base-Half, Base-Test(1), Base-Test(2), Base-Test(3) :',\
          base_base, '/', base_half, '/', base_test1, '/', base_test2, '/', base_test3)