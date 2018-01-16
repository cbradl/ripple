import math
import unicornhathd
import time

#bloop


def circle(r, center_x, center_y, b, hue):
    sat = 0.7
    count = 0
    
    led_x = center_x + r
    led_y = center_y
    if 0 < led_x < 16 and 0 < led_y < 16:
        unicornhathd.set_pixel_hsv(led_x, led_y + .5, hue, sat, b)

    for theta in range(0, 628):
        logic_x = center_x + (r * math.cos(theta / 100))
        logic_y = center_y + (r * math.sin(theta / 100))

        if abs(logic_x - led_x) > 1:
            print(str(led_x) + ", " + str(led_y))
            if 0 < led_x < 16 and 0 < led_y < 16:
                unicornhathd.set_pixel_hsv(led_x, led_y, hue, sat, b)
            led_x = int(round(logic_x))
            count = 0

        elif abs(logic_y - led_y) > 1:
            print(str(led_x) + ", " + str(led_y))
            if 0 < led_x < 16 and 0 < led_y < 16:
                unicornhathd.set_pixel_hsv(led_x, led_y, hue, sat, b)
            led_y = int(round(logic_y))
            count = 0

        count += 1


def single_ripple(radius, x, y, color):
    for r in range(1, radius):
        circle(r, x, y, 1, color)
        circle(r - 1, x, y, .5, color)
        unicornhathd.show()
        time.sleep(.1)
        circle(r - 1, x, y, 0, color)


blue = .666

single_ripple_circle(8, 7.5, 7.5, blue)
single_ripple_circle(5, 3.5, 3.5, blue)
single_ripple_circle(15, 12.5, 3.5, blue)


#oooop
#branch_test
