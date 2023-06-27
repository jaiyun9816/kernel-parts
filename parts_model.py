from abc import abstractmethod

class PartsModel :
    def __init__(self) :
        pass
        
    def set_kernel(self, kernel_source) :
        def set_agent(co) : #core data 구독
            self.kernel_obj = co
        kernel_source.subscribe(set_agent) 
     
    @abstractmethod
    def run_parts(self) :
        pass