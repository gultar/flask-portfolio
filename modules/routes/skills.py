from modules.dependencies import *
from modules.file_utils import *

def register_route(routes_blueprint, app, env):

    @app.route('/skills')
    def skills():
        return render_template(
            'skills.html',
            logged_in=session.get('logged_in'),
            username=session.get('username')
        )
