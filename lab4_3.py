import time  # Импорт модуля time для работы с временем.
from datetime import datetime  # Импорт класса datetime из модуля datetime.

# Цикл, который будет выполняться 5 раз.
for _ in range(5):
    current_time = datetime.now()  # Получаем текущее время.
    print(f"Текущее время: {current_time.strftime('%H:%M:%S')}")  # Выводим текущее время.
    time.sleep(1)  # Приостанавливаем выполнение программы на 1 секунду.