import jwt
from database.base import *
from flask import request
import json
import datetime
from config import SECRET_KEY_PASSWORD

def current_command_new_player(connect):
    token = jwt.decode(request.args["Authorization"], SECRET_KEY_PASSWORD, algorithms="HS256")
    data = json.loads(request.data)
    command = select(commnad_user).where(commnad_user.c.name == request.args["name"], commnad_user.c.user_id == token["ID"])
    result = connect.execute(command)
    for i in result:
        command = select(player_command).where(player_command.c.command_id == i[0], player_command.c.number == data["number"])
        result = connect.execute(command)
        for j in result:
            return {"success": False, "message": "В этой команде уже состоит игрок с таким номером"}, 401
        command = insert(player_command).values(command_id=i[0], fio=data['deistv'], number=data["number"])
        connect.execute(command)
        connect.commit()
        return {"success": True}