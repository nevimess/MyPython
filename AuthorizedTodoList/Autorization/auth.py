import hashlib, json, pickle
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
    '''Base exception to handle login issues.'''

    def __init__(self,username,user=None):
        super.__init__(self, username,user)
        self.username = username
        self.user = user

class PasswordTooShort(AuthException):
    '''Is raised when password is less than 6 characters'''
    pass

class UserAlreadyExists(AuthException):
    '''Is raised when user already exists'''
    pass

class Authenticator:
    '''Class for maintaining user list.'''

    USER_FILE = 'users.pickle'

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
        '''Trying to login with provided credentials.'''
        try:
            user = self.userlist[username]
        except KeyError:
            raise InvalidUsername(username + " not found!")

        if not user.check_password(password):
            raise InvalidPassword("Wrong password!")

        user.is_logged = True
        return True

    def logout(self,username):
        '''Performing a logout'''
        try:
            user = self.userlist[username]
        except KeyError:
            raise InvalidUsername(username + "not found")
        user.is_logged = False

    def is_logged(self,username):
        '''Checking if user is logged in'''
        if username in self.userlist:
            return self.userlist[username].is_logged
        else:
            raise InvalidUsername(username + "not found")

    def serialize(self):
        '''Method for dumping credentials into file.'''
        try:
            with open(Authenticator.USER_FILE,'wb') as handle:
                pickle.dump(self.userlist,handle,protocol=pickle.HIGHEST_PROTOCOL)

        except Exception as e:
            print(e.__class__)
            print(e.args)

        finally:
            handle.close()

    def deserialize(self):
        '''Deserialisation back into objects'''
        try:
            with open(Authenticator.USER_FILE,'rb') as handle:
                data = pickle.load(handle)

        except Exception as e:
            print(e.__class__)
            print(e.args)

        finally:
            handle.close()
            self.userlist = data

class InvalidUsername(AuthException):
    '''Is raised when username is not found'''
    pass

class InvalidPassword(AuthException):
    '''Is raised when password do not match username'''
    pass

class Authorizor:
    '''Class to extend authenticator with permission options'''

    def __init__(self, authenticator):
        '''Initializer'''
        self. authenticator = authenticator
        self.permissions = {}

    def add_permission(self,perm_name):
        '''Creating a new permission to give an access.'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission already exists")

    def grant_permission(self,username,perm_name):
        '''Method that is used to grant permissions to user'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does noe exists!")
        else:
            if not username in self.authenticator.userlist:
                raise InvalidUsername("Username does not exists!")
            perm_set.add(username)

    def check_permisstion(self,username,perm_name):
        '''Checking if user has desired permition granted'''
        if not self.authenticator.is_logged(username):
            raise NotLoggedInError(username + " not logged in!")
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exists")
        else:
            if username not in perm_set:
                raise NotPermitted(username)
            else:
                return True

class NotLoggedInError(AuthException):
    '''Is raised when user is not logged in'''
    pass

class NotPermitted(AuthException):
    '''It is raised when user is not permitted to this resource'''
    pass

class PermissionError(AuthException):
    '''It is raised when theres an error with permission.'''
    pass

authenticator = Authenticator()
authorizor = Authorizor(authenticator)


