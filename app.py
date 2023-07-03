# from modules.dependencies import *
# from modules.routes import create_routes
# from flask_session import Session
# from modules.file_utils import *
# import secrets
# from dotenv import dotenv_values, load_dotenv  
# import os

# load_dotenv()
# env = dotenv_values(".env")

# app = Flask(__name__, template_folder='./templates',static_folder=os.path.abspath("./static"))
# app.config['SESSION_TYPE'] = 'filesystem'
# app.secret_key = secrets.token_hex(16)
# Session(app)


# if __name__ == '__main__':
#     create_routes(app)
#     app.jinja_env.auto_reload = True
#     app.config['TEMPLATES_AUTO_RELOAD'] = True
#     app.run(host="0.0.0.0", port='5000')
    
    
from modules.dependencies import *
from modules.routes import create_routes
from flask_session import Session
from modules.file_utils import *
import secrets
from dotenv import dotenv_values, load_dotenv
import os
from flask_sslify import SSLify

load_dotenv()
env = dotenv_values(".env")

app = Flask(__name__, template_folder='./templates', static_folder=os.path.abspath("./static"))
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = secrets.token_hex(16)
Session(app)

# Force HTTPS redirect
sslify = SSLify(app)

if __name__ == '__main__':
    create_routes(app)
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port='5000', ssl_context=('cert.pem', 'key.pem'))
