import json

import jwt
from flask import request
from database.base import *
from config import SECRET_KEY_PASSWORD

def command_show_all(connect):
    token = jwt.decode(request.args["Authorization"], SECRET_KEY_PASSWORD, algorithms="HS256")
    command = select(commnad_user).where(commnad_user.c.user_id == token["ID"]).order_by(commnad_user.c.id.desc())
    result = connect.execute(command)
    msg = ""
    for i in result:
        msg += json.dumps(
            {'ID': i[0], "Name": i[2]}) + "$"
    return {"success": True, "message": msg}