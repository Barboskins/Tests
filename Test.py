"""Задача №1 unit-tests
Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» необходимо
протестировать программу по работе с бухгалтерией Лекции 2.1.
При наличии своего решения данной задачи можно использовать его или использовать предложенный код в
директории scr текущего задания.

Следует протестировать основные функции по получению информации о документах, добавлении и удалении
элементов из словаря.
Рекомендации по тестам.

Если у вас в функциях информация выводилась(print), то теперь её лучше возвращать(return) чтобы можно
было протестировать.
input можно "замокать" с помощью unittest.mock.patch, если с этим будут проблемы,
то лучше переписать функции так, чтобы данные приходили через параметры"""


import requests
import unittest
from bookkeeping import documents,directories,get_human_documents,del_document_3,get_new_documents_and_shelf
from API_REST import TOKEN_YA,create_folder,checking_folder_creation, wrong_create_folder, wrong_checking_folder_creation


# class TestBookkeeping(unittest.TestCase):
#     def setUP(self):
#         pass
#     def tearDown(self):
#         pass
#     def test_number_doc_hum(self):
#         self.assertEqual(get_human_documents('10006'),'Аристарх Павлов')
#     def test_del_doc_number(self):
#         self.assertNotEqual(get_human_documents('10006'), documents,directories)
#     def test_add_new_data(self):
#         self.assertNotEqual(get_new_documents_and_shelf('1','2','3','4'), documents, directories)
#
# if __name__ == '__main__':
#     unittest.main()

"""Задача №2 Автотест API Яндекса
Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой

Пример положительных тестов:
Код ответа соответствует 200.
Результат создания папки - папка появилась в списке файлов."""



class TestAPI(unittest.TestCase):
    def setUP(self):
        pass
    def tearDown(self):
        pass
    def test_create_folder(self):
        self.assertEqual(create_folder(TOKEN_YA),201)
    def test_folder_existence(self):
        self.assertEqual(checking_folder_creation(TOKEN_YA), 200)
    def test_wrong_create_folder(self):
        self.assertEqual(wrong_create_folder(TOKEN_YA),409)
    def test_wrong_checking_folder_creation(self):
        self.assertEqual(wrong_checking_folder_creation(TOKEN_YA),404)



if __name__ == '__main__':
    unittest.main()



