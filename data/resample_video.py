import os, sys

import cv2

video_in = sys.argv[1]
video_out = sys.argv[2]
cap = cv2.VideoCapture(video_in)
fps = int(cap.get(cv2.CAP_PROP_FPS))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_out, fourcc, fps, (w, h))

while True:
    more, im = cap.read()
    if not more:
        break
    im_lo = cv2.resize(im, (w // 4, h // 4))
    im_lo_hi = cv2.resize(im_lo, (w, h))
    ymin = h * 3 // 8
    ymax = h * 5 // 8
    xmin = w * 3 // 8
    xmax = w * 5 // 8
    im_lo_hi[ymin:ymax, xmin:xmax] = im[ymin:ymax, xmin:xmax]
    out.write(im_lo_hi)
