from TodoApp import todolist
from Autorization import auth
from pprint import pprint
import sys

class BadInput(Exception):
    '''Exception for bad input from user'''
    pass

class TodoAuth():
    '''Main class for auth TodoList'''

    commandlist_logoff = ['1. Login', '2. Create user','3. Exit']
    commandlist_logoff_cnt = 3

    commandlist_loggedon = todolist.TodoList.actions
    commandlist_loggedon_cnt = 9


    def __init__(self):
        '''Initializer'''
        self.todolist = todolist.TodoList()

    def printer(self,list):
        '''List printer'''
        for item in list:
            pprint(item)

    def input_check(self,inputt,command_cnt):
        '''Input validation'''
        try:
            inputt = int(inputt)
        except ValueError:
            raise BadInput("Input is not a number!")
        if((inputt > command_cnt) or (inputt < 1)):
            raise BadInput("Input not in command range! Check and try again!")


    def main(self):
        '''Main function of app'''
        validator = auth.authorizor
        validator.authenticator.deserialize()
        while True:
            self.printer(TodoAuth.commandlist_logoff)
            try:
                command = raw_input("Choose a command\n")
                self.input_check(command,TodoAuth.commandlist_logoff_cnt)

            except BadInput as e:
                pprint(e.__class__)
                pprint(e.args)
                continue

            if(command == '1'):
                username = raw_input("Enter your login: \n")
                password = raw_input("Entry your password: \n")
                try:
                    if validator.authenticator.login(username,password):  #Calling login method
                        self.input_check(command,TodoAuth.commandlist_loggedon_cnt)
                        self.todolist.change_username(username)
                        self.todolist.main()
                except Exception as e:
                    pprint(e.__class__)
                    pprint(e.args)
                    pass
            elif(command == '2'):
                username = raw_input("Enter desired login: \n")
                password = raw_input('Enter desired password: \n')
                try:
                    validator.authenticator.add_user(username,password)
                    validator.authenticator.serialize()
                except Exception as e:
                    pprint(e.__class__)
                    pprint(e.args)
            elif(command == '3'):
                pprint("Terminating Application")
                validator.authenticator.serialize()
                sys.exit(-1)


if __name__ == '__main__':
    app = TodoAuth()
    app.main()
