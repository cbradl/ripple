import math
import unicornhathd

#bloop
r = 3

center_x, center_y = 7

original_pixel_x = center_x+r
original_pixel_y = center_y

count = 0

for theta in range(0, 360):
    pixel_x = center_x+r*cos(theta)
    pixel_y = center_y+r*sin(theta)

    if abs(pixel_x - original_pixel_x) > 1:
        unicornhathd.set_pixel_hsv(origina_pixel_x, original_pixel_y, 0, .7, count / 8)
        original_pixel_x = int(pixel_x)
        count = 0

    if abs(pixel_y - original_pixel_y) > 1:
        unicornhathd.set_pixel_hsv(origina_pixel_x, original_pixel_y, 0, .7, count / 8)
        original_pixel_y = int(pixel_y)
        count = 0

    count += 1

unicornhathd.show()