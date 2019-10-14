import cv2

im = cv2.imread('EX_Chronos_screen02.jpg') # (1080, 1920)
h, w, c = im.shape
im_lo = cv2.resize(im, (w // 4, h // 4))
im_lo_hi = cv2.resize(im_lo, (w, h))
print(im.shape)
print(im_lo_hi.shape)
ymin = h * 3 // 8
ymax = h * 5 // 8
xmin = w * 3 // 8
xmax = w * 5 // 8
im_lo_hi[ymin:ymax, xmin:xmax] = im[ymin:ymax, xmin:xmax]
cv2.imwrite('resampled.png', im_lo_hi)

