"""
Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

Перечень полок, на которых находятся документы хранится в следующем виде:

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

Задача №1
Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию,
когда пользователь будет пытаться добавить документ на несуществующую полку.
Внимание: p, s, l, a - это пользовательские команды, а не названия функций.
Функции должны иметь выразительное название, передающие её действие.

Задание 2

d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
m – move – команда, которая спросит номер документа и целевую полку и переместит его
с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;
"""

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_human_documents(doc_number):
    """Displaying a person's name on a document"""
    for doc in documents:
        if doc_number == doc['number']:
            return doc['name']


def get_shelf_number(doc_number):
    """Conclusion of a person's shelf on a document"""
    for shelf in directories.items():
        if doc_number in shelf[1]:
            return shelf[0]


def get_list_of_documents():
    """Output of all documents"""
    list_document = []
    for doc in documents:
        val = list(doc.values())
        list_document.append(val)
    return list_document


def get_new_documents_and_shelf(type_d, number_d, owner_name, n_shelf):
    """Adding a new document"""
    new_list = {}
    for shelf in directories.keys():
        if n_shelf in shelf:
            # print(n_shelf)
            new_list.setdefault("type", type_d)
            new_list.setdefault("number", number_d)
            new_list.setdefault("name", owner_name)
            documents.append(new_list)
            directories[n_shelf].append(number_d)
            return documents, directories


def del_document_3(doc_number):
    """deleting a document from the catalog and shelves"""
    for elem in documents:
        if doc_number in elem['number']:
            del (elem['number'])
    for shelf in directories.items():
        if doc_number in shelf[1]:
            shelf[1].remove(doc_number)
            return documents, directories
# print(del_document_3('10006'))

def new_shelf(new_shelf):
    """creating a new shelf"""
    if new_shelf not in directories.keys():
        directories.setdefault(new_shelf, [])
        return directories


def final_block():
    while True:
        user_input = input(
            'Введите команду p,s,l,a,d,as, где '
            'p - выводит имя человека по номеру документа, '
            's - выводит номер полки, на которой лежит запрашиваемый документ, '
            'l - выводит список всех документов в каталоге, '
            'a  - добавляет новый документ в каталог и в перечень полок, '
            'd  - удаляет документ из каталога и с полки, as - добавляет новую полку в перечень полок . '
            'Введите ext для выхода')
        if user_input == "p":
            # например:
            ghd = get_human_documents(input('Введите номер документа'))
            # p = input('Введите номер документа')
            # x = get_human_documents(p)
            if ghd is not None:
                print(ghd)
            else:
                print('Номер документа введен неверно')
        elif user_input == "s":
            gsn = get_shelf_number(input('Введите номер документа'))
            if gsn is not None:
                print(gsn)
            else:
                print('Номер документа введен неверно')
        elif user_input == "l":
            print(get_list_of_documents())
        elif user_input == "a":
            gnwdas = get_new_documents_and_shelf(input('Введите тип документа: '), input('Введите номер документа: '),
                                                 input('Введите имя владельца: '), input('Введите номер полки: '))
            if gnwdas is not None:
                print(gnwdas)
            else:
                print('Указанная полка не найдена')
        elif user_input == "d":
            dd = del_document_3(input('Введите тип документа: '))
            if dd is not None:
                print(dd)
            else:
                print('Номер документа не найден')
        elif user_input == "as":
            ns = new_shelf(input('Введите номер новой полки: '))
            if ns is not None:
                print(ns)
            else:
                print('Данная полка уже существует')
        elif user_input == "ext":
            print('До свидания')
            break


# final_block()