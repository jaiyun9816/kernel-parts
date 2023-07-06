from base.parts_model import PartsModel
import dill

class CoverallsChangeOn(PartsModel) :
    def __init__(self):
        super().__init__()
        
    def run_parts(self) : 
        if self.kernel_obj.out_temperature < 0 or  self.kernel_obj.human_temperature <= 35.5 : 
            self.kernel_obj.coveralls.append("coveralls")
            print("\thuman get dressed coveralls")

if __name__ == '__main__' :
    snapshot = CoverallsChangeOn()
    with open(f'./snapshot/coveralls_change_on.simx', 'wb') as f :
        dill.dump(snapshot, f)