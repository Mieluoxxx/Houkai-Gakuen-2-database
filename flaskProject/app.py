from models import db
from config import app
from route import bp

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(bp)  # 设置路由

if __name__ == '__main__':
    app.run(debug=True)
    db.session.commit()
