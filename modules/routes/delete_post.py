
from modules.dependencies import *
from modules.file_utils import *
from modules.decorators import admin_required

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/admin/delete/<slug>', methods=['GET', 'POST'])
    @admin_required
    def delete_post(slug):
        post_path = f"./posts/{slug}.md"

        if not os.path.exists(post_path):
            return 'Post not found', 404

        if request.method == 'POST':
            os.remove(post_path)
            return redirect(url_for('blog'))

        post_content = read_file(post_path)

        return render_template('delete.html', post_title=slug, post_content=post_content)
