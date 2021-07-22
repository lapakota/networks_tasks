# Трассировка автономных систем

Запуск:
    python tracer_as.py,
    после ввести имя или ip адрес (87.240.190.67 либо vk.com)
    
Результат:
    Во время работы программы выводятся ip адреса, полученные
    через tracert. 
    В конце выводится подобная таблица:

    +--------+----------------+---------+-----------+-----------------+
    | number |       ip       | country | AS number |     provider    |
    +--------+----------------+---------+-----------+-----------------+
    |   1.   |  192.168.0.1   |    *    |     *     |        *        |
    |   2.   | 212.220.30.188 |    RU   |   12389   | PJSC Rostelecom |
    |   3.   | 87.226.146.236 |    RU   |   12389   | PJSC Rostelecom |
    |   4.   |  188.254.2.2   |    RU   |   12389   | PJSC Rostelecom |
    |   5.   | 188.254.10.86  |    RU   |   12389   | PJSC Rostelecom |
    |   6.   | 87.240.190.67  |    RU   |   47541   |  VKontakte Ltd  |
    +--------+----------------+---------+-----------+-----------------+