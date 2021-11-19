from Observable import Observable

class Weather(Observable):
    def __init__(self, name):
        Observable.__init__(self, name)