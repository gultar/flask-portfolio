# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/publications')
    def post_titles():
        posts = os.listdir('./posts')
        post_filenames = [post.replace('.md', '') for post in posts]
        post_contents = []

        for post in posts:
            post_path = f"./posts/{post}"
            post_contents.append(read_file(post_path))

        post_titles = [extract_post_title(post) for post in post_contents]

        print(post_titles)

        return render_template(
            'publications.html', 
            post_titles=post_titles, 
            post_filenames=post_filenames,
            logged_in=session.get('logged_in'),
        )
