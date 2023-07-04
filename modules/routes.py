from modules.dependencies import *
from modules.file_utils import *
from modules.decorators import *
import os

def create_routes(app):
        
    load_dotenv()
    env = dotenv_values(".env")

    # Define the context processor
    @app.context_processor
    def inject_current_page():
        def get_current_page():
            return request.path

        # Return the current_page function under the variable name 'current_page'
        return dict(current_page=get_current_page)


    # Route for user login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            
            if "ADMIN_USER" not in env:
                env["ADMIN_USER"] = os.environ.get("ADMIN_USER")

            if "ADMIN_PASSWORD" not in env:
                env["ADMIN_PASSWORD"] = os.environ.get("ADMIN_PASSWORD")

            if username == env["ADMIN_USER"] and password == env["ADMIN_PASSWORD"]:
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('index'))
            else:
                return 'Invalid credentials'

        return render_template('login.html')
    
    # Default route for the home page
    @app.route('/')
    def index():
        portfolio_content = read_file("./portfolio.md", encoding="UTF-8")
        return render_template(
            'index.html',
            portfolio_content=portfolio_content,
            language="English",
            logged_in=session.get('logged_in'),
            username=session.get('username')
        )
    
    # Route for the French version of the coding portfolio
    @app.route('/coding-fr')
    def coding_fr():
        portfolio_content = read_file("./portfolio-fr.md", encoding="UTF-8")
        return render_template(
            'index.html',
            portfolio_content=portfolio_content,
            language="French",
            logged_in=session.get('logged_in'),
            username=session.get('username')
        )
    
    # Route for the translation portfolio
    @app.route('/translation')
    def translation():
        portfolio_content = read_file("./translation_portfolio.md", encoding="UTF-8")
        return render_template(
            'translation-portfolio.html',
            portfolio_content=portfolio_content,
            language="English",
            logged_in=session.get('logged_in'),
            username=session.get('username')
        )
    
    # Route for the French version of the translation portfolio
    @app.route('/translation-fr')
    def translation_fr():
        portfolio_content = read_file("./translation_portfolio-fr.md", encoding="UTF-8")
        return render_template(
            'translation-portfolio.html',
            portfolio_content=portfolio_content,
            language="French",
            logged_in=session.get('logged_in'),
            username=session.get('username')
        )

    # Route for the blog page
    @app.route('/blog')
    @app.route('/blog/page/<int:page>')
    def blog(page=1):
        posts_per_page = 5
        posts = os.listdir('./posts')
        paths = [post.replace(".md", "") for post in posts]
        print('Path unsorted', paths)
        # Sort the paths based on the file modification timestamp in descending order
        paths.sort(key=lambda x: os.path.getmtime(f"./posts/{x}.md"), reverse=True)
        print('Path sorted', paths)
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
                post_content = extract_text_until_subtitle(post_content)
                post_content_with_link = wrap_title_with_link(post_content, post)
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
    
    # Route for the terminal page
    @app.route('/terminal', methods=['GET'])
    def terminal():
        return render_template('terminal.html')

    # Route for user logout
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('index'))

    # Route for displaying a blog post
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

    # Route for searching blog posts
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

    # Route for displaying post titles
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
    
    # Route for getting the content of a markdown file
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
    
    # Route for getting the content of a blog post
    @app.route("/get-post/<slug>", methods=['GET'])
    def get_post(slug):
        post_path = f"./posts/{slug}.md"
        post_content = read_file(post_path)
        return post_content


    # Route for editing a blog post (requires admin permission)
    @app.route('/admin/edit/<slug>', methods=['GET', 'POST'])
    @admin_required
    def edit_post(slug):
        post_path = f"./posts/{slug}.md"

        if request.method == 'POST':
            new_content = request.form.get('content')
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
    
    # Route for editing a blog post (requires admin permission)
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

    # Route for deleting a blog post (requires admin permission)
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

    return app
