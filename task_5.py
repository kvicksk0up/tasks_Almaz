from time import sleep

class Trafficlight:

    def color_red(self):
        self.red = sleep(1)
        print('red')

    def color_green(self):
        self.green = sleep(2)
        print('green')

    def color_yellow(self):
        self.yellow = sleep(0.5)
        print('yellow')


tl = Trafficlight()
tl.color_red()
tl.color_yellow()
tl.color_green()
