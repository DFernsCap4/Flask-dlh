from flask import (
    Blueprint, flash, g, redirect, render_template, request , url_for
)

from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created_at, user_id, username FROM posts p JOIN users u ON p.user_id = u.id ORDER BY created_at DESC'
    ).fetchall()
    
    return render_template('blog/index.html',posts=posts)

