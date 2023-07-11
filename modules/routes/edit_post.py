
from modules.dependencies import *
from modules.file_utils import *
from modules.decorators import admin_required

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
    @app.route('/admin/edit/<slug>', methods=['GET', 'POST'])
    @admin_required
    def edit_post(slug):
        post_path = f"./posts/{slug}.md"

        if request.method == 'POST':
            new_content = request.form.get('content')
            print('Received content', new_content)
            # Generate a unique filename for the new post
            slug = format_to_slug(slug)

            # Save the post to a new file
            post_path = f'./posts/{slug}.md'
            write_file(post_path, new_content)
            return redirect(url_for('post', slug=slug))



        post_content = read_file(post_path)

        return render_template(
            'edit.html', 
            post_content=post_content, 
            post_title=slug, 
            logged_in=session.get('logged_in')
        )
