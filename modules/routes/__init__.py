# from flask import Blueprint

# routes_blueprint = Blueprint('routes', __name__)

# from .login import *
# from .index import *
# from .coding_fr import *
# from .translation import *
# from .translation_fr import *
# from .blog import *
# from .terminal import *
# from .logout import *
# from .post import *
# from .search import *
# from .publications import *
# from .get_markdown import *
# from .get_list_of_pages import *
# from .get_post import *
# from .edit_post import *
# from .create_post import *
# from .delete_post import *
# from .skills import *


# route_modules = [
#     login,
#     index,
#     coding_fr,
#     translation,
#     translation_fr,
#     blog,
#     terminal,
#     logout,
#     post,
#     search,
#     publications,
#     get_markdown,
#     get_list_of_pages,
#     get_post,
#     edit_post,
#     create_post,
#     delete_post,
#     skills,
# ]

# def register_routes(app, env):
#     for route_module in route_modules:
#         print('ROUTE:', route_module)
#         res = route_module.register_route(routes_blueprint, app, env)
#         print('Result',res)
#     app.register_blueprint(routes_blueprint)

import os
import importlib
from flask import Blueprint

routes_blueprint = Blueprint('routes', __name__)

# Get the current directory
current_directory = os.path.dirname(__file__)

# Get a list of all Python files in the current directory
files = [f for f in os.listdir(current_directory) if f.endswith('.py')]

# Import all the modules dynamically
route_modules = []
for file_name in files:
    module_name = os.path.splitext(file_name)[0]
    if module_name != '__init__':
        module = importlib.import_module(f'.{module_name}', __name__)
        route_modules.append(module)

def register_routes(app, env):
    for route_module in route_modules:
        print('ROUTE:', route_module)
        res = route_module.register_route(routes_blueprint, app, env)
        print('Result', res)
    app.register_blueprint(routes_blueprint)

