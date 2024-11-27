# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Сортируем студентов для соответствия с оценками
sorted_students = sorted(students)
# Проверяем соответствие между именами студентов и списком оценок
if len(grades) != len(sorted_students):
    print("Количество студентов и оценок не совпадает.")
else:
    # Создаем словарь с именем студента и его средним баллом
    average_grades = {}
    for i, student in enumerate(sorted_students):
        average_grades[student] = sum(grades[i]) / len(grades[i])

    # Вывод результата
    print(average_grades)