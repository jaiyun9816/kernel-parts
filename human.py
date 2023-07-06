from base.kernel_object import KernelObject

class Human(KernelObject) :
    def __init__(self):
        super().__init__()
        self.human_temperature = 36.8
        self.coveralls = []
        self.out_temperature = 3