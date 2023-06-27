from pyevsim import BehaviorModelExecutor
from pyevsim import SysMessage
from pyevsim.definition import *
from character import Character

class Buff_Model(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_state("MOVE", 0)

        self.insert_input_port("input")
        self.insert_output_port("next")
        
        self.data = Character()
        
    def ext_trans(self, port, msg):
        if port == "input":
            data = msg.retrieve()
            if data[0] != None :
                self.data = data[0]
            self.data.stamina_count(1) # 계산
            self._cur_state = "MOVE"
            

    def output(self):
        msg = SysMessage(self.get_name(), "next")
        msg.insert(self.data)
        print("buff : ", self.data.stamina)
        return msg
        
    def int_trans(self):
        if self._cur_state == "MOVE" :
            self._cur_state = "IDLE"
        else:
            self._cur_state = "MOVE"

class Debuff_Model(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_state("NEXT", 0)

        self.insert_input_port("next")
        self.insert_output_port("output")
        
        self.data = Character()
        
    def ext_trans(self, port, msg):
        if port == "next":
            data = msg.retrieve()
            if data[0] != None :
                self.data = data[0]
            self.data.stamina_count(-2) # 계산
            self._cur_state = "NEXT"
            

    def output(self):
        msg = SysMessage(self.get_name(), "output")
        msg.insert(self.data)
        print("debuff : ", self.data.stamina)
        return msg
        
    def int_trans(self):
        if self._cur_state == "NEXT" :
            self._cur_state = "IDLE"
        else:
            self._cur_state = "NEXT"