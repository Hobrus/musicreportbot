# Используйте официальный образ Python
FROM python:3.11-slim

# Установите рабочую директорию
WORKDIR /app

# Установите зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте остальной код
COPY src/ .

# Запустите бота при старте контейнера
CMD ["python", "bot.py"]
