from rx import create

class KernelObject :
    def __init__(self) :
        pass
    
    def get_source(self) :
        return create(self.object_rx)
    
    def object_rx(self, observer, scheduler) :
        observer.on_next(self)
        observer.on_completed()
        