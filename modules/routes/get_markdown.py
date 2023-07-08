# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/get-markdown/<path:slug>')
    def get_markdown(slug):
        if slug.startswith('coding'):
            if slug.endswith('-fr'):
                portfolio_path = f"./portfolio-fr.md"
            else:
                portfolio_path = f"./portfolio.md"
        elif slug.startswith('translation'):
            if slug.endswith('-fr'):
                portfolio_path = f"./translation_portfolio-fr.md"
            else:
                portfolio_path = f"./translation_portfolio.md"
        else:
            post_path = f"./posts/{slug}.md"
            if not os.path.exists(post_path):
                return 'Not found', 404
            return read_file(post_path)

        if not os.path.exists(portfolio_path):
            return 'Not found', 404

        return read_file(portfolio_path, encoding="UTF-8")