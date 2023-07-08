# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route("/get-post/<slug>", methods=['GET'])
    def get_post(slug):
        post_path = f"./posts/{slug}.md"
        post_content = read_file(post_path)
        return post_content
