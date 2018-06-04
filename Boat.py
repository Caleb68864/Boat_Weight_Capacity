from Calculator import Calculator


class Boat:
    def __init__(self):
        self.Main_Dims = {"height": 0,
                          "width": 0,
                          "length": 0
                          }
        self.Bow_Dims = {"height": 0,
                          "width": 0,
                          "length": 0
                          }

        self.Capacity = 0

    def getCapacity(self):
        main_cft = 1
        bow_cft = 1
        for key in self.Main_Dims:
            main_cft = main_cft * self.Main_Dims[key]

        for key in self.Bow_Dims:
            bow_cft = bow_cft * self.Bow_Dims[key]

        total_cft = main_cft + bow_cft;
        # print(main_cft)
        # print(bow_cft)
        # print(total_cft)
        calc = Calculator();
        gallons = calc.cfttogal(total_cft)
        self.Capacity = calc.galtolb(gallons)

    # Get Tons per Inch Immersion
    def getTPI(self):
        return self.Capacity / (self.Main_Dims['height'] * 12)

    def getDraftforlb(self, lb):
        return lb / self.getTPI()