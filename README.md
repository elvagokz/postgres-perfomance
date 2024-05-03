## Подготовка к тесту

Для запуска убедитесь, что у вас установлен postgresql версии не ниже 16, python и psycopg2
последний вы можете установить при помощи команды

```bash
pip install psycopg2
```
Создайте базу данных с помощью команды:


```bash
psql -U postgres -c "CREATE DATABASE new_db;"
```

## Запуск теста

В скрипте ***ps_test.py*** поменяйте значения на свои

```python
if name == "main":
dbname = "имя вашей базы данных"
user = "пользователь postgresql"
password = "пароль от postgresql"
host = "адрес сервера с БД"
port = "5432"
```
После этого запустите скрипт командой:

```bash
python ps_test.py
```

Следуя подсказкам введете количество одновременных потоков и время в секундах для вставки данных.
После этого запустится скрипт вставки данных на заданное Вами время, после чего
Вы получите отчёт о статистике проведённой операции в виде:

```
Затрачено времени в секундах: 600.422249
Производительность в секунду: 8993.6707192208
Использование процессора в %: 12.8
Использование памяти в %: 45.8
Использование диска в %: 83.4
         293 function calls in 601.424 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  601.424  601.424 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        2    0.000    0.000    0.000    0.000 __init__.py:1683(cpu_times)
        2    0.000    0.000    0.000    0.000 __init__.py:1724(_cpu_tot_time)
        1    0.000    0.000    0.000    0.000 __init__.py:1743(_cpu_busy_time)
        1    0.000    0.000    0.000    0.000 __init__.py:1759(_cpu_times_deltas)
        1    0.000    0.000    1.001    1.001 __init__.py:1780(cpu_percent)
        1    0.000    0.000    0.000    0.000 __init__.py:1821(calculate)
        1    0.000    0.000    0.000    0.000 __init__.py:1998(virtual_memory)
        1    0.000    0.000    0.000    0.000 __init__.py:2078(disk_usage)
        2    0.000    0.000    0.000    0.000 _common.py:267(usage_percent)
        2    0.000    0.000    0.000    0.000 _common.py:293(wrapper)
        3    0.000    0.000    0.000    0.000 _common.py:585(open_binary)
        3    0.000    0.000    0.000    0.000 _pslinux.py:219(get_procfs_path)
        1    0.000    0.000    0.000    0.000 _pslinux.py:383(virtual_memory)
        2    0.000    0.000    0.000    0.000 _pslinux.py:563(cpu_times)
        2    0.000    0.000    0.000    0.000 _pslinux.py:575(<listcomp>)
        1    0.000    0.000    0.000    0.000 _psposix.py:123(disk_usage)
        3    0.000    0.000    0.000    0.000 _weakrefset.py:38(_remove)
        3    0.000    0.000    0.000    0.000 _weakrefset.py:81(add)
        1    0.000    0.000  601.424  601.424 ps_test.py:119(measure_performance)
        3    0.000    0.000  600.422  200.141 threading.py:1017(_wait_for_tstate_lock)
        6    0.000    0.000    0.000    0.000 threading.py:1095(daemon)
        3    0.000    0.000    0.000    0.000 threading.py:1177(_make_invoke_excepthook)
        6    0.000    0.000    0.000    0.000 threading.py:1306(current_thread)
        3    0.000    0.000    0.000    0.000 threading.py:222(__init__)
        3    0.000    0.000    0.000    0.000 threading.py:246(__enter__)
        3    0.000    0.000    0.000    0.000 threading.py:249(__exit__)
        3    0.000    0.000    0.000    0.000 threading.py:255(_release_save)
        3    0.000    0.000    0.000    0.000 threading.py:258(_acquire_restore)
        3    0.000    0.000    0.000    0.000 threading.py:261(_is_owned)
        3    0.000    0.000    0.000    0.000 threading.py:270(wait)
        3    0.000    0.000    0.000    0.000 threading.py:505(__init__)
        6    0.000    0.000    0.000    0.000 threading.py:513(is_set)
        3    0.000    0.000    0.000    0.000 threading.py:540(wait)
        3    0.000    0.000    0.000    0.000 threading.py:734(_newname)
        3    0.000    0.000    0.000    0.000 threading.py:761(__init__)
        3    0.000    0.000    0.001    0.000 threading.py:834(start)
        3    0.000    0.000    0.000    0.000 threading.py:944(_stop)
        3    0.000    0.000  600.422  200.141 threading.py:979(join)
        5    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x902780}
        6    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        6    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        3    0.000    0.000    0.000    0.000 {built-in method _thread.start_new_thread}
        1    0.000    0.000  601.424  601.424 {built-in method builtins.exec}
       25    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.round}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        3    0.000    0.000    0.000    0.000 {built-in method io.open}
        2    0.000    0.000    0.000    0.000 {built-in method now}
        1    0.000    0.000    0.000    0.000 {built-in method posix.statvfs}
        1    1.000    1.000    1.000    1.000 {built-in method time.sleep}
        3    0.000    0.000    0.000    0.000 {method '__enter__' of '_thread.lock' objects}
        3    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
       15  600.422   40.028  600.422   40.028 {method 'acquire' of '_thread.lock' objects}
        3    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        3    0.000    0.000    0.000    0.000 {method 'append' of 'collections.deque' objects}
       13    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        6    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {method 'locked' of '_thread.lock' objects}
        2    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        6    0.000    0.000    0.000    0.000 {method 'release' of '_thread.lock' objects}
       53    0.000    0.000    0.000    0.000 {method 'split' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'total_seconds' of 'datetime.timedelta' objects}

```
Где вы сможете оценить метрики сервера при выполнение вставки а так же показатели профилирования. Вы всегда можете добавить интересующие Вас метрики 
в функцию ***def measure_performance***

Из предоставленного отчета можно сделать следующие выводы:

    Производительность в секунду: 8996.786138066473: Программа достигла производительности вставки примерно 8996 записей в секунду. Это означает, что база данных обрабатывает примерно 8996 записей в секунду.

    Использование процессора в %: 2.3: Загрузка процессора составила около 2.3%. Это довольно низкое значение, что может означать, что программа не является CPU-интенсивной.

    Использование памяти в %: 58.9: Использование памяти составило около 58.9%. Это умеренное значение, что может указывать на то, что программа использует средние объемы оперативной памяти.

    Использование диска в %: 83.0: Использование диска составило около 83.0%. Это довольно высокое значение, что может указывать на интенсивное использование дискового ввода/вывода при вставке данных в базу.

    Профилирование кода: В отчете профилировщика видно, что большая часть времени программы затрачивается на ожидание завершения потоков в функции threading.py:979(join). Это ожидание завершения работы потоков.

    Малая доля времени на выполнение кода: Функция measure_performance занимает всего 200.071 секунды из общего времени выполнения в 600.214 секунд.

Исходя из этих данных, можно сделать вывод о том, что программа вставляет данные в базу данных с достаточно высокой производительностью, при этом не сильно нагружая процессор и используя умеренное количество памяти. Однако интенсивное использование диска может быть узким местом в работе программы.
