import numpy as np
import cv2
from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
def featureMatching():
    
    img1= cv2.imread('1.PNG', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('4-1canny(40,100).png', cv2.IMREAD_GRAYSCALE)
    corr = signal.correlate2d(img1, img2, boundary='symm', mode='same')
    y, x = np.unravel_index(np.argmax(corr), corr.shape) # find
    fig, (ax_orig, ax_template, ax_corr) = plt.subplots(1, 3)
    ax_orig.imshow(img1, cmap='gray')
    ax_orig.set_title('Original')
    ax_orig.set_axis_off()
    ax_template.imshow(img2, cmap='gray')
    ax_template.set_title('Template')
    ax_template.set_axis_off()
    ax_corr.imshow(corr, cmap='gray')
    ax_corr.set_title('Cross-correlation')
    ax_corr.set_axis_off()
    ax_orig.plot(x, y, 'ro')
    fig.show()
 
featureMatching()
