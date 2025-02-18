import numpy as np


def calculate_statistics(sample):
    mean = np.mean(sample)  # Среднее (нестабильное для Коши!)
    median = np.median(sample)  # Медиана - более надёжная характеристика
    q1, q3 = np.percentile(sample, [25, 75])
    quartile_range = (q1 + q3) / 2  # Средний квартильный размах
    variance = np.mean(sample**2) - mean**2  # Оценка дисперсии

    return mean, median, quartile_range, variance

# Размеры выборок
sample_sizes = [10, 100, 1000]
num_experiments = 1000

# Словарь для хранения результатов
results = {size: {"mean": [], "median": [], "quartile_range": [], "variance": []} for size in sample_sizes}

# Генерация выборок и вычисление статистик
for size in sample_sizes:
    for _ in range(num_experiments):
        sample = np.random.standard_cauchy(size)  # Генерация выборки Коши
        mean, median, quartile_range, variance = calculate_statistics(sample)

        results[size]["mean"].append(mean)
        results[size]["median"].append(median)
        results[size]["quartile_range"].append(quartile_range)
        results[size]["variance"].append(variance)

# Упаковка результатов в массивы
summary_statistics = {size: {key: np.mean(value) for key, value in results[size].items()} for size in sample_sizes}

# Вывод результатов
for size, stats in summary_statistics.items():
    print(f"Результаты для выборки n={size}:")
    print(f" Среднее: {stats['mean']:.2f}")
    print(f" Медиана: {stats['median']:.2f}")
    print(f" Средний квартильный размах: {stats['quartile_range']:.2f}")
    print(f" Оценка дисперсии: {stats['variance']:.2f}\n")