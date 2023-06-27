from kernel_game import Kernel_Game
from character import Character
import time

start_time = time.time()
kernel_obj = Character()
source = kernel_obj.get_source()

kernel = Kernel_Game(source)

idx = 0

while kernel.exit_kernel() :
    idx += 1
    print(f"[count{idx}]Stamina :", kernel_obj.stamina)
    kernel.run_kernel()
    
end_time = time.time()
execution_time = end_time - start_time

print("실행 시간:", execution_time, "초")