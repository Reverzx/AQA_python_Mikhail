import re
import statistics
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def create_students_file():
    try:
        with open("students.txt", "x", encoding="utf-8") as file:
            file.write("name: Mikhail Zakhodin, group: A-101, grades: [5, 4, 3] \n")
            file.write("name: Ivan Ivanov, group: A-101, grades: [4, 4, 5] \n")
            file.write("name: Angelina Borisova, group: A-102, grades: [5, 5, 5] \n")
            file.write("name: Kolesnikov Artur, group: A-102, grades: [3, 3, 3] \n")
            file.write("name: Gimli Gloin, group: A-103, grades: [4, 3, 3] \n")
            file.write("name: Legolas Thranduil, group: A-103, grades: [5, 3, 5] \n")
            file.write("name: Loren Thor, group: A-103, grades: [5, 5, 5] \n")
    except FileExistsError:
        logging.warning("Файл уже существует!")


def read_student_file():
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            file_str = file.read()
        pattern = r"name: (.*?), group: (.*?), grades: \[(.*?)\]"
        count_student = 0
        students = {}
        avg_score: float
        all_students = 0
        for i in (re.findall(pattern, file_str)):
            if i[1] not in students:
                count_student = 1
                avg_score = statistics.mean(list(map(float, i[2].split(", "))))
                students[i[1]] = {
                    "count_student": count_student,
                    "avg_score": round(avg_score / count_student, 2)
                }
            else:
                count_student += 1
                avg_score += statistics.mean(list(map(float, i[2].split(", "))))
                students[i[1]] = {
                    "count_student": count_student,
                    "avg_score": round(avg_score / count_student, 2)
                }
            all_students += 1
        logging.info(students)
        logging.info(f"Общее количество студентов {all_students}")
        return students, all_students
    except FileNotFoundError:
        logging.critical("Невозможно прочитать файл")


def write_to_file(students, all_students):
    try:
        with open("students.txt", "a", encoding="utf-8") as file:
            file.write("\n Статистика студентов: \n")
            file.write(f"Общее количество студентов: {all_students} \n")
            for i, s in students.items():
                logging.info((f"В группе {i} учится {s['count_student']} студентов. "
                              f"Их средняя оценка: {s['avg_score']}"))
                file.write(f"В группе {i} учится {s['count_student']} студентов. "
                           f"Их средняя оценка: {s['avg_score']} \n")
    except FileExistsError:
        logging.critical("Невозможно прочитать файл")


def main():
    create_students_file()
    students, all_students = read_student_file()
    write_to_file(students, all_students)


main()
