# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/about')
    def about():
        about_content = read_file("./about.md", encoding="UTF-8")
        return render_template(
            'about.html',
            about_content=about_content,
            language="English",
            logged_in=session.get('logged_in'),
            username=session.get('username')
        )
