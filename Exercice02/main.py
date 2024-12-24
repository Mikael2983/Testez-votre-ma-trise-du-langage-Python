students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

name = input("Entrez le nom de l’étudiant :")

if name in students:
    print(f"Notes de {name} : ")
    Somme_notes = 0
    for subject in students[name]:
        print(f"{subject}: {students[name][subject]}")
        Somme_notes += int(students[name][subject])
    print(f"Moyenne de {name} : {Somme_notes / len(students[name])}")
else:
    print(f"L'étudiant {name} n'existe pas dans la liste.")
