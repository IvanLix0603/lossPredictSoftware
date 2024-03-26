# Идея: Создать продукт на основе искусственной нейронной сети (дальше НС) для определения процентов потерь производительности или потерь во времени вычислительного комплекса(ВК). 

Виды причин возникновения потерь:
1.  промахи в кэше
2.  связность алгоритмов  
3.  влияния системных процессов 
4.  влияния пользовательских процессов

# Краткое описание
Для того чтобы обучить НС необходимо было собрать данные по работе разных ВК (ноутов, компов и т.д.), 
поэтому и был создан данный программный комлекс.

## Состав программного комплекса:
1. big_test - здесь находятся все виды тестов
2. db - база данных с результатами работы программного комплека
3. merge_db - слияние полученной БД с предыдущей
4. visual - визуализация работы тестов и вычисления потерь
5. log - запись логов
6. main.py - программа управления всего комлекса
7. main.scr - скрипт запуска комплекса
8. parse_cpu.py - программа парсинга файла lscpu
9. README.md - файл описания программного комплекса

# ПОДРОБНЕЕ:

## big_test
В данной директории находятся все виды тестов которые используются в программном комплексе.

### Общие признаки дирекстории, содержащиейся в big_test:
- состав каждой директории: 1_test, 2_test, 3_test, 4_test - практически одинаковый, но есть в каждом из них парочка особенностей.
- каждый тест фиксирует время выполнения исполняемого файла mylinpack_64(дальше - "тест") через утилиту time. 
- графики и время выполенения заносятся в соответсвующие папки

### Частные признаки директории, содержащиейся в big_test:
- все тесты работают с количеством элементов до 1200, кроме 2_test, ОСОБЕННОСТЬ-все тесты кроме 2 сначала прогноизуют с 1000 элементов на 1200 и только потом делаюь просчет на 1200.
1_test - общий тест, т.е. не используются какие-либо приблуды.
2_test - тест с разными опциями компилятора.
3_test - с использованием утилиты nice
4_test - использования утилиты yes для создния пользовательского процесса за счет параллельности через модуль thread.


### Принцип работы каждого теста. (см. файлы scr2.sh and scr1.sh)
#### 1_test
a) scr2.sh:
1. в цикле приосходит запуск scr1.sh i, где i - это количестов элементов которое будет считать программа mylinpack_64.
2. запуск питоновского скрипта predict_1200.py
3. копирование результатов в дирикторию /visual/1_test/

b) scr1.sh:
1. на вход скрипта принимается число показывающие число элементов с которыми будет работать тест.
2. создаются папки для хранения результатов
3. инициализируется шаг, с которым будет изменяться колчество элементов
4. компилируется файо mylinpack.
5. цикл for:
            - i - количество элементов с которым будет работать тест
            - с каждом проходом происходит запуск теста с i-ым количеством элементов, при этом замеряется время выполнения работы теста с
            i-ым количеством элементов
            - результат времени записывается в файл tmp_timing 
6. после цикла идет обработка файла tmp_timing с помощью утилиты awk, т. е. вытаскивается время и количество элементов, и распихивается все это по файлам
7. запускается питоновский скрипт отображения результатов.

c) paint_plot.py - предназначен для визуализации результатов теста:
1. на вход принимаются файлы откуда брать результаты(дальше данные)
2. данные извлекаются из файлов и преорбразуются в нужный тип данных.
3. помимо отрисовки графика данных, отрисовывается еще график полиномиальной регрессии(для чего нужна?-это тип теоритческое прогнозирование времени работы теста, оно также производится в разделе visual)
4. сохранение результатов в папке results 

e) predict_1200.py - предназначена для прогнозирование времени работы на 1200 элементов
1. данные извлекаются из файлов и преорбразуются в нужный тип данных.
2. отрисовываются полученные результаты после прогнозировния и сохраниаюься в папку results.

#### 2_test
1. в цикле приосходит запуск scr1.sh i, где i - это количестов элементов которое будет считать программа mylinpack_64.
2. копирование результатов в дирикторию /visual/2_test/

b) scr1.sh:
1. на вход скрипта принимается число показывающие число элементов с которыми будет работать тест.
2. создаются папки для хранения результатов
3. инициализируется шаг, с которым будет изменяться колчество элементов
4. компилируется файо mylinpack.c c разными опциями компилятора.
5. цикл for - запсукаются поочередно три исполняемых файла:
            - i - количество элементов с которым будет работать тест
            - с каждом проходом происходит запуск теста с i-ым количеством элементов, при этом замеряется время выполнения работы теста с
            i-ым количеством элементов
            - результат времени записывается в файл tmp_timing 
6. после цикла идет обработка файлов tmp_timing_О(опция компилятора) с помощью утилиты awk, т. е. вытаскивается время и количество элементов, и распихивается все это по файлам
6. запускается питоновский скрипт отображения результатов.

c) paint_plot.py - предназначен для визуализации результатов теста:
1. на вход принимаются файлы откуда брать результаты(дальше данные)
2. данные извлекаются из файлов и преорбразуются в нужный тип данных.
3. отрисоваются графики работы, с использованием 3 опций.
4. сохранение результатов в папке results 

#### 3_test
Аналогично первому тесту, за исключением того что запуск ./mylinpack происходит с заниженным nice

#### 4_test
Аналогично первому тесту, за исключением того что параллельным образом идет процесс с yes,(по идее нужно чтобы работа теста шла с включенном монитором) запуск ./mylinpack.

## visual
Данная директория предназначена для аппроксимации теоритических значений и представления в виде столбчатой диаграммы потери во времени.

### Состав
1. директории с результатами тестов: 1_test, 2_test, 3_test, 4_test
2. питонвские скрипты визуализации 1_test_hist.py, 2_test_hist.py, 3_test_hist.py, 4_test_hist.py
3. скрипт для реализации полиномиальной регресии: poly.py

На выходе каждого скрипта получается файл: delta_i_test_j.txt, где i=1..4, j=[25, 50, 100, 150, 200, 300, 500, 1000, 1200], после чего этот файл передается в директорию db.

## db
Данная директория предназначена для формирования таблицы с данными, которые впоследствии пойдут на обучении НС.

### load.py 
Этот скрипт и формирует таблицы с данными.
На вход ему подается распарсенный файл lscpu и delta_i_test_j.txt, где i=1..4, j=[25, 50, 100, 150, 200, 300, 500, 1000, 1200]
Этот большой массив записывается в таблицу.
