# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/translation-fr')
    def translation_fr():
        portfolio_content = read_file("./translation_portfolio-fr.md", encoding="UTF-8")
        return render_template(
            'translation-portfolio.html',
            portfolio_content=portfolio_content,
            language="French",
            logged_in=session.get('logged_in'),
            username=session.get('username')
        )
