from flask import *

from user.autme.autme import user_autme
from user.register.register import user_register
from database.base import base_connect
from menu.show_menu import show_menu_user
from show_matches.show_math import show_all_math
from command.show.all import command_show_all
from command.create.create import command_create
from command.show_current_command.show import show_current_command
from command.new_player.new_player import current_command_new_player

app = Flask(__name__)

@app.route("/user/autme", methods=["GET"])
def autme_user():
    return user_autme(connect)

@app.route("/user/register", methods=["POST"])
def register_user():
    return user_register(connect)

@app.route("/user/menu", methods=["GET"])
def menu_user():
    return show_menu_user(connect)

@app.route("/user/math/all", methods=["GET"])
def show_math_all():
    return show_all_math(connect)

@app.route("/user/command/show/all", methods=["GET"])
def show_command_all():
    return command_show_all(connect)

@app.route("/user/command/create", methods=["POST"])
def create_new_command():
    return command_create(connect)

@app.route("/user/command/current", methods=["GET"])
def show_cur_command():
    return show_current_command(connect)

@app.route("/user/command/current/player/new", methods=["POST"])
def new_player_command():
    return current_command_new_player(connect)

if __name__ == '__main__':
    connect = base_connect()
    print("Server started")
    app.run(debug=True, host="65.21.114.247")