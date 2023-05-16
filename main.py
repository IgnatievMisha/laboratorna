class InvalidUsernameError(Exception):
    def __init__(self, username):
        self.username=username


def register_user(username):
    if len(username)<5:
        raise InvalidUsernameError(username)
    else:
        print(":)")
#priklad
try:
    username=input()
    register_user(username)
except InvalidUsernameError as e:
    print(f":( {e.username}, minimum 5 symbols")