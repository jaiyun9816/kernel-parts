from base.parts_model import PartsModel
import dill

class HumanTempIdle(PartsModel) :
    def __init__(self):
        super().__init__()
        
    def run_parts(self) : 
        if self.kernel_obj.human_temperature >= 35 : 
            self.kernel_obj.human_temperature -= 0.3
            print("human_temperature -0.3")
        

if __name__ == '__main__' :
    snapshot = HumanTempIdle()
    with open(f'./snapshot/human_temp_idle.simx', 'wb') as f :
        dill.dump(snapshot, f)