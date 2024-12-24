class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"{self.title}, de {self.author}, paru en {self.year}"


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        removed_book = False
        borrowed_book = False

        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                removed_book = True
                break

        if removed_book:
            print(f"le livre {book_title} est été supprimé")
        else:
            for book in self.borrow_books:
                if book.title == book_title:
                    borrowed_book = True
                    break

            if borrowed_book:
                print(
                    f"le livre {book_title} a été emprunté, attendez son retour")
            else:
                print(
                    f"le livre {book_title} n'est pas référencé dans la bibliothèque")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)
                print(f"le livre {book} a été emprunté")
                break

    def return_book(self, book_title):
        returned_book = False
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)
                returned_book = True
                break
        if returned_book:
            print(f"le livre {book_title} a été restitué")
        else:
            print(f"le livre {book_title} n'est pas référencé dans la bibliothèque")

    def available_books(self):
        print("liste des livres disponibles")
        for book in self.books:
            print(book)

    def borrowed_books(self):
        print("liste des livres empruntés")
        for book in self.borrow_books:
            print(book)


books = [
    ["Les Misérables", "Victor Hugo", 1862],
    ["Notre-Dame de Paris", "Victor Hugo", 1831],
    ["Les Contemplations", "Victor Hugo", 1856],
    ["Madame Bovary", "Gustave Flaubert", 1857],
    ["Les Fleurs du mal", "Charles Baudelaire", 1857],
    ["Germinal", "Émile Zola", 1885],
    ["Le Rouge et le Noir", "Stendhal", 1830],
    ["La Chartreuse de Parme", "Stendhal", 1839],
    ["À la recherche du temps perdu", "Marcel Proust", 1913],
    ["Du côté de chez Swann", "Marcel Proust", 1913],
    ["Le Grand Meaulnes", "Alain-Fournier", 1913],
    ["Les Croix de bois", "Roland Dorgelès", 1919],
    ["Voyage au bout de la nuit", "Louis-Ferdinand Céline", 1932],
    ["L'Étranger", "Albert Camus", 1942],
    ["La Peste", "Albert Camus", 1947],
    ["Huis clos", "Jean-Paul Sartre", 1944],
    ["Le Deuxième Sexe", "Simone de Beauvoir", 1949],
    ["La Modification", "Michel Butor", 1957],
    ["Bonjour tristesse", "Françoise Sagan", 1954],
    ["L'Amant", "Marguerite Duras", 1984],
    ["En attendant Godot", "Samuel Beckett", 1952],
    ["Les Particules élémentaires", "Michel Houellebecq", 1998],
    ["Soumission", "Michel Houellebecq", 2015],
    ["Chanson douce", "Leïla Slimani", 2016],
    ["L'Énigme du retour", "Dany Laferrière", 2009],
    ["Au revoir là-haut", "Pierre Lemaitre", 2013],
    ["La Vérité sur l'affaire Harry Quebert", "Joël Dicker", 2012],
    ["L'Anomalie", "Hervé Le Tellier", 2020],
    ["Sérotonine", "Michel Houellebecq", 2019],
    ["L'Art de perdre", "Alice Zeniter", 2017],
    ["Les Loyautés", "Delphine de Vigan", 2018],
    ["Rien ne s'oppose à la nuit", "Delphine de Vigan", 2011],
    ["1984", "George Orwell", 1949],
    ["Le Meilleur des mondes", "Aldous Huxley", 1932],
    ["Le Vieil Homme et la Mer", "Ernest Hemingway", 1952],
    ["Les Cerfs-volants de Kaboul", "Khaled Hosseini", 2003],
    ["La Bibliothèque de minuit", "Matt Haig", 2020],
    ["Le Sympathisant", "Viet Thanh Nguyen", 2015],
    ["Shantaram", "Gregory David Roberts", 2003],
    ["Kafka sur le rivage", "Haruki Murakami", 2002],
    ["La Ballade de l'impossible", "Haruki Murakami", 1987]
]

librairy = Library()

for reference in books:
    livre = Book(reference[0], reference[1], reference[2])
    librairy.add_book(livre)

librairy.borrow_book("La Modification")
librairy.borrow_book("Les Fleurs du mal")
librairy.remove_book("Les Fleurs du mal")
librairy.remove_book("Mortelle Adèle, Tome 01: Tout ça finira mal")
librairy.return_book("Les Fleurs du mal")
librairy.return_book("Mortelle Adèle, Tome 01: Tout ça finira mal")
librairy.remove_book("Les Fleurs du mal")
librairy.borrow_book("Chanson douce")
librairy.borrow_book("Les Croix de bois")
librairy.borrow_book("Notre-Dame de Paris")
librairy.available_books()
librairy.borrowed_books()
