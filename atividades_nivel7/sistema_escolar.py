# NÍVEL 7 — Desafios completos
# Desafio 16 — Sistema escolar

# Cada aluno:

# nome
# nota1
# nota2

# Menu:

# 1 - Cadastrar aluno
# 2 - Ver boletim
# 3 - Ver aprovados
# 4 - Ver reprovados
# 5 - Mostrar média da turma
# 6 - Sair


import os 
from pprint import pprint

def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')


students = []

while True:

    option = input('Menu:\n'

    '1 - Register student\n'
    '2 - Show report card\n'
    '3 - Show approved\n'
    '4 - Show filed\n'
    '5 - Show class average\n'
    '6 - Exit\n'
    '7 - show all students\n')


    clear_window()

    if option not in ['1', '2', '3', '4', '5', '6', '7']:
        print('Invalid option! Try again.')
        continue

    if option == '6':
        print('Exited application\n')
        break 
    
    if option == '1':
        name = input('Enter student name: \n')
        first = float(input('Enter first note: \n'))
        second = float(input('Enter second note: \n'))
        students.append({"name" : name, "first" : first, "second" : second})
        print(f'Student {name} registered successfully\n')

    if option == '2':
        while True:
            find_student = input('Enter student name to show report card: \n')
            for student in students:
                if find_student == student["name"]:
                    print(f'Student: {student["name"]}\n'
                    f'first note: {student["first"]}\n'
                    f'second note: {student["second"]}\n')
            if find_student not in [student["name"] for student in students]:
                print('Student not found! Try again.\n')

            option = input('Enter for continue or 2 - Back to menu\n')    
            if option == '2':
                break


    if option =='3':
        for student in students:
            average = (student["first"] + student["second"])/2
            if average > 7:
                print(f'APPROVED\n'
                f'Student: {student["name"]}. Average: {average}\n')

    if option == '4':
        for student in students:
            average = (student["first"] + student["second"])/2
            if average < 7:
                print(f'REPROVED\n'
                f'Student: {student["name"]}. Average: {average}\n')



    if option == '5': 
        all_average = 0
        class_average = 0
        for student in students:
            student_average = (student["first"] + student["second"])/2
            all_average += student_average
        class_average = all_average / len(students)
        print('AVERAGE CLASS: '
              f'{class_average:.2f}\n')
        
        

    if option == '7':
        for student in students:
            pprint(f'STUDENT: {student["name"] }'
            f' FIRST NOTE: {student["first"] }'
            f' SECOND NOTE: {student["second"]}')
        
        print(f'{len(students)} students registered\n')














