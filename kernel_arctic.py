from base.kernel_model import KernelModel
import dill
import time

class KernelArctic(KernelModel) :
    def __init__(self, kernel_source):
        super().__init__(kernel_source)
        self.state = "normal"
        self.set_parts()
    
    def set_parts(self):
        #state에 맞는 parts
        parts = []
        if self.state == "normal" :
            parts = ["out_temp_down", "human_temp_idle", "coveralls_change_on"]
        elif self.state == "cold" :
            parts = ["out_temp_up", "human_temp_coveralls", "coveralls_change_out"]
        
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
        if self.kernel_obj.out_temperature > 40 :
            print("[out temperature is 40] : exit")
            return False
        return True
                
    def run_kernel(self):
        if "coveralls" in self.kernel_obj.coveralls :
            state = "cold"
        else :
            state = "normal"
        
        if self.state != state :
            self.state = state
            print(f"<<change state : {self.state}>>")
            self.set_parts()  
        
        self.run_parts()
        self.exit_kernel()
        time.sleep(1)
        