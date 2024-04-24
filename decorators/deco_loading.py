"""
Когда Python выполняет декораторы:

Главное свойство декораторов – то, что они выполняются сразу после определе-
ния декорируемой функции. Обычно на этапе импорта (т. е. когда Python загру-
жает модуль)

Смотря что понимать под словом "конструктор".
Метод new() создаёт экземпляр класса, а init() - инициализирует его атрибуты.
В документации Питона init() называют не конструктором, а "специальным методом".
 Процесс конструирования состоит из этих двух методов, поэтому ни new(), ни init() по отдельности не являются конструкторами.
  В принципе можно назвать и то, и другое конструкторами, но это будет не совсем верное определение.

"""

registry = []

def register(func):
    print(f"register decorator is running function {func}")
    registry.append(func)
    return func

@register
def f1():
    print("running f1()")

@register
def f2():
    print("running f2()")

def f3():
    print("running f3()")

def main():
    print("running main()")
    print(f"registry -> {registry}")
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()