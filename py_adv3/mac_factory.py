MINI14 = '1.4Ghz Mac mini'


class AppleFactory:
    class MacMini14:
        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = 'Intel HD'

        def __str__(self):
            info = (f'Model: {MINI14}',
                    f'Pamięć: {self.memory},'
                    f'HDD: {self.hdd}')
            return '\n'.join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            msg = f'Nie znam modelu {model}'
            print(msg)


class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = (f'Pamięć: {self.memory}',
                f'HDD: {self.hdd}')
        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AS894380293')

    def config_memory(self, amount):
        self.computer.memory = amount

    def config_hdd(self, amount):
        self.computer.hdd = amount

    def config_gpu(self, model):
        self.computer.gpu = model


class HardwareEng:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        steps = (self.builder.config_memory(memory),
                 self.builder.config_hdd(hdd),
                 self.builder.config_gpu(gpu))
        [step for step in steps]

    @property
    def computer(self):
        return self.builder.computer

def main():
    engineer = HardwareEng()
    engineer.construct_computer(hdd=500,
                                memory=8,
                                gpu="GeForce GTX")
    computer = engineer.computer
    print(computer)


if __name__ == '__main__':
    # fac = AppleFactory()
    # mac_mini = fac.build_computer(MINI14)
    # print(mac_mini)
    main()
