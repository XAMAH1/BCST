import json

import jwt
from flask import request
from database.base import *
from config import SECRET_KEY_PASSWORD

def show_current_command(connect):
    token = jwt.decode(request.args["Authorization"], SECRET_KEY_PASSWORD, algorithms="HS256")
    command = select(commnad_user).where(commnad_user.c.user_id == token["ID"], commnad_user.c.name == request.args["name"])
    result = connect.execute(command)
    for current_command in result:
        command = select(player_command).where(player_command.c.command_id == current_command[0])
        msg = ""
        num = 0
        result = connect.execute(command)
        for i in result:
            num += 1
            msg += json.dumps({'ID': i[0], "Name": i[2]}) + "$"
        return {"success": True, "message": msg, "colvoGame": num, "dateCreate": current_command[3]}