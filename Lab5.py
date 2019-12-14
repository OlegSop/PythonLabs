# SOLID
# SRP: клас Phone інійціалізує телефон, клас CheckPhone перевіряє справність елементів телефона


class Phone:
    def __init__(self, cpu, memory, operator, screen):
        self.cpu = cpu
        self.memory = memory
        self.operator = operator
        self.screen = screen

    def call(self):
        pass


class CheckPhone:
    def createReport(self, point):
        if point == "Camera":
            pass
        elif point == "CPU":
            pass
        elif point == "SIM-card":
            pass
        elif point == "Screen":
            pass
        else:
            print("No point for check")


# OCP: Розділяємо клас CheckPhone на підкласи
class CheckPhoneCamera(CheckPhone):
    def createReport(self):
        print("Camera has min damage")


class CheckPhoneCPU(CheckPhone):
    def createReport(self):
        print("Processor loaded at 47%")


class CheckPhoneSIM(CheckPhone):
    def __init__(self):
        self.operator = Phone.operator

    def createReport(self):
        print("Your operator: {}".format(self.operator))


class CheckPhoneScreen(CheckPhone):
    def createReport(self):
        print("The screen is not damaged")


# LSP & ISP: Змінюємо клас Phone на клас Smartphone
class SmartPhone:
    def __init__(self, cpu, memory, operator, screen, camera):
        self.cpu = cpu
        self.memory = memory
        self.operator = operator
        self.screen = screen
        self.camera = camera

    def call(self):
        value = input("Enter phone number: ")
        print(f"Forwarding with number {value}")

    def make_photo(self):
        print("Not enough memory")

    def connect_to_internet(self):
        value = input("Enter type of connection: ")
        if value == "wifi":
            print("Phone connected to wifi")
        elif value == "4g":
            print("Phone connected to LTE")
        else:
            print("Phone connected to WCDMA")


class HomePhone:
    def __init__(self, operator, type):
        self.operator = operator
        self.type = type

    def call(self):
        value = input("Enter phone number: ")
        print(f"Forwarding with number {value}")


if __name__ == '__main__':
    Panasonic = HomePhone("Vodafone", "Radiophone")
    Samsung_S9 = SmartPhone("Samsung Exynos 9810", "4 GB", "Lifecell", "Super AMOLED", "Super Speed Dual Pixel")
    Samsung_S9.connect_to_internet()
    Samsung_S9.make_photo()
    Panasonic.call()


