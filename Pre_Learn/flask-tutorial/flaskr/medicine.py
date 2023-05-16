from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('medicine', __name__)


@bp.route('/medicine')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT id, name, description FROM medicine ORDER BY id ASC'
    ).fetchall()
    return render_template('medicine/index.html', posts=posts)
