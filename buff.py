from base.parts_model import PartsModel
import dill
class Buff(PartsModel) :
    def __init__(self):
        super().__init__()
        
    def run_parts(self) : 
        self.kernel_obj.stamina += 1
        print("buff stamina +1")

if __name__ == '__main__' :
    snapshot = Buff()
    with open(f'./snapshot/buff.simx', 'wb') as f :
        dill.dump(snapshot, f)