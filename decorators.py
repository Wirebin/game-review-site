from flask import redirect, session, abort, url_for
from functools import wraps


def admin_required(f):
    @wraps(f)
    def check_access(*args, **kwargs):
        if session.get('access_level') != 'admin':
            return abort(404)
        return f(*args, **kwargs)
    return check_access


def login_required(f):
    @wraps(f)
    def check_login(*args, **kwargs):
        if not session.get('user_id'):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return check_login
