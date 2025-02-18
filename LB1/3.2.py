import numpy as np

def calculate_statistics(sample):
    mean = np.mean(sample)
    median = np.median(sample)
    quartile_range = (np.percentile(sample, 75) + np.percentile(sample, 25)) / 2
    variance = np.mean(sample**2) - mean**2  # Оценка дисперсии

    return mean, median, quartile_range, variance

lambda_ = 10  # Параметр распределения Пуассона
sample_sizes = [10, 100, 1000]
num_experiments = 1000

# Храним результаты для каждого размера выборки
results = {size: {"mean": [], "median": [], "quartile_range": [], "variance": []} for size in sample_sizes}

# Генерируем выборки и считаем статистики
for size in sample_sizes:
    for _ in range(num_experiments):
        sample = np.random.poisson(lambda_, size)  # Генерация выборки из Пуассона
        mean, median, quartile_range, variance = calculate_statistics(sample)

        results[size]["mean"].append(mean)
        results[size]["median"].append(median)
        results[size]["quartile_range"].append(quartile_range)
        results[size]["variance"].append(variance)

# Усредняем результаты
final_results = {
    size: {
        "E(z)": np.mean(results[size]["mean"]),
        "Медиана": np.mean(results[size]["median"]),
        "Средний квартильный размах": np.mean(results[size]["quartile_range"]),
        "Оценка дисперсии": np.mean(results[size]["variance"])
    } for size in sample_sizes
}

# Вывод результатов
for size, stats in final_results.items():
    print(f"Размер выборки: {size}")
    for stat_name, stat_value in stats.items():
        print(f"{stat_name}: {stat_value}")
    print()