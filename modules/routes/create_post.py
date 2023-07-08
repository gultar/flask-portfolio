
from modules.dependencies import *
from modules.file_utils import *
from modules.decorators import admin_required

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/admin/edit/new', methods=['GET', 'POST'])
    @admin_required
    def create_post():
        if request.method == 'POST':
            new_content = request.form.get('content')
            title = request.form.get('title')

            if title == '':
                error_message = 'Title cannot be empty.'
                return render_template('new-post.html', error_message=error_message)

            slug = format_to_slug(title)
            post_path = f"./posts/{slug}.md"

            # Save the post to a new file
            write_file(post_path, new_content)
            return redirect(url_for('post', slug=slug))

        # Handle the GET request
        return render_template('new-post.html',logged_in=session.get('logged_in'))

