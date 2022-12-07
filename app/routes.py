from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import Post

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts():
    all_posts = Post.query.all()
    return render_template('posts.html', posts=all_posts)

# Create a dynamic route, that allows us
# to get a single post, based on it's ID.
@app.route('/post/<id>')
def post_by_id(id):
    post = Post.query.get(int(id))
    return render_template('post-single.html', post=post)

@app.route('/create-post', methods=["POST"])
def create_post():
    title = request.form['inputTitle']
    body = request.form['inputBody']
    new_post = Post(title=title, body=body, user_id=1)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('posts'))

@app.route('/test')
def test():
    return redirect('/another-test')