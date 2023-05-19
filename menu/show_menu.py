import json

import jwt
from flask import request
from database.base import *
from config import SECRET_KEY_PASSWORD

def show_menu_user(connect):
    token = jwt.decode(request.args["Authorization"], SECRET_KEY_PASSWORD, algorithms="HS256")
    command = select(math).where(math.c.user_id == token["ID"]).order_by(math.c.id.desc()).limit(3)
    result = connect.execute(command)
    msg = ""
    num = 0
    for i in result:
        num += 1
        msg += json.dumps({'UserID': i[0], "ResultGame": "test", "ScoreOneTeams": i[4], "ScoreTwoTeams": i[5], "NumberTeam": i[2], "NumberTwoTeam": i[3]}) + "$"
    return {"success": True, "message": msg, "colvoGame": num}