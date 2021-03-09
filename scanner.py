import cv2
import numpy as np

def rectify(h):
    h = h.reshape((4, 2))
    hnew = np.zeros((4, 2), dtype=np.float32)

    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]
    hnew[2] = h[np.argmax(add)]

    diff = np.diff(h, axis=1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]

    return hnew


# add image here.
image = cv2.imread('1.jpg')

# resize image so it can be processed
# choose optimal dimensions such that important content is not lost
image = cv2.resize(image, (1500, 880))

# *************************

# creating copy of original image
orig = image.copy()
cv2.imshow("Original.jpg", orig)
# ***********************

# convert to grayscale and blur to smooth
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Gray.jpg", gray)
# ********************************

# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
blurred = cv2.medianBlur(gray, 5)
cv2.imshow("Original Blurred.jpg", blurred)
# *******************************

# apply Canny Edge Detection
edged = cv2.Canny(blurred, 0, 50)
orig_edged = edged.copy()
cv2.imshow("Original Edged.jpg", orig_edged)
# ******************************

# find the contours in the edged image, keeping only the
# largest ones, and initialize the screen contour
(contours, _) = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# get approximate contour
for c in contours:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * p, True)

    if len(approx) == 4:
        target = approx
        break

# mapping target points to 800x800 quadrilateral
approx = rectify(target)
pts2 = np.float32([[0, 0], [800, 0], [800, 800], [0, 800]])

M = cv2.getPerspectiveTransform(approx, pts2)
dst = cv2.warpPerspective(orig, M, (800, 800))

cv2.drawContours(image, [target], -1, (0, 255, 0), 2)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
cv2.imshow("Outline.jpg", image)
cv2.imshow("doc grayscale", dst)
# *****************************

# using thresholding on warped image to get scanned effect (If Required)
ret2, th4 = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("black and white scan", th4)

# other thresholding methods

ret, thresh1 = cv2.threshold(dst, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("binary scan", thresh1)
ret, thresh2 = cv2.threshold(dst, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow("gray scan", thresh2)


cv2.waitKey(0)
cv2.destroyAllWindows()
