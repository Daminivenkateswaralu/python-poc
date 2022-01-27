from flask import Flask, jsonify

app = Flask(__name__)

users = [{'id': 0,'name':'john', 'email':'john@gmail.com','mobile':'8567891230'},
{'id': 1,'name':'David', 'email':'david@gmail.com','mobile':'4561237890'},
{'id': 2,'name':'roy', 'email':'roy@gmail.com','mobile':'7890123456'}]

@app.route("/")
def home():
    return "This is home page!!"

@app.route("/users", methods= ['GET'])
def getUsers():
    return jsonify({"users": users})

@app.route("/users/<int:id>", methods= ['GET'])
def getUsersfromId(id):
    return jsonify({"users": users[id]})

@app.route("/users", methods= ['POST'])
def createUser():
    user = {'id': 4,'name':'Deepak', 'email':'deepak@gmail.com','mobile':'7812345609'}
    users.append(user)
    return jsonify({'added user': user})

@app.route("/users/<int:id>", methods= ['PUT'])
def modifyUser(id):
    users[id]['id'] = 3
    return jsonify({'added user': users})

@app.route("/users/<int:id>", methods= ['DELETE'])
def deleteUser(id):
    users.remove(users[id])
    return jsonify({'Message': "User deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)

