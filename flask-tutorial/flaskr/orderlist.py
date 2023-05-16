from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('orderlist', __name__)


@bp.route('/orderlist')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT orderList.id AS 订单号, orderList.created AS 订单时间, customer.name AS 客户名称, customer.address AS 客户地址, '
        'medicine.name AS 药物名称'
        'FROM orderList '
        'JOIN customer ON orderlist.customer_id = customer.id '
        'JOIN medicine ON orderlist.medicine_id = medicine.id'
    ).fetchall()
    return render_template('orderlist/index.html', posts=posts)
