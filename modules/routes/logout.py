# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('index'))
