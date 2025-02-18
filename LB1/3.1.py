import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import poisson

# Устанавливаем параметр распределения Пуассона
lambda_ = 10
sample_sizes = [10, 50, 1000]

# Создаем график
plt.figure(figsize=(10, 6))

# Границы X для теоретического распределения
x = np.arange(0, 25)
pmf = poisson.pmf(x, mu=lambda_)  # Функция вероятности Пуассона

# Генерируем выборки и строим гистограммы
for size in sample_sizes:
    sample = np.random.poisson(lambda_, size)
    sns.histplot(sample, bins=range(25), kde=False, stat="density", alpha=0.6, label=f"n={size}")

# Добавляем теоретическое распределение
plt.plot(x, pmf, 'ro-', markersize=5, label="Poisson PMF (λ=10)")

plt.legend()
plt.xlabel("X")
plt.ylabel("Density")
plt.title("Гистограммы выборок и плотность распределения Пуассона")
plt.grid()
plt.show()