import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import cauchy

# Размеры выборок
sample_sizes = [10, 50, 1000]

# Значения X для плотности распределения
x = np.linspace(-10, 10, 1000)
pdf = cauchy.pdf(x, loc=0, scale=1)  # Теоретическая плотность распределения Коши

# Создаём график
plt.figure(figsize=(10, 6))

# Построение гистограмм
for size in sample_sizes:
    sample = np.random.standard_cauchy(size)  # Генерация выборки Коши
    sns.histplot(sample, kde=False, bins=50, label=f"n={size}", stat="density", alpha=0.6)

# Наложение плотности распределения
plt.plot(x, pdf, 'r-', label="Cauchy(0,1) density")

# Подписи осей и легенда
plt.legend()
plt.xlabel("X")
plt.ylabel("Density")
plt.title("Гистограммы выборок и плотность распределения Коши")
plt.xlim(-10, 10)  # Ограничим ось X для лучшей визуализации
plt.show()