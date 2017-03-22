import hashlib
'''Module with basic resources authorization utilities.'''

class User:
    '''An user object'''

    def __init__(self,username,password):
        '''User Object initializer'''
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged = False

    def _encrypt_pw(self,password):
        '''Password encryption method. Returns sha digest'''
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self,password):
        '''Checks if password is valid for the user. Then returns True.'''
        encrypted = self._encrypt_pw(password)
        return self.password == encrypted

class AuthException(Exception):
    '''Exception to handle login issues.'''

    def __init__(self,username,user=None):
        super.__init__(self, username,user)
        self.username = username
        self.user = user

class PasswordTooShort(AuthException):
    '''Simple inheritance to see whats going on.'''
    pass

class UserAlreadyExists(AuthException):
    '''Simple inheritance to see whats going on'''
    pass

class Authenticator:
    '''Class for maintaining user list.'''

    def __init__(self):
        '''Initializer'''
        self.userlist = {}

    def add_user(self, username, password):
        '''Method for adding users. Throwing PasswordTooShort and UserAlreadyExists exceptions'''
        if username in self.userlist:
            raise UserAlreadyExists(username)
        elif len(password) < 6:
            raise PasswordTooShort("Password has to be at least 6 characters long!")
        else:
            self.userlist[username] = User(username,password)

    def login(self,username,password):

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass


if __name__ == '__main__':
    user = User("admin","password")
    print(user._encrypt_pw("blabla"))

