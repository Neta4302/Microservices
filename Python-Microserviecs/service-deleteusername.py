from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

username = us.user_name()

# Find data in json
#def _find_user(user, username):
#    data = [x for x in username if x["user"]==user]
#    return data

@app.route('/delete/<user>', methods=['DELETE'])
def delete(user):
    _user = us.delete_username(user)
    if _user is None:
        return jsonify({ 'error': 'Username does not exist.' }), 403

    data = [x for x in username if x['user'] != user]
    return jsonify({ 'message': 'Delete successfully!' }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1