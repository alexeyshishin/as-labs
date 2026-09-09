#!/usr/bin/env python3
from datetime import datetime

now = datetime.now()

today_date = now.date()
current_time = now.time()

day_of_week = now.weekday()

target_date = datetime(2026, 7, 1)
days_left = (target_date - datetime.combine(today_date, datetime.min.time())).days

print(f"Сегодняшняя дата: {today_date}")
print(f"Текущее время: {current_time}")
print(f"Номер дня недели: {day_of_week}")
print(f"Дней осталось до 1 июля 2026 года: {days_left}")
