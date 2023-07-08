# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/coding-fr')
    def coding_fr():
        portfolio_content = read_file("./portfolio-fr.md", encoding="UTF-8")
        return render_template(
            'index.html',
            portfolio_content=portfolio_content,
            language="French",
            logged_in=session.get('logged_in'),
            username=session.get('username')
        )