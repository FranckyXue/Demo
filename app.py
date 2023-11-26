from flask import Flask, request, jsonify
from extensions import db
import config

app = Flask(__name__)
app.config.from_object(config.Config)
db.init_app(app)

with app.app_context():
    db.create_all()

# 导入模型和路由
from models import User
@app.route('/')
def home():
    return 'Welcome to the User API'


@app.route('/get_user_list', methods=['GET'])
def get_user_list():
    users = User.query.all()
    return jsonify([user.serialize for user in users]), 200

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    user = User(name=data['name'], gender=data['gender'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize), 201

@app.route('/edit_user', methods=['PUT'])
def edit_user():
    data = request.json
    user = User.query.get(data['uid'])
    if user:
        user.name = data.get('name', user.name)
        user.gender = data.get('gender', user.gender)
        db.session.commit()
        return jsonify(user.serialize), 200
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
