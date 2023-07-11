
from modules.dependencies import *
from modules.file_utils import *
import os

def register_route(routes_blueprint, app, env):
    @app.route('/blog')
    @app.route('/blog/page/<int:page>')
    def blog(page=1):
        posts_per_page = 5
        posts = os.listdir('./posts')
        paths = [post.replace(".md", "") for post in posts]
        
        # Sort the paths based on the file modification timestamp in descending order
        paths.sort(key=lambda x: os.path.getmtime(f"./posts/{x}.md"), reverse=True)
        
        total_posts = len(paths)
        total_pages = (total_posts + posts_per_page - 1) // posts_per_page

        start_index = (page - 1) * posts_per_page
        end_index = start_index + posts_per_page
        paged_paths = paths[start_index:end_index]

        top_posts = paged_paths[:5]
        post_contents = []

        for post in top_posts:
            post_path = f"./posts/{post}.md"
            if os.path.exists(post_path):
                post_content = read_file(post_path)
                # print('post_content',post_content)
                post_content = extract_text_until_subtitle(post_content)
                print('extract_text_until_subtitle',post_content)
                post_content_with_link = wrap_title_with_link(post_content, post)
                print('wrap_title_with_link', post_content_with_link)
                post_contents.append(post_content_with_link)
                
        return render_template(
            'blog.html',
            posts=paged_paths,
            top_posts=top_posts,
            post_contents=post_contents,
            logged_in=session.get('logged_in'),
            username=session.get('username'),
            total_pages=total_pages,
            current_page=page
        )
