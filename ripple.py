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

        for theta in range(0, 314):
            logic_x = center_x + (r * math.cos(theta / 50))
            logic_y = center_y + (r * math.sin(theta / 50))

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
        self.__circle(self.radius, self.x, self.y, 1, blue)
        self.__circle(self.radius - 1, self.x, self.y, .5, blue)
        self.__circle(self.radius - 2, self.x, self.y, 0, blue)
        self.radius += 1


rip_array = [0,0,0,0,0]
last_time = time.time()-4
i = 0

while True:
    if last_time + 1 < time.time():
        rip_array[i%5] = Ripple(random.randrange(0, 16), random.randrange(0, 16))
        i += 1
        last_time = time.time()
    for x in range(len(rip_array)):
        if type(rip_array[x]) != int:
            rip_array[x].move_ripple()
    unicornhathd.show()
