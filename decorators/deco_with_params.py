"""
Декораторы функций - это простой способ модификации поведения любой функции без внесения изменения в ее код.
 Они часто лежат в основе многих библиотек и вы наверняка с ними знакомы,
 даже если и никогда не писали (привет FastAPI, Flask и миллионы других).

Декораторы позволяют вам выполнить произвольный код до/после/вместо вызова функции,
 модифицируя ее входные аргументы, результат выполнения и добавляя различные сайд-эффекты.
"""
import time


def decorator(call):
    def wrapper(*args, **kwargs):
        r = call(*args, **kwargs)
        return r
    return wrapper


def call(a: int) -> str:
    return str(a)


# В другом виде можно представить как
decorated_call = decorator(call)

# вызов как обычную функцию
assert decorated_call(1) == "1"
assert decorator(call)(1) == "1"

# Следует всегда декорировать ваш wrapper с помощью functools.wraps.
# Эта функция копирует всю служебную метаинформацию о декорируемой функции в функцию-декоратор
# (название функции, докстринги, список входящих аргументов, их типы и тд).

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# для примера покажем как это выглядит без сахара

# обычный декоратор
# decorated_func = decorator(call)

# декоратор с параметрами
# decorator_wrapper = decorator(arg1, arg2)
# decorated_func = decorator_wrapper(call)

# или в одну строчку
# decorated_func = decorator(arg1, arg2)(call)
##############################################


# Декоратора с параметрами
def decorator_wrapper(arg1, arg2):
    def real_decorator(func):     # декоратор в этом случае замыкание, имеет доступ в любом уровне вложенности.
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return real_decorator

@decorator_wrapper(1,2)
def func():
    ...

"""
Еще одно важное уточнение: 
процесс декорирования происходит на этапе первого прохождения интерпретатором Python вашего кода
 (когда Python получает представление об объектах, которыми он может оперировать в рантайме).

Т.е. в самом рантайме (процесс вызова функции) во всех сценариях декорирования будет выполнен только код, 
находящийся внутри wrapper'а.

Сам же код декоратора будет выполнен сразу при старте вашего приложения, 
как только интерпретатор дойдет до строки @decorator.
 Именно поэтому все декораторы должны быть объявлены как синхронные функции. 
 Даже если они являются декораторами для асинхронных функций
(в таком случае асинхронным будет объявлен wrapper).
"""

# Напиши декоратор, который производит замер времени, но замер можно не производить.
def clocked(active=False):  # decorator wrapper
    print("clocked loaded")

    def real_deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"inside wrapper, clocked: {active}")

            if active:
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter() - start
                print(f"clocked done, time is {end}")
            else:
                result = func(*args, **kwargs)

            print("wrapper is done")
            return result
        return wrapper
    return real_deco

@clocked(True)
def myfunc():
    print("start myfunc")
    time.sleep(1.0)
    print("done myfunc")

# myfunc()


#################################
# для реализации декоратора который может принимать аргументы, а может и не принимать,
# нужно сначала написать обычный декоратор,
# а затем написать для него обёртку, получится 4 уровня сложности.
def schrodinger_decorator(
        call=None,
        *,
        active=True,
):
    wrap_decorator = clocked(active)

    # если использовали декоратор как декоратор с параметрами
    if call is None:
        return wrap_decorator

    else:
        return wrap_decorator(call)

@schrodinger_decorator
def my_substractor(num1, num2):
    result = num1 - num2
    print(f"{result = }")


@schrodinger_decorator(active=False)
def my_substractor(num1, num2):
    result = num1 - num2
    print(f"{result = }")


my_substractor(10, 5)