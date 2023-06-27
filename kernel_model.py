from abc import abstractmethod

class KernelModel :
    def __init__(self, kernel_source) :
        self.source = kernel_source
        self.set_kernel(kernel_source)
        
        self.parts = []

    def set_kernel(self, kernel_source) :
        def set_agent(co) : #kernel data 구독
            self.kernel_obj = co
        kernel_source.subscribe(set_agent)
    
    #parts list clear
    def clear_parts(self) :
        self.parts = []

    #parts run
    def run_parts(self) :
        for parts in self.parts :
            parts.run_parts()
    
    @abstractmethod  
    def update_kernel_obj(self) :
        self.kernel_obj.set_kernel_obj()
        
    @abstractmethod
    def exit_kernel(self) :
        pass
        
    def run_kernel(self) :
        self.run_parts()
        self.update_kernel_obj()
        self.exit_kernel()
        
        