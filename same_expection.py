import numpy as np
import matplotlib.pyplot as plt

# 生成两个不同分布的随机变量
# 可以使用numpy中的随机数生成函数来生成不同分布的随机变量

# 第一个分布：正态分布
mean1 = 0
std1 = 1
size = 10000
distribution1 = np.random.normal(mean1, std1, size)

# 第二个分布：均匀分布
# 均匀分布的范围可以根据具体情况调整
min_value = -2
max_value = 2
distribution2 = np.random.uniform(min_value, max_value, size)

# 计算期望
mean_distribution1 = np.mean(distribution1)
mean_distribution2 = np.mean(distribution2)

# 绘制直方图
plt.hist(distribution1, bins=50, alpha=0.5, label='Normal Distribution')
plt.hist(distribution2, bins=50, alpha=0.5, label='Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distributions with Same Mean')
plt.legend()
plt.show()

print("Mean of Normal Distribution:", mean_distribution1)
print("Mean of Uniform Distribution:", mean_distribution2)
