#1
class InvalidUsernameError(Exception):
    def __init__(self, username):
        self.username=username


def register_user(username):
    if len(username)<5 or username=="hitler" or len(username)>20:
        raise InvalidUsernameError(username)
    else:
        print(":)")
#priklad
try:
    username=input()
    register_user(username)
except InvalidUsernameError as e:
    print(f":( {e.username}, minimum 5 symbols, maximum 20 or unacceptable name")




#2
class InvalidPasswordError(Exception):
    def __init__(self, password):
        self.password=password

def validate_password(password):
    if len(password)<3:
        raise InvalidPasswordError(password)
    else:
        print("good password")
def validate_password2(password):
    k=0
    for i in password:
        if i.isnumeric():
            k=k+1
    if k==0:
        raise InvalidPasswordError(password)
    else:
        print("good password")
#priklad
try:
    password=input()
    validate_password(password)
    validate_password2(password)
except InvalidPasswordError as p:
    print(f'Bad password :(, {p.password}, minimum 3 symbols, or password does not contain numbers')




#3
class InvalidFileFormatError(Exception):
    def __init__(self, filename):
        self.filename=filename

def read_file(filename):
