# Модуль для выполнения опреаций
import sympy


def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    """"Принимает на вход строку-пример.
    Возвращает результат примера."""
    return sympy.simplify(expr)


def solve_eq(expr: str) -> str:                    # x**3 - 8 = 0 -> "2"
    # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    expr1 = ''
    for i in expr:
        if i != '0' and i != '=':
            expr1 += i
    x = sympy.Symbol('x')
    return sympy.solve(expr1, x)


def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """"Упрощает введенный многочлен"""
    return sympy.simplify(expr)