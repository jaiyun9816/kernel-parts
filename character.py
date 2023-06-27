from base.kernel_object import KernelObject

class Character(KernelObject) :
    def __init__(self):
        super().__init__()
        self.stamina = 10