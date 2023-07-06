from base.parts_model import PartsModel
import dill

class CoverallsChangeOut(PartsModel) :
    def __init__(self):
        super().__init__()
        
    def run_parts(self) : 
        if self.kernel_obj.out_temperature > 5 : 
            self.kernel_obj.coveralls = []
            print("\thuman take off coveralls")

if __name__ == '__main__' :
    snapshot = CoverallsChangeOut()
    with open(f'./snapshot/coveralls_change_out.simx', 'wb') as f :
        dill.dump(snapshot, f)