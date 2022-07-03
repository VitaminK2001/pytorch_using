import torch

a = torch.arange(3).reshape(3,1)
print(torch.arange(2))
b = torch.arange(2).reshape(1,2)
print(b[0])


print(a+b) # 矩阵a将复制列，矩阵b将赋值行


