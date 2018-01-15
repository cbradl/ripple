import math
import unicornhathd
import time

#bloop
r = 7

center_x = 7
center_y = 7

original_pixel_x = center_x+r
original_pixel_y = center_y

count = 0

for theta in range(0, 628):
    pixel_x = center_x+r*math.cos(theta/100)
    pixel_y = center_y+r*math.sin(theta/100)

    if abs(pixel_x - original_pixel_x) > 1:
        unicornhathd.set_pixel_hsv(original_pixel_x, original_pixel_y, 0, .7,1 )
        original_pixel_x = int(pixel_x)
        count = 0

    elif abs(pixel_y - original_pixel_y) > 1:
        unicornhathd.set_pixel_hsv(original_pixel_x, original_pixel_y, 0, .7, 1)
        original_pixel_y = int(pixel_y)
        count = 0

    count += 1
    time.sleep(.01)
    unicornhathd.show()
#oooop
#branch_test
