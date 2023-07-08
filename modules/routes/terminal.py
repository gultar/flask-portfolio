# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/terminal', methods=['GET'])
    def terminal():
        return render_template('terminal.html')
