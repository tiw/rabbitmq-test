#! /usr/bin/env python
from flask import Flask, request, json, Response
import services

app = Flask(__name__)
app.debug = True


@app.route("/authenticate", methods=['POST'])
def authenticate():
    is_authenticated = services.authenticate(request.form['user_name'], request.form['password'])
    return Response(json.dumps({'is_authenticated': is_authenticated}), mimetype='application/json')
    #services.authenticate(user_name, password)


if __name__ == '__main__':
    app.run()
