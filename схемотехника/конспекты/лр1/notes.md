# Виды дешифраторов

- линейные
- пирамидальные
- матричные
- комбинированные

Все базовые логические элементы строятся на транзисторах

Дешифратор можно построить на ИЛИ-НЕ (или И-НЕ)

EN - enable - вход страбирования

F<sub>j</sub> = EN * M<sub>j</sub>(A<sub>2</sub>, A<sub>1</sub>, A<sub>0</sub>), j = 0..2<sup>n</sup> - 1 = 0..7

Таблицу истинности приводить в отчете, хоть она и очевидна

t<sub>зд.р.ср</sub> - время задержки распространения сигнала (среднее)

> динамическая vs статическая мощность
>
> могут попросить посчитать задержку сигнала в схеме

# В чем проблема линейных дешифраторов?

- конъюнкторы максимум 3 входа (сейчас 4) => большие схемы имеют оч. много каскадов

# Пирамидальный (каскадный) дешифратор

Идея: перемножить x<sub>0</sub> и x<sub>1</sub> и далее в каждом каскаде домножать на x<sub>i</sub>

Проблема: большие задержки

# Ступенчатый (матричный) дешифратор

Количество входов делят на две части пополам, если их нечетно, то на (n+1)/2 и (n-1)/2

Выход = A<sub>i</sub> * B<sub>j</sub>

Быстродействие - второе место после линейного (если схема мала - до 4х16)

# EN(enable) вход стробирования (строб)

- EN - просто включать/выключать дешифратор
- EN позволяет включать/выключать дешифраторы в каскаде при наращивании 
- EN позволяет устранить гонку сигналов

> EC2 - сигнал синхронизации

# Отчет

цель работы скопировать из методы, схемы можно отсканить от руки

# Схемы

4-разрядный счетчик дает комбинации для смены входных значений

D_FF - flip-floap триггер, задерживающий значение на 1 такт

CLK - строб синхронизации

В отчете линии logic analyzer прописать через properties или в paint

Временная диаграмма - 7 сигналов

Если на графике нет задержек - добавить лишние НЕ на линии или в отчете написать что они очень малы и не видны на схеме

Можно начинать со второй схемы

пункт в - схема с анализатором и импульсным генератором

г - амплитуда помех - выбросы на логическом анализаторе

пункт д - потом для EN не ключ, а генератор

е - поставить два курсора

> обязательно убрать помехи

2в - счетчик на 3 триггера и комбинация 2 дешифраторов 2-4 в 3-8 обЪединенных по EN входу

К дешифратору 5-32 из 3-8 один из входа лучше не вешать - или 1 или земля

