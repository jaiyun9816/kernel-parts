from base.parts_model import PartsModel
import dill

class HumanTempCover(PartsModel) :
    def __init__(self):
        super().__init__()
        
    def run_parts(self) : 
        if self.kernel_obj.human_temperature <= 37 : 
            self.kernel_obj.human_temperature += 0.3
            print("human_temperature +0.3")
        

if __name__ == '__main__' :
    snapshot = HumanTempCover()
    with open(f'./snapshot/human_temp_coveralls.simx', 'wb') as f :
        dill.dump(snapshot, f)