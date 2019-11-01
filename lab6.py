class CPU_Ratio:
    def __init__(self,bus_speed,multiplier):
        self.bus_speed = bus_speed
        self.multiplier =  multiplier


    def set_frequency(self):
        return self.bus_speed * self.multiplier


class Processor:
    def __init__(self,brand,model,frequency):
        self.brand = brand
        self.model = model
        self.frequency = frequency

    def info(self):
        print("Model: {} {} Frequency: {} Mhz".format(self.brand,self.model,self.frequency.set_frequency()))


if __name__ == '__main__':
    frequency1 = CPU_Ratio(199.96 , 22)
    frequency2 = CPU_Ratio(99.36 , 34)
    processor1 = Processor("AMD" , "FX-8350",frequency1)
    processor2 = Processor("Intel" , "Core i5-8400",frequency2)
    processor1.info()
    processor2.info()