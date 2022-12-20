from . import bp as app
from app import db
from app.blueprints.blog.models import Post
from flask_cors import cross_origin

@app.route('/posts')
@cross_origin
def api_posts():
    result = []

    for post in Post.query.all():
        result.append({
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'date_created': post.date_created,
            'username': post.user.username
        })

    return result

@app.route('/post/<id>')
@cross_origin
def api_post_by_id(id):
    post = Post.query.get(int(id))

    return {
        'id': post.id,
        'title': post.title,
        'body': post.body,
        'date_created': post.date_created,
        'username': post.user.username
    }