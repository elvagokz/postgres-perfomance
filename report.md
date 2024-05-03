## Вывод результатов теста

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

## Отчёт

Из предоставленного отчета можно сделать следующие выводы:

    1. Производительность в секунду: 600.422249: Программа достигла производительности вставки примерно 8993 записей в секунду.

    2. Использование процессора в %: 12.8: Это довольно низкое значение, что может означать, что программа не является CPU-интенсивной.

    3. Использование памяти в %: 45.8: Это умеренное значение, что может указывать на то, что программа использует средние объемы оперативной памяти.

    4. Использование диска в %: 83.4: Это довольно высокое значение, что может указывать на интенсивное использование дискового ввода/вывода при вставке данных в базу.

    Профилирование кода: 

    1. Общее количество вызовов функций: 293.

    2. Файл ps_test.py вызывает 119 раз функцию measure_performance.

    3. Самая длительная функция - threading.py:979(join), вызвана 3 раза и занимает 600.422 секунды.

Исходя из этих данных, можно сделать вывод о том, что программа вставляет данные в базу данных с достаточно высокой производительностью, при этом не сильно нагружая процессор и используя умеренное количество памяти. Однако интенсивное использование диска может быть узким местом в работе программы.

## Предложения

Рекомендации для оптимальной конфигурации PostgreSQL:

    Память (RAM):
        Выделение достаточного количество оперативной памяти для PostgreSQL, 25-40% от общего объема памяти сервера.
        Важно настроить параметры shared_buffers(25% от доступной памяти) и work_mem(1-2 MB на активного пользователя) в зависимости от доступной памяти.

    Жесткий диск:
        Использование SSD для ускорения чтения и записи данных.
        Разделение данных, журналов и временных файлов на разные диски.

    Процессор:
        Использование многоядерных процессоров для улучшения производительности.
        Для этого настройте параметры max_connections и max_worker_processes в зависимости от количества одновременных подключений и нагрузки на сервер.

    Конфигурационные параметры PostgreSQL:
        Настройка параметров effective_cache_size и random_page_cost для лучшего использования кэша и оптимизации запросов.
        Параметр checkpoint_segments для управления частотой записи в журнал.
        Параметр autovacuum для автоматического очищения и анализа таблиц для предотвращения фрагментации данных.

    Безопасность:
        Нежелательно использование логин postgres, лучше создать отдельного пользователя с необходимыми привилегиями.
        Настройка SSL-шифрование для безопасного обмена данными между сервером и клиентами.