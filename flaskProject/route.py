from flask import Blueprint, render_template, redirect, request, flash, jsonify
from datetime import date
from models import db, User, Customer, Medicine, Orderlist

bp = Blueprint('main', __name__)


@bp.route('/index')
def admin():
    return render_template('index.html')


@bp.route('/medicine')
def medicine():
    medicine = Medicine.query.all()
    return render_template('medicine/medicine.html', Medicines=medicine)


@bp.route('/customer')
def customer():
    customers = Customer.query.all()
    return render_template('customer/customer.html', Customers=customers)


@bp.route('/orderlist')
def orderlist():
    orderlist = Orderlist.query.all()
    return render_template('orderlist/orderlist.html', Orderlists=orderlist)


@bp.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print('获得的数据', username, password)
        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                return redirect('/index')
            else:
                flash('密码错误')
        else:
            flash('用户名不存在')
    return render_template('login.html')


@bp.route('/customer/add', methods=['GET', 'POST'])
def customer_add():
    if request.method == 'POST':
        customer_name = request.form.get('customer_name')
        customer_sex = request.form.get('customer_sex')
        customer_phone = request.form.get('customer_phone')
        customer_address = request.form.get('customer_address')
        if customer_name != "" and customer_sex != "" \
                and customer_phone != "" and customer_address != "":
            new_customer = Customer(name=customer_name, sex=customer_sex, phone=customer_phone,
                                    address=customer_address)
            print(customer_name, customer_sex, customer_phone, customer_address)
            db.session.add(new_customer)
            db.session.commit()
        return redirect('/customer')
    return render_template('customer/customer_add.html')


@bp.route('/customer/delete')
def customer_delete():
    customer_id = request.args.get('id')
    customer = Customer.query.filter_by(id=customer_id).first()
    if customer is None:
        return '客户不存在'
    db.session.delete(customer)
    db.session.commit()
    db.session.close()
    return redirect('/customer')


@bp.route('/customer/change', methods=['GET', 'POST'])
def customer_change():
    customer_id = request.args.get('id')
    customer = Customer.query.filter_by(id=customer_id).first()
    if request.method == 'POST':
        customer_name = request.form.get('customer_name')
        customer_sex = request.form.get('customer_sex')
        customer_phone = request.form.get('customer_phone')
        customer_address = request.form.get('customer_address')

        if not customer_name:
            flash('客户姓名不能为空')
            return redirect('/customer_change')
        if not customer_sex:
            flash('客户性别不能为空')
            return redirect('/customer_change')
        if not customer_phone:
            flash('客户联系方式不能为空')
            return redirect('/customer_change')

        customer.name = customer_name
        customer.sex = customer_sex
        customer.phone = customer_phone
        customer.address = customer_address

        db.session.add(customer)
        db.session.commit()
        return redirect('/customer')
    return render_template('customer/customer_change.html', customer=customer)


@bp.route('/medicine/add', methods=['GET', 'POST'])
def medicine_add():
    if request.method == 'POST':
        medicine_id = request.form.get('medicine_id')
        medicine_name = request.form.get('medicine_name')
        medicine_price = float(request.form.get('medicine_price'))
        medicine_stock = int(request.form.get('medicine_stock'))
        medicine_description = request.form.get('medicine_description')
        if medicine_id != "" and medicine_name != "" \
                and medicine_price != "" and medicine_stock != "" \
                and medicine_description != "":
            new_medicine = Medicine(id=medicine_id, name=medicine_name, price=medicine_price,
                                    stock=medicine_stock, description=medicine_description)
            print(medicine_id, medicine_name, medicine_price, medicine_stock, medicine_description)
            db.session.add(new_medicine)
            db.session.commit()
        return redirect('/medicine')
    return render_template('medicine/medicine_add.html')


@bp.route('/medicine/delete')
def medicine_delete():
    medicine_id = request.args.get('id')
    medicine = Medicine.query.filter_by(id=medicine_id).first()
    if medicine is None:
        return '药物不存在'
    db.session.delete(medicine)
    db.session.commit()
    db.session.close()
    return redirect('/medicine')


@bp.route('/medicine/change', methods=['GET', 'POST'])
def medicine_change():
    medicine_id = request.args.get('id')
    medicine = Medicine.query.filter_by(id=medicine_id).first()
    if request.method == 'POST':
        medicine_id = request.form.get('medicine_id')
        medicine_name = request.form.get('medicine_name')
        medicine_price = float(request.form.get('medicine_price'))
        medicine_stock = int(request.form.get('medicine_stock'))
        medicine_description = request.form.get('medicine_description')

        if not medicine_id:
            flash('批准文号不能为空')
            return redirect('/medicine_change')
        if not medicine_name:
            flash('药物名称不能为空')
            return redirect('/medicine_change')
        if not medicine_price:
            flash('药物售价不能为空')
            return redirect('/medicine_change')
        if not medicine_stock:
            flash('药物库存量不能为空')
            return redirect('/medicine_change')

        medicine.id = medicine_id
        medicine.name = medicine_name
        medicine.price = medicine_price
        medicine.stock = medicine_stock
        medicine.description = medicine_description

        db.session.add(medicine)
        db.session.commit()
        return redirect('/medicine')
    return render_template('medicine/medicine_change.html', medicine=medicine)


# 定义路由，用于处理获取药品详情的请求
@bp.route('/medicine/detail')
def medicine_detail():
    # 获取药品 ID
    id = request.args.get('id')

    # 从数据库中获取药品信息
    medicine = Medicine.query.get(id)

    # 将药品信息转换为字典
    if medicine:
        medicine_dict = medicine.to_dict()
        # 将药品信息转换为 JSON 格式，并将其作为响应发送回客户端
        return jsonify(medicine_dict)
    else:
        return jsonify({'error': 'Medicine not found'})


@bp.route('/orderlist/add', methods=['GET', 'POST'])
def orderlist_add():
    if request.method == 'POST':
        orderlist_name = request.form.get('order_name')
        orderlist_c_id = int(request.form.get('order_c_id'))
        orderlist_m_id = request.form.get('order_m_id')
        orderlist_quantity = int(request.form.get('order_quantity'))
        if orderlist_name and orderlist_c_id and orderlist_m_id and orderlist_quantity:
            if orderlist_c_id not in [c.id for c in Customer.query.all()]:
                flash('Invalid customer ID')
            elif orderlist_m_id not in [m.id for m in Medicine.query.all()]:
                flash('Invalid medicine ID')
            elif orderlist_quantity <= 0:
                flash('Invalid quantity')
            else:
                new_orderlist = Orderlist(m_id=orderlist_m_id, c_id=orderlist_c_id, name=orderlist_name,
                                          quantity=orderlist_quantity,
                                          date=date.today().strftime('%Y-%m-%d'))
                try:
                    db.session.add(new_orderlist)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    print(str(e))
                return redirect('/orderlist')
        else:
            flash('Invalid input')
    return render_template('orderlist/orderlist_add.html', customers=Customer.query.all(),
                           medicines=Medicine.query.all())


def orderlist_delete():
    orderlist_id = request.args.get('id')
    order = Orderlist.query.filter_by(id=orderlist_id).first()
    order.type = "退货"
    order.date = date.today()
    db.session.add(order)
    db.session.commit()
    db.session.close()
    return render_template('orderlist/orderlist.html')


@bp.route('/orderlist/detail')
def orderlist_detail():
    # 获取订单 ID
    id = request.args.get('id')
    # 从数据库中获取订单信息
    order = Orderlist.query.get(id)
    medicine = Medicine.query.get(order.m_id)
    customer = Customer.query.get(order.c_id)
    # 将订单信息转换为字典
    if order and medicine and customer:
        order_dict = order.to_dict()
        medicine_dict = medicine.to_dict()
        customer_dict = customer.to_dict()
        # 将订单信息转换为 JSON 格式，并将其作为响应发送回客户端
        return jsonify(order_dict, medicine_dict, customer_dict)


@bp.route('/test')
def test():
    return render_template('test.html')
