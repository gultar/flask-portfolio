from modules.dependencies import *
from modules.file_utils import *

def register_route(routes_blueprint, app, env):
    @app.route('/projects/<slug>')
    def project_view(slug):
        post_path = f"./projects/{slug}.md"

        if not os.path.exists(post_path):
            return 'Post not found', 404

        post_content = read_file(post_path, encoding="UTF-8")
        print(post_content)
        return render_template(
            'project-view.html', 
            post_content=post_content, 
            post_title=slug, 
            logged_in=session.get('logged_in'), 
            username=session.get('username')
        )
