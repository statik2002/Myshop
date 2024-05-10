import asyncio
import datetime
from http.client import BAD_REQUEST
import logging
from logging.handlers import RotatingFileHandler
from pprint import pprint
from smb.SMBConnection import SMBConnection

import requests
from environs import Env


async def get_token(login: str, password: str, debug: bool):
    if debug:
        url = 'http://127.0.0.1:8000/api/v1/token/login/'
    else:
        url = 'https://neit.ru/api/token/'

    header = {
        'phone_number': login,
        'password': password
    }

    response = requests.post(url, json=header)
    response.raise_for_status()

    token = response.json()['access']
    return token


async def get_all_products_from_server(token, debug):
    if debug:
        url_send_shift = f'http://127.0.0.1:8000/api/v1/products/'
    else:
        url_send_shift = f'https://neit.ru/api/v1/goods/'
    header = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url_send_shift, headers=header, timeout=500)
    response.raise_for_status()

    print(response.json())

    return response.json()


async def get_product_by_id(token, product_id: int, debug: bool = True):
    if debug:
        url_send_shift = f'http://127.0.0.1:8000/api/v1/products/{product_id}/get_product/'
    else:
        url_send_shift = f'https://neit.ru/api/v1/update_products/'
    header = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url_send_shift, headers=header, timeout=500)
    response.raise_for_status()

    return response.json()


async def get_product_by_id_public(product_id: int, debug: bool = True):
    if debug:
        url_send_shift = f'http://127.0.0.1:8000/api/v1/products/{product_id}/'
    else:
        url_send_shift = f'https://neit.ru/api/v1/update_products/'

    response = requests.get(url_send_shift, timeout=500)
    response.raise_for_status()
    print(response)

    return response.json()


async def initial_catalogs_upload(token, catalogs, debug):
    if debug:
        url_send_shift = f'http://127.0.0.1:8000/api/v1/initial_upload_catalog/'
    else:
        url_send_shift = f'https://neit.ru/api/v1/catalogs/'
    header = {
        'Authorization': f'Bearer {token}'
    }

    data = catalogs

    response = requests.post(url_send_shift, headers=header, json=data)
    response.raise_for_status()

    return response.json()


async def initial_upload_products(token, products, debug):
    if debug:
        url_send_shift = f'http://127.0.0.1:8000/api/v1/initial_upload_products/'
    else:
        url_send_shift = f'https://neit.ru/api/v1/update_products/'
    header = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.post(url_send_shift, headers=header, json=products, timeout=600)
    response.raise_for_status()

    return response.json()


async def fetch_file(path, shared_folder, username, password, remote_name, filepath, port=455, my_name='server'):
    conn = SMBConnection(username=username, my_name=my_name, password=password, remote_name=remote_name,
                         is_direct_tcp=True)
    try:
        conn.connect(remote_name, port)

        with open(filepath, 'wb') as oksfile:
            conn.retrieveFile(shared_folder, path, oksfile)

        conn.close()

    except Exception as e:
        py_logger.critical(f'\n{datetime.datetime.now()} --- Connection Error: \n {e} \n')
        conn.close()
        return None
    

async def parse_leftovers_for_site(filepath):
    data = ''
    with open(filepath, 'r', encoding='windows-1251') as f:
        data = f.read().split('\n')

    start_line = data.index('$$$REPLACEQUANTITY') + 1
    end_line = data.index('$$$REPLACEASPECTREMAINS') - 1

    leftovers_data = data[start_line:end_line]

    catalogs = []
    products = []

    for line in leftovers_data:
        split_line = line.split(';')
        if split_line[16] == '0':
            # This group
            catalogs.append(
                {
                    'code_1c': int(split_line[0]),
                    'name': split_line[2],
                    'catalog': None if split_line[15] == '' else int(split_line[15]),
                    'child': []
                }
            )

        elif split_line[16] == '1':
            # This is are product
            products.append(
                {
                    'code_1c': int(split_line[0]),
                    'name': split_line[2],
                    #'receipt_name': split_line[3],
                    'price': float(split_line[4].replace(',', '.')),
                    'quantity': float(split_line[5].replace(',', '.')),
                    'catalog': None if split_line[15] == '' else int(split_line[15])
                }
            )

    return catalogs, products


async def get_customers(token, debug):
    if debug:
        url = f'http://127.0.0.1:8000/api/v1/customers/'
    else:
        url = f'https://neit.ru/api/v1/goods/'
    header = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=header, timeout=500)
    response.raise_for_status()

    return response.json()


async def get_customers_public(debug):
    if debug:
        url = f'http://127.0.0.1:8000/api/v1/customers/'
    else:
        url = f'https://neit.ru/api/v1/goods/'

    response = requests.get(url, timeout=500)
    response.raise_for_status()

    return response.json()


async def get_customer_by_id(token, debug, id):
    if debug:
        url = f'http://127.0.0.1:8000/api/v1/customers/{id}/'
    else:
        url = f'https://neit.ru/api/v1/goods/'
    header = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=header, timeout=500)
    response.raise_for_status()

    return response.json()


async def get_customer_by_phone(token, debug, phone):
    if debug:
        url = f'http://127.0.0.1:8000/api/v1/customers/get_customer_by_phone/'
    else:
        url = f'https://neit.ru/api/v1/goods/'
    header = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        'phone_number': phone
    }

    response = requests.get(url, headers=header, json=data, timeout=500)
    response.raise_for_status()

    return response.json()


async def register_customer(token, debug, customer):
    if debug:
        url = f'http://127.0.0.1:8000/api/v1/customers/'
    else:
        url = f'https://neit.ru/api/v1/goods/'
    header = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.post(url, headers=header, json=customer, timeout=500)
    response.raise_for_status()

    return response.json()


async def register_customer_public(debug, customer):
    print('in register')
    if debug:
        url = f'http://127.0.0.1:8000/api/v1/customers/'
    else:
        url = f'https://neit.ru/api/v1/goods/'

    response = requests.post(url, json=customer, timeout=500)
    response.raise_for_status()
    print(response)

    return response.json()
    

async def main():
    env = Env()
    env.read_env()

    debug = True

    api_login = env.str('API_LOGIN')
    api_password = env.str('API_PASSWORD')
    #port = env.int('SMB_PORT')
    #oks_path = env.str('SMB_OKS_PATH')
    #shared_folder = env.str('SMB_SHARED_FOLDER')
    #username = env.str('SMB_USERNAME')
    #my_name = env.str('SMB_MY_NAME')
    #password = env.str('SMB_PASSWORD')
    #remote_name = env.str('SMB_REMOTE_NAME')
    #leftovers_path = env.str('SMB_LEFTOVERS_PATH')
    token=''

    try:
        token = await get_token(api_login, api_password, debug)
        print(token)
        '''
        await fetch_file(
                    leftovers_path,
                    shared_folder,
                    username,
                    password,
                    remote_name,
                    'ostatki.txt',
                    port,
                    my_name
                )
        '''                
        catalogs, products = await parse_leftovers_for_site('ostatki.txt')
        #response = await initial_catalogs_upload(token, catalogs, debug)
        #print(response)
        response = await initial_upload_products(token, products, debug)
        print(response)
        #products = await get_all_products_from_server(token, debug)
        #pprint(products)

        #product_id = 100
        #product = await get_product_by_id_public(product_id, debug)
        #pprint(product)

        #customers = await get_customers(token, debug)
        #pprint(customers)
        #customer = await get_customer_by_id(token, debug, 1)
        #pprint(customer)
        #customer = await get_customer_by_phone(token, debug, '+79149569967')
        #pprint(customer)

        #response = await register_customer(token, debug, {
        #    'email': 'asda@gdfdf.ru', 
        #    'password': 'password1', 
        #    'phone_number': '+79146667778',
        #    'first_name': 'Fedya',
        #    'last_name': 'Slyapkin'
        #    })
        #pprint(response)

        '''
        response = await register_customer_public(debug, {
            'email': 'asda@gdfdf.ru', 
            'password': 'password1', 
            'phone_number': '+79146667778',
            'first_name': 'Fedya',
            'last_name': 'Slyapkin'
            })
        pprint(response)
        '''

        #customers = await get_customers_public(debug)
        #pprint(customers)

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            print(e.response.json()['error'])

    #except Exception as e:
    #    py_logger.critical(f'\n{datetime.datetime.now()} --- Connection Error: \n {e} \n')


if __name__ == '__main__':
    # получение пользовательского логгера и установка уровня логирования
    py_logger = logging.getLogger(__name__)
    py_logger.setLevel(logging.INFO)

    # настройка обработчика и форматировщика в соответствии с нашими нуждами
    py_handler = logging.FileHandler(f"{__name__}.log", mode='a')
    py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    # py_handler. .handlers.RotatingFileHandler(f"{__name__}.log", 10000, 3)

    # добавление форматировщика к обработчику
    py_handler.setFormatter(py_formatter)
    # добавление обработчика к логгеру
    py_logger.addHandler(py_handler)
    rotate_handler = RotatingFileHandler(f"{__name__}.log", maxBytes=500000, backupCount=5)
    py_logger.addHandler(rotate_handler)

    asyncio.run(main())
