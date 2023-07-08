# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/post/<slug>')
    def post(slug):
        post_path = f"./posts/{slug}.md"

        if not os.path.exists(post_path):
            return 'Post not found', 404

        post_content = read_file(post_path)

        return render_template(
            'post.html', 
            post_content=post_content, 
            post_title=slug, 
            logged_in=session.get('logged_in'), 
            username=session.get('username')
        )
