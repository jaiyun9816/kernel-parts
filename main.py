from kernel_arctic import KernelArctic
from human import Human

kernel_obj = Human()
source = kernel_obj.get_source()

kernel = KernelArctic(source)

idx = 0


for i in range(20):
    idx += 1
    print(f"\n[count{idx}]\nHuman temperature : {round(kernel_obj.human_temperature, 1)}")
    print(f"Out temperature {round(kernel_obj.out_temperature, 1)}")
    kernel.run_kernel()
