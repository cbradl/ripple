import math
import unicornhathd
import time

#bloop
r = 7

center_x = 7.5
center_y = 7.5

original_pixel_x = center_x+r
original_pixel_y = center_y

count = 0

unicornhathd.set_pixel_hsv(original_pixel_x, original_pixel_y + .5, 0, .7, 1)
unicornhathd.show()

for theta in range(0, 628):
    pixel_x = center_x+(r*math.cos(theta/100.))
    pixel_y = center_y+(r*math.sin(theta/100.))

    if abs(pixel_x - original_pixel_x) > 1:
        print(str(original_pixel_x) + ", " + str(original_pixel_y))
        unicornhathd.set_pixel_hsv(original_pixel_x, original_pixel_y, 0, .7,1 )
        original_pixel_x = int(round(pixel_x))
        count = 0

    elif abs(pixel_y - original_pixel_y) > 1:
        print(str(original_pixel_x) + ", " + str(original_pixel_y))
        unicornhathd.set_pixel_hsv(original_pixel_x, original_pixel_y, 0, .7, 1)
        original_pixel_y = int(round(pixel_y))
        count = 0

    count += 1
    time.sleep(.001)
    unicornhathd.show()
#oooop
#branch_test
