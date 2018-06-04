from Boat import Boat

if __name__ == '__main__':
    boat = Boat()
    height = 1.5
    width = 4
    boat.Main_Dims = {"height": height,
                      "width": width,
                      "length": 8
                      }
    boat.Bow_Dims = {"height": height,
                      "width": width,
                      "length": 2
                      }
    boat.getCapacity()
    print("Capacity: {}".format(boat.Capacity))
    print("TPI: {}".format(boat.getTPI()))
    lb = 8*250+50
    print("Draft for {} lbs: {}".format(lb, boat.getDraftforlb(lb)))