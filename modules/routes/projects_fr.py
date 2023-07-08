# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/projects-fr')
    def projects_fr():
        portfolio_content = read_file("./projects-fr.md", encoding="UTF-8")
        return render_template(
            'projects.html',
            portfolio_content=portfolio_content,
            language="Français",
            logged_in=session.get('logged_in'),
            username=session.get('username')
        )
