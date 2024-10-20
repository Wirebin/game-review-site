from flask import redirect, session, abort, url_for
from account import get_user_by_id
from functools import wraps


def admin_required(f):
    @wraps(f)
    def check_access(*args, **kwargs):
        user = get_user_by_id(session.get("user_id"))
        if user.access_level != "admin":
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
