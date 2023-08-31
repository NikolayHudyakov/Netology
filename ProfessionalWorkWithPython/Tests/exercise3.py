def get_sort_course(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    # С этого момента начинается выполнение задания 2
    # На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете

    # Отсортируйте курсы по длительности (ключ duration), но при этом сохраните порядковый номер каждого курса из courses_list
    # Самое простое — создать новый словарь durations_dict с ключом — duration и значением — исходным номером курса в courses_list
    # Но у нас могут быть курсы с одинаковой длительностью, поэтому значение словаря — это список индексов, а не одно значение
    durations_dict = {}

    # Допишите код цикла так, чтобы в нём вы получали id курса. Подсказка: помните о функции enumerate
    for id, course_dict in enumerate(courses_list):
        key = course_dict["duration"]  # Получите значение из ключа duration
        # Допишите код ниже, который добавляет в словарь durations_dict по ключу key значения — id
        durations_dict[id] = key
    # Отсортируем словарь по ключам. Этот код уже готов, ничего менять не нужно
    # Здесь мы получаем пары ключ-значение в виде кортежа, и функция sorted выполняет сортировку по первым значениям кортежа — ключам

    durations_dict = dict(sorted(durations_dict.items(), key=lambda p: p[1]))
    # Выведите курсы, отсортированные по длительности
    # Допишите код цикла так, чтобы в нём вы получали из durations_dict ключи и значения'
    ret = []
    for key, value in durations_dict.items():
        # Допишите код, который проходит по всему списку значений и выводит на экран текст вида «название курса — длительность»

        ret.append(f'{courses[key]} - {value} месяцев')
    return ret
