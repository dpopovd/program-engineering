results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1,
           30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

# Три лучшие и три худшие результаты
best_results = sorted(results)[:3]
bad_results = sorted(results)[-3:]

# Результаты начиная с 10
results_ot_10 = [result for result in results if result >= 10]

print("Три лучшие результаты:", best_results)
print("Три худшие результаты:", bad_results)
print("Результаты начиная с 10:", results_ot_10)