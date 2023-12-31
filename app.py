# from modules.dependencies import *
# from modules.routes import create_routes
# from flask_session import Session
# from modules.file_utils import *
# import secrets
# from dotenv import dotenv_values, load_dotenv  
# import os

# load_dotenv()
# env = dotenv_values(".env")

# if "ADMIN_USER" not in env:
#     env["ADMIN_USER"] = os.environ.get("ADMIN_USER")

# if "ADMIN_PASSWORD" not in env:
#     env["ADMIN_PASSWORD"] = os.environ.get("ADMIN_PASSWORD")

# app = Flask(__name__, template_folder='./templates',static_folder=os.path.abspath("./static"))
# app.config['SESSION_TYPE'] = 'filesystem'
# app.secret_key = secrets.token_hex(16)
# Session(app)


# if __name__ == '__main__':
#     create_routes(app)
#     print('ENVNN',os.environ.get("ADMIN_USER"))
#     print('ENVNN',os.environ.get("ADMIN_PASSWORD"))
#     app.jinja_env.auto_reload = True
#     app.config['TEMPLATES_AUTO_RELOAD'] = True
#     app.run(host="0.0.0.0", port='5000', debug=True)
    
from flask import Flask
from flask_session import Session
from modules.routes import register_routes
from modules.dependencies import load_dotenv, dotenv_values
from modules.file_utils import *
import secrets
import os

load_dotenv()
env = dotenv_values(".env")

if "ADMIN_USER" not in env:
    env["ADMIN_USER"] = os.environ.get("ADMIN_USER")

if "ADMIN_PASSWORD" not in env:
    env["ADMIN_PASSWORD"] = os.environ.get("ADMIN_PASSWORD")

app = Flask(__name__, template_folder='./templates', static_folder=os.path.abspath("./static"))
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = secrets.token_hex(16)
Session(app)

register_routes(app, env)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port='5000',debug=True)


