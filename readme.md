# Тестовое задание для Lesta Studio (St.Petersburg).

<details><summary> Задание #1</summary>

На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен
нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.
```Python
    # Python example:
        def isEven(value): return value%2==0
```
</details>

[Код моей реализации.](https://github.com/MrFedko/Lesta_studio/blob/986ed53eb4bf5be5ee33db4915855df5cf586542/test_one/my_code.py)
```Python
def my_is_even(value: int) -> bool: return value & 1 == 0
```

Побитовые операции в языках программирования играют фундаментальную роль при работе с множеством приложений.

С помощью побитового оператора & можно проверить, является ли число четным или нечетным. Для целых чисел, если младший бит равен 1, то число нечетное (основываясь на преобразовании двоичных чисел в десятичные). 
Зачем это нужно, если можно просто использовать %2? На моем компьютере, например, &1 выполняется на 66% 
Чтобы это проверить, в точку входа ([main](https://github.com/MrFedko/Lesta_studio/blob/986ed53eb4bf5be5ee33db4915855df5cf586542/test_one/main.py)) я вшил сравнение результата выполнения проверки с помощью взятия остатка от деления и побитового &.


<details><summary>Задание #2</summary>

На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы
каждой реализации.

</details>


<details><summary>Задание #3</summary>

На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы
считаете, что функция соответствует заданным критериям.

</details>
