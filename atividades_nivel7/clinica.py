# Desafio 17 — Clínica

# Cada paciente:

# nome
# idade
# diagnóstico

# Menu:

# 1 - Cadastrar
# 2 - Buscar paciente
# 3 - Mostrar todos
# 4 - Remover paciente
# 5 - Sair


import os
from pprint import pprint

def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

patients = []

while True:

    option = input('MENU: \n'
    '1 - Register\n'
    '2 - Search for patient\n'
    '3 - Show all\n'
    '4 - Remove patient\n'
    '5 - Exit\n')

    clear_window()
    
    if option not in ['1', '2', '3', '4', '5']:
        print('Invalid option! Try again.')
        continue

    if option == '5':
        print('Exited application...')
        break


    if option == '1':
        name = input('Enter the patient name: ')
        age = input('Enter the patient age: ')
        diagnosis = input('Enter the diagnosis: ')
        patients.append({"name" : name, "age" : age, "diagnosis" : diagnosis})



    if option == '2':
        find_patient = input('Enter the patient name: ')
        for patient in patients:
            if find_patient == patient["name"]:
                print(f'PATIENT: {patient["name"]}\n DIAGNOSIS: {patient["diagnosis"]}')

        if find_patient not in [patient["name"] for patient in patients]:
            print('Patient not found!')

        


    if option == '3':
        print(f'Patients\n')
        for patient in patients:
            print(f'PATIENT: {patient["name"]}\n AGE: {patient["age"]}\n DIAGNOSIS: {patient["diagnosis"]}\n')

    if option == '4':
        remove_patient = input('Enter the patient name to remove: ')
        for patient in patients:
            if remove_patient == patient["name"]:
                patients.remove({"name" : name, "age" : age, "diagnosis" : diagnosis})
        print(f'Patient {remove_patient} removed successfully!')