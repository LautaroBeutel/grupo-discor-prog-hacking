class Bank():
    def __init__(self, users_list):
        self.users_list = users_list
        self.session = False

    def showAll(self):
        print(f'\n{"*"*50}\n')
        print('Usuarios: ')
        for i in self.users_list:
            print(f'\tnombre: {i.name}\t   user code: {i.user_code}')
        print(f'\n{"*"*50}\n')

    def usrExist(self, user_name):
        for usr in self.users_list:
            if usr.name == user_name:
                return usr
        return False
    
    def codeExist(self, usr_code):
        for usr in self.users_list:
            if usr.user_code == usr_code:
                return usr
        return False

    def logIn(self, usr_name, usr_pswd):
        user = self.usrExist(usr_name)
        if user != False:
            if user.paswd == usr_pswd:
                self.session = user
                return True
            else:
                print('Error: Wrong password')
        else:
            print('Error: user dont exist')
            return False

    def usrEnough(self, mount):
        if self.session.money < mount:
            return False
        return True

    def addMoney(self, amount):
        if self.session == False:
            print('Error: not logged')
            return False
        else:
            self.session.money += amount
            print(f'mount: {self.session.money}')
    
    def extractMoney(self, amount):
        if self.usrEnough(amount):
            self.session.money -= amount

    def sendMoney(self, amount, payee_code):
        usr = self.codeExist(payee_code)
        if usr == False:
            print('Error: cant find the user')
            return False
        else:
            self.session.money -= amount
            usr.money += amount