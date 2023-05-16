from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('customer', __name__)

@bp.route('/customer')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT name, phone, address FROM customer'
    ).fetchall()
    return render_template('customer/index.html', posts=posts)