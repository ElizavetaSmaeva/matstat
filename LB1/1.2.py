import numpy as np


def calculate_statistics(sample):
    mean = np.mean(sample)
    median = np.median(sample)
    quartile_range = (np.percentile(sample, 75) + np.percentile(sample, 25)) / 2
    variance = np.mean(sample**2) - mean**2  # Оценка дисперсии по формуле

    return mean, median, quartile_range, variance

sample_sizes = [10, 100, 1000]
num_experiments = 1000

results = {size: {"mean": [], "median": [], "quartile_range": [], "variance": []} for size in sample_sizes}

# Генерируем выборки и считаем статистики
for size in sample_sizes:
    for _ in range(num_experiments):
        sample = np.random.normal(0, 1, size)  # Генерация выборки
        mean, median, quartile_range, variance = calculate_statistics(sample)

        results[size]["mean"].append(mean)
        results[size]["median"].append(median)
        results[size]["quartile_range"].append(quartile_range)
        results[size]["variance"].append(variance)

# Усредняем результаты
final_results = {
    size: {
        "mean": np.mean(results[size]["mean"]),
        "median": np.mean(results[size]["median"]),
        "quartile_range": np.mean(results[size]["quartile_range"]),
        "variance": np.mean(results[size]["variance"]),
    }
    for size in sample_sizes
}

# Вывод в виде таблицы
import pandas as pd
df = pd.DataFrame(final_results).T
df.columns = ["Среднее", "Медиана", "Средний квартильный размах", "Оценка дисперсии"]
print(df)