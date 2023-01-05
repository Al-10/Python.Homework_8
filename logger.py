# Модуль для записи резуьтатов вычислений
import csv


def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('result.csv', 'a') as data:
        data.write(f'{str(expr)} => {str(result)}\n')


def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    with open('result.csv', 'r') as data:
        return data.read()