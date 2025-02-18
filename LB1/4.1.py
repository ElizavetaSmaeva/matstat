import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import uniform

# Границы распределения
a, b = -np.sqrt(3), np.sqrt(3)

# Размеры выборок
sample_sizes = [10, 50, 1000]

# Создаём график
plt.figure(figsize=(10, 6))

# Границы оси X
x = np.linspace(a - 0.5, b + 0.5, 1000)
pdf = uniform.pdf(x, loc=a, scale=b - a)  # Плотность равномерного распределения

# Генерация и построение выборок
for size in sample_sizes:
    sample = np.random.uniform(a, b, size)
    sns.histplot(sample, kde=False, bins=20, label=f"n={size}", stat="density", alpha=0.6)

# Наложение графика плотности
plt.plot(x, pdf, 'r-', label="Равномерное U(-√3, √3)")

plt.legend()
plt.xlabel("X")
plt.ylabel("Плотность")
plt.title("Гистограммы выборок и плотность равномерного распределения")
plt.show()