# Сначала мы   создадим массив `a` заданного размера и значений, а затем вычислим среднее 
# значение по каждому столбцу (признаку).

# 1. Создание массива `a`.
# 2. Нахождение среднего значения по каждому столбцу с использованием метода `mean`.
# 3. Запись результата в массив `mean_a`.

### Пояснения:
# - `np.array` создаёт массив `a` размером 5x2 с указанными значениями.
# - `np.mean(a, axis=0)` вычисляет среднее значение по каждому столбцу. Аргумент `axis=0` указывает на то, что операция `mean` будет проводиться по столбцам.
# - Результат, массив `mean_a`, содержит средние значения для каждого столбца массива `a`.


import numpy as np

# Создание массива a размером 5x2
a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])

# Нахождение среднего значения по каждому признаку (столбцу)
mean_a = np.mean(a, axis=0)

print("Массив a:")
print(a)
print("\nСреднее значение по каждому признаку (столбцу):")
print(mean_a)

