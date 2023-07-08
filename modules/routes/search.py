# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/search', methods=['GET'])
    def search():
        keyword = request.args.get('keyword')

        if keyword:
            # Get a list of posts that contain the keyword
            posts = []
            post_files = os.listdir('./posts')
            for post_file in post_files:
                with open(f'./posts/{post_file}', 'r') as f:
                    post_content = f.read()
                    if keyword.lower() in post_content.lower():
                        posts.append(post_file.replace(".md", ""))

            return render_template(
                'search_results.html', 
                keyword=keyword, 
                posts=posts, 
                logged_in=session.get('logged_in')
                )

        return redirect(url_for('index'))
