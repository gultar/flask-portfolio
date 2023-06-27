from functools import wraps
from flask import redirect, url_for, session

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in') or session.get('username') != 'admin':
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function