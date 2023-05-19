import jwt
from database.base import *
from flask import request
import json
import datetime
from config import SECRET_KEY_PASSWORD

def command_create(connect):
    token = jwt.decode(request.args["Authorization"], SECRET_KEY_PASSWORD, algorithms="HS256")
    data = json.loads(request.data)
    command = select(commnad_user).where(commnad_user.c.name == data["name"], commnad_user.c.user_id == token["ID"])
    result = connect.execute(command)
    for i in result:
        return {"success": False, "message": "У вас уже есть комманда с таким названием"}, 401
    date_today = datetime.datetime.today()
    command = insert(commnad_user).values(user_id=token["ID"], name=data['name'], date_Create=str(date_today))
    connect.execute(command)
    connect.commit()
    return {"success": True}