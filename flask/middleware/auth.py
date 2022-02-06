from functools import wraps
from db.database import connection, session
from models.users import Users
from flask import request, jsonify
import sys
import jwt


def auth(f):
    @wraps(f)
    def checkFunction(*args, **kwargs):
        auth = request.headers["Authorization"]
        if auth is None:
            return jsonify("Cannot Access")
        token = str.replace(str(auth), "Bearer ", "")
        uid = jwt.decode(token, "heedonge", options={
                         "verify_signature": False})["uid"]
        try:
            user = session.query(Users.uid).filter(Users.uid == uid).first()
            if user != None:
                if len(user) == 0:
                    return jsonify("Cannot Access")
                else:
                    return f(*args, **kwargs)
            else:
                return jsonify("Cannot Access")
        except Exception as e:
            session.rollback()
            print(e, file=sys.stderr)
            return jsonify("Cannot Access")
    return checkFunction
