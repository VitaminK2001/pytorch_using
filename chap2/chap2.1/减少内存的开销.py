import torch

y = torch.arange(3)
x = torch.arange(3)
before = id(y)
y = y + x
print(id(y) == before)  # 发现不是原地操作，这样会增加开销，而且有其他引用仍然指向旧的内存位置

# 可以通过切片执行原地操作
z = torch.zeros_like(y)
print('id(z):', id(z))
z[:] = x + y
print('id(z):', id(z))
z = x + y  # 这样会分配新的内存
print('id(z):', id(z))

