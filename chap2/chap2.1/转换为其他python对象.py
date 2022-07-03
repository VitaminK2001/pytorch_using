# 将深度学习框架定义的张量转换为numpy张量
import torch

x = torch.arange(3)
a = x.numpy()
b = torch.tensor(a)  # torch张量和numpy数组可以互相转换
print(type(a), type(b))

a = torch.tensor([3.5])
print(a, a.item(), float(a), int(a))  # 要将大小为1 的张量转换为python标量，可以用item函数

