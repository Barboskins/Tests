import requests
from pprint import pprint
TOKEN_YA = 'УКАЗАТЬ ТОКЕН'

def create_folder(token):
    HEADERS = {"Authorization": f"OAuth {token}"}
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                            params={"path": '/test_folder'},
                            headers=HEADERS
                            )
    return response.status_code



def checking_folder_creation(token):
    HEADERS = {"Authorization": f"OAuth {token}"}
    resp = requests.patch('https://cloud-api.yandex.net/v1/disk/resources',
                            params={"path": '/test_folder'},
                            headers=HEADERS
                            )
    return resp.status_code

def wrong_create_folder(token):
    HEADERS = {"Authorization": f"OAuth {token}"}
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                            params={"path": '/'},
                            headers=HEADERS
                            )
    return response.status_code



def wrong_checking_folder_creation(token):
    HEADERS = {"Authorization": f"OAuth {token}"}
    resp = requests.patch('https://cloud-api.yandex.net/v1/disk/resources',
                            params={"path": '/какая-то папка'},
                            headers=HEADERS
                            )
    return resp.status_code

# pprint(create_folder(TOKEN_YA))
# pprint(checking_folder_creation(TOKEN_YA))
# pprint(wrong_create_folder(TOKEN_YA))
# pprint(wrong_checking_folder_creation(TOKEN_YA))