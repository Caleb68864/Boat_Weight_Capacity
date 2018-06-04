class Calculator:
    def __init__(self):
        pass

    def cfttogal(self, cft):
        return cft * 7.4805;

    #weight of gallons of water in lb.
    def galtolb(self, gal):
        return gal * 8.35

    def volumecube(self, height, width, length):
        return height * width * length

    def volumehalfcube(self, height, width, length):
        return self.volumecube(height, width, length) / 2
