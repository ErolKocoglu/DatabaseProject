DEBUG = False
PORT = 8090
SECRET_KEY = "secret"
WTF_CSRF_ENABLED = True

PASSWORDS = {
    "admin": "$pbkdf2-sha256$29000$JURobc2Zs/b.v9fau/f.Pw$mtRukM9nSuiopdvTz3WN6zBr5NqwSjfA0ElolTdn0Ok",
    "normaluser": "$pbkdf2-sha256$29000$JURobc2Zs/b.v9fau/f.Pw$mtRukM9nSuiopdvTz3WN6zBr5NqwSjfA0ElolTdn0Ok",
}

ADMIN_USERS = ["admin"]