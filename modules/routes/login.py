# from . import routes_blueprint
from modules.dependencies import *
from modules.file_utils import *

# @routes_blueprint.record
def register_route(routes_blueprint, app, env):
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
