import torch

x = torch.arange(12).reshape(3,4)

print(x)

print(x[0])

x[0:2, :] = 12
print(x)


