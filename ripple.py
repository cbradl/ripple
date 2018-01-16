import math
import unicornhathd
import time
import random

#bloop


class Ripple:
    def __init__(self, x, y):
        self.radius = 2
        self.x = x
        self.y = y

    def __circle(self, r, center_x, center_y, b, hue):
        sat = 0.7

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

            elif abs(logic_y - led_y) > 1:
                print(str(led_x) + ", " + str(led_y))
                if 0 < led_x < 16 and 0 < led_y < 16:
                    unicornhathd.set_pixel_hsv(led_x, led_y, hue, sat, b)
                led_y = int(round(logic_y))


    def move_ripple(self):
        blue = .666
        self.circle(self.radius, self.x, self.y, 1, blue)
        self.circle(self.radius - 1, self.x, self.y, .5, blue)
        self.circle(self.radius - 2, self.x, self.y, 0, blue)
        self.radius += 1


first = Ripple(2, 2)
second = Ripple(13, 13)

for i in range(0, 10):
    first.move_ripple()
    second.move_ripple()
    unicornhathd.show()

'''
blue = .666
x = 1
y = 1

single_ripple(15, x + .5, y + .5, blue)
single_ripple(15, 14 + .5, 14 + .5, blue)

while x < 14:
    last_time = time.time()+4.11
    if last_time + 4 < time.time():
        single_ripple(random.randrange(5, 16), x + .5, y + .5, blue)
        last_time = time.time()
        x += 2
        y += 2'''

