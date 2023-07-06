from base.parts_model import PartsModel
import dill

class OutTempUp(PartsModel) :
    def __init__(self):
        super().__init__()
        
    def run_parts(self) : 
        self.kernel_obj.out_temperature += 0.5
        print("out_temperature +0.5")

if __name__ == '__main__' :
    snapshot = OutTempUp()
    with open(f'./snapshot/out_temp_up.simx', 'wb') as f :
        dill.dump(snapshot, f)