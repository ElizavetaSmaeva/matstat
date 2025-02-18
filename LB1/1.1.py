import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Задаем размеры выборок
sample_sizes = [10, 50, 1000]

# Создаём график
plt.figure(figsize=(10, 6))

# Границы оси X
x = np.linspace(-4, 4, 1000)
pdf = norm.pdf(x, loc=0, scale=1)  # Плотность нормального распределения

# Генерация и построение выборок
for size in sample_sizes:
    sample = np.random.normal(0, 1, size)
    sns.histplot(sample, kde=False, bins=20, label=f"n={size}", stat="density", alpha=0.6)

# Наложение графика плотности
plt.plot(x, pdf, 'r-', label="N(0,1) density")

plt.legend()
plt.xlabel("X")
plt.ylabel("Density")
plt.title("Гистограммы выборок и плотность нормального распределения")
plt.show()