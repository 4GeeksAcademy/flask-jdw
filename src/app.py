from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from passlib.hash import pbkdf2_sha256 as sha256

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to your own secret key
jwt = JWTManager(app)

# Mock user data (for demonstration purposes)
users = [
    {'id': 1, 'username': 'user1', 'password': '$pbkdf2-sha256$29000$3VMfqfg3k7fe47guVhjrwQ$1A9VSMqgxzsoiU6Z01EnTAWIhNhoY89nN7N5BfV62Rk'},
    {'id': 2, 'username': 'user2', 'password': '$pbkdf2-sha256$29000$x6nukz1xYhnlIKtpWlWlvA$jvxBkpkHYVXfL.lT13gEd8pEQC0rLUzZ5tGmqqLWqdo'}
]

# Authentication endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = next((user for user in users if user['username'] == username), None)

    if not user or not sha256.verify(password, user['password']):
        return jsonify({'message': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=user['id'])
    return jsonify({'access_token': access_token}), 200

# Signup endpoint
@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    if next((user for user in users if user['username'] == username), None):
        return jsonify({'message': 'Username already exists'}), 400

    hashed_password = sha256.hash(password)
    new_user = {'id': len(users) + 1, 'username': username, 'password': hashed_password}
    users.append(new_user)

    return jsonify({'message': 'User created successfully'}), 201

# Protected route
@app.route('/private', methods=['GET'])
@jwt_required()
def private():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)
