"""
Nombre del Archivo: online_banking.py

Descripción:
Este programa simula un sistema de gestion de un banco online,
el siguiente tiene como caracteristicas:
    * Logueo de usuarios
    * Posibilidad de ingresar, extraer o transferir dinero
    * Desplegar un menu para realizar esas acciones

Autor: Lautaro Beutel
Fecha de Creación: 1 de enero de 2024
"""

import argparse

from model_user import User
from model_bank import Bank
from menu import Menu

#creo una lista de opciones
opciones = ['Add money', 'Extract money', 'Transfer', 'Exit']

#instancio un objeto menu de la clase menu
miMenu = Menu(opciones)

# Instancio tres objetos usuarioX de la clase User y los meto en una lista
usuario1 = User('martina', '13251')
usuario2 = User('jorge', '123')
usuario3 = User('pedro', 'contra123')

users_list = [usuario1, usuario2, usuario3]

# Instancio un objeto fakeBank de la clase Bank
fakeBank = Bank(users_list)

# Aquí comienza el código real del programa.
def main():
    # ... lógica principal del programa ...

    parser = argparse.ArgumentParser(description='client terminal interface for online bank')

    # Agrega argumentos opcionales "-u" y "-p" para el nombre de usuario y la contraseña
    parser.add_argument('-u', '--user', type=str, help='Username')
    parser.add_argument('-p', '--passw', type=str, help='User password')

    args = parser.parse_args()

    if args.user:
        user_name = args.user
    else:
        user_name = input('User: ')

    if args.passw:
        user_passwd = args.passw
    else:
        user_passwd = input('Password: ')

    if fakeBank.logIn(user_name, user_passwd):
        while True:
            print(f'\n{"*" * 100}')
            print(f'FakeBank, client: {fakeBank.session.name}, current money: {fakeBank.session.money}, client code: {fakeBank.session.user_code}\n')
            miMenu.showOptions()
            print(f'\n{"*" * 100}')
            selection = input(f'select a option (1-{len(opciones)}): ')

            if selection == '1':
                amount = int(input('Amount: '))
                fakeBank.session.money =+ amount
            elif selection == '2':
                amount = int(input('Amount: '))
                if fakeBank.usrEnough(amount):
                    fakeBank.extractMoney(amount)
                else:
                    print('Error: you havent enought money')
            elif selection == '3':
                fakeBank.showAll()
                amount = int(input('Amount: '))
                payee = int(input('payee user code: '))
                if fakeBank.usrEnough(amount):
                    fakeBank.sendMoney(amount, payee)
            elif selection == '4':
                print('Session closed, see you later!!!')
                break
            else:
                print('Error: invalid option')
if __name__ == "__main__":
    main()
