import json

import jwt
from flask import request
from database.base import *
from config import SECRET_KEY_PASSWORD

def show_all_math(connect):
    token = jwt.decode(request.args["Authorization"], SECRET_KEY_PASSWORD, algorithms="HS256")
    command = select(math).where(math.c.user_id == token["ID"]).order_by(math.c.id.desc())
    result = connect.execute(command)
    msg = ""
    for i in result:
        msg += json.dumps(
            {'UserID': i[0], "ResultGame": "test", "ScoreOneTeams": i[4], "ScoreTwoTeams": i[5], "NumberTeam": i[2],
             "NumberTwoTeam": i[3]}) + "$"
    command = select(math).where(math.c.user_id == token["ID"])
    result = connect.execute(command)
    num = 0
    for i in result:
        num += 1
    return {"success": True, "message": msg, "colvoGame": num}