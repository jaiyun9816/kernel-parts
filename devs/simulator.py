from pyevsim import SystemSimulator
from pyevsim.definition import *
from buff_model import *


ss = SystemSimulator()
engine = ss.register_engine("test", "VIRTUAL_TIME", 1)

buff = Buff_Model(0, Infinite, "Buff", "sname")
engine.register_entity(buff)

debuff = Debuff_Model(0, Infinite, "Debuff", "sname")
engine.register_entity(debuff)

engine.insert_input_port('input')
engine.coupling_relation(None, 'input', buff, 'input')
engine.coupling_relation(buff, 'next', debuff, 'next')

engine.insert_external_event('input', None)

for i in range(10) :
    print(f"[count{i}]")
    engine.simulate(1)