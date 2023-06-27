from base.kernel_model import KernelModel
import dill

class Kernel_Game(KernelModel) :
    def __init__(self, kernel_source):
        super().__init__(kernel_source)
        self.set_parts()
    
    def set_parts(self):
        #state에 맞는 parts
        parts = []
        if self.state == "IDLE" :
            parts = ["buff", "debuff"]
        elif self.state == "danger" :
            parts = ["debuff"]
        
        self.update_parts(parts)
        pass
        
    def update_parts(self, parts) :
        self.parts = []
        for snap in parts :
            with open(f'./snapshot/{snap}.simx', 'rb') as f :
                parts_model = dill.load(f)
                parts_model.set_kernel(self.source)
                self.parts.append(parts_model)
                
    def update_kernel_obj(self):
        pass
    
    def exit_kernel(self):
        if self.kernel_obj.stamina <= 0 :
            print("dead")
        return False
                
    def run_kernel(self):
        if self.kernel_obj.stamina <= 5 :
            state = "danger"
            if self.state != state :
                self.state = state
                print("\nchange state :", self.state)
                self.set_parts()
        
        self.run_parts()
        self.exit_kernel()
        