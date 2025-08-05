from flask import Flask, jsonify, request

app = Flask(__name__)

# Sadə data (list formatında)
users = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Aysel"}
]

# Bütün istifadəçiləri göstər (GET)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Tək istifadəçi göstər (GET)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user) if user else ('Not Found', 404)

# Yeni istifadəçi əlavə et (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = {
        "id": len(users) + 1,
        "name": data.get("name")
    }
    users.append(new_user)
    return jsonify(new_user), 201

# API işə sal (run)
if __name__ == '__main__':
    app.run(debug=True)
