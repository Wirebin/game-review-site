from flask import redirect, url_for, session, abort
from functools import wraps


def admin_required(f):
    @wraps(f)
    def check_access(*args, **kwargs):
        print("Decorator called")
        print("Session access level:", session.get('access_level'))
        if session.get('access_level') != 'admin':
            return abort(404)
        return f(*args, **kwargs)
    return check_access

