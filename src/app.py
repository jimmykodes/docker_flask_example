import json

from flask import Flask, abort, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(host='db:27017')
db = client.blog
posts = db.posts


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/new_post', methods=("GET",))
def new_post():
    return render_template("new_post.html")


@app.route('/posts', methods=("POST",))
def create_post():
    if not request.form:
        abort(400)
    data = request.form.to_dict()
    posts.insert_one(data)
    return redirect(url_for("list_posts"))


@app.route('/posts', methods=("GET",))
def list_posts():
    all_posts = []
    for post in posts.find():
        post['_id'] = str(post['_id'])
        all_posts.append(post)
    return jsonify(all_posts)


if __name__ == '__main__':
    app.run('0.0.0.0', '80', debug=True)
