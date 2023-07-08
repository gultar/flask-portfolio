from flask import jsonify
import json
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/get-list-of-pages/', methods=['GET'])
    def get_list_of_pages():
        pages_list = ["coding","coding-fr","translation","translation-fr"]
        return json.dumps(pages_list)
