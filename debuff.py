from base.parts_model import PartsModel
import dill

class Debuff(PartsModel) :
    def __init__(self):
        super().__init__()
        
    def run_parts(self) : 
        self.kernel_obj.stamina -= 2
        print("debuff stamina -2")
        
if __name__ == '__main__' :
    snapshot = Debuff()
    with open(f'./snapshot/debuff.simx', 'wb') as f :
        dill.dump(snapshot, f)