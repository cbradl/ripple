import math
import unicornhathd
import time

#bloop
r = 7

center_x = 7.5
center_y = 7.5

led_x = center_x + r
led_y = center_y

count = 0

unicornhathd.set_pixel_hsv(led_x, led_y + .5, 0, .7, 1)
unicornhathd.show()

for theta in range(0, 628):
    logic_x = center_x + (r * math.cos(theta / 100))
    logic_y = center_y + (r * math.sin(theta / 100))

    if abs(logic_x - led_x) > 1:
        print(str(led_x) + ", " + str(led_y))
        unicornhathd.set_pixel_hsv(led_x, led_y, 0, .7, 1)
        led_x = int(round(logic_x))
        count = 0

    elif abs(logic_y - led_y) > 1:
        print(str(led_x) + ", " + str(led_y))
        unicornhathd.set_pixel_hsv(led_x, led_y, 0, .7, 1)
        led_y = int(round(logic_y))
        count = 0

    count += 1
    time.sleep(.001)
    unicornhathd.show()
#oooop
#branch_test
