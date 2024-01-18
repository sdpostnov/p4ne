from ipaddress import IPv4Network
import random
class IPv4RandomNetwork(IPv4Network):
    def __init__(self, mask_min=8, mask_max=24):
        IPv4Network.__init__(self,
                             (random.randint(0x0B000000, 0xDF000000),
                              random.randint(mask_min, mask_max)),
                             strict=False,
                             )

    def regular(self):
        return self.is_global
net1=IPv4RandomNetwork()
print(net1,net1.regular())