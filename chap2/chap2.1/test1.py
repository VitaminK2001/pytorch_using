import torch

x = torch.arange(12)
print(x)
print(x.shape) # [12]
print(x.size()) # [12]

x = x.reshape(3, 4) # (高度，宽度)
print(x)
print(x.shape) # [3,4]
print(x.size()) # [3,4]

y = torch.zeros(2,3,4)  # (个数，高度，宽度)
print(y)
print(y.shape)  # [2,3,4]

z = torch.randn(3,4)
print(z)



