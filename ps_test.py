import psycopg2
import random
import time
import threading
from datetime import datetime
import cProfile
import psutil
import string

class PostgreSQLTester:
    """
    Класс для тестирования производительности PostgreSQL.
    """

    def __init__(self, dbname, user, password, host, port):
        """
        Инициализация объекта PostgreSQLTester.

        Параметры:
        - dbname (str): Имя базы данных PostgreSQL.
        - user (str): Имя пользователя PostgreSQL.
        - password (str): Пароль пользователя PostgreSQL.
        - host (str): Хост базы данных PostgreSQL.
        - port (str): Порт базы данных PostgreSQL.
        """
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        # Устанавливаем соединение
        self.conn = self.create_connection()
        if self.conn is not None:
            self.create_table()

    def create_connection(self):
        """
        Создает соединение с базой данных PostgreSQL.

        Возвращает:
        - psycopg2.connection: Объект соединения с базой данных PostgreSQL, если соединение успешно установлено.
        - None: Возвращает None, если произошла ошибка при подключении к базе данных.
        """
        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return conn
        except psycopg2.Error as e:
            print("Ошибка подключения к БД:", e)
            return None

    def create_table(self):
        """
        Создает таблицу в базе данных PostgreSQL, если она не существует.
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            first_number INT NOT NULL,
            second_number INT NOT NULL,
            random_text TEXT
        )
        """
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute("DROP TABLE IF EXISTS test_table")
                    cursor.execute(create_table_query)
            print("Таблица создана.")
        except psycopg2.Error as e:
            print("Ошибка создания таблицы:", e)

    def insert_data(self, num_records):
        """
        Вставляет фейковые данные в базу данных PostgreSQL.

        Параметры:
        - num_records (int): Количество записей, которые нужно вставить.

        Возвращает:
        - None
        """
        if self.conn is not None:
            try:
                with self.conn.cursor() as cursor:
                    for i_rec in range(num_records):
                        first_number = random.randint(1, 1000)
                        second_number = random.randint(1, 1000)
                        random_text = ''.join(random.choices(string.ascii_letters, k=10))  # Рандомный текст из букв
                        print("Вставка данных: first_number =", first_number, ", second_number =", second_number, ", random_text =", random_text)
                        cursor.execute("INSERT INTO test_table (first_number, second_number, random_text) VALUES (%s, %s, %s)",
                                       (first_number, second_number, random_text))
                    self.conn.commit()
            except psycopg2.Error as e:
                print("Ошибка вставки данных в БД:", e)

    def insert_for_duration(self, num_records, duration):
        """
        Выполняет вставку фейковых данных в течение указанной продолжительности.

        Параметры:
        - num_records (int): Количество записей для вставки за одну итерацию.
        - duration (int): Продолжительность вставки данных в секундах.

        Возвращает:
        - None
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            self.insert_data(num_records)
            time.sleep(0.1)  # Опциональная задержка между итерациями вставки

    def measure_performance(self, num_threads, duration):
        """
        Замеряет производительность вставки данных в базу данных PostgreSQL.

        Параметры:
        - num_threads (int): Количество параллельных потоков.
        - duration (int): Продолжительность вставки данных в секундах.

        Возвращает:
        - None
        """
        if self.conn is None:
            print("Невозможно установить соединение с базой данных.")
            return

        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.insert_for_duration, args=(1000, duration // num_threads))
            threads.append(t)

        start_time = datetime.now()

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        end_time = datetime.now()
        total_time = (end_time - start_time).total_seconds()

        print("Затрачено времени в секундах:", total_time)
        print("Производительность в секунду:", (num_threads * 1000 * duration) / total_time)

        cpu_percent = psutil.cpu_percent(interval=1)
        print("Использование процессора в %:", cpu_percent)

        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent
        print("Использование памяти в %:", memory_percent)

        disk_usage = psutil.disk_usage('/')
        print("Использование диска в %:", disk_usage.percent)

if __name__ == "__main__":
    dbname = "ps_test"
    user = "postgres"
    password = "r1gdR1rg"
    host = "localhost"
    port = "5432"

    tester = PostgreSQLTester(dbname, user, password, host, port)

    num_threads = int(input("Введите количество параллельных потоков: "))
    duration = int(input("Введите количество секунд вставки: "))

    cProfile.run('tester.measure_performance(num_threads, duration)')
