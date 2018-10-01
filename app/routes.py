from datetime import datetime

from flask import render_template

from app import app
from .models import Post

@app.route('/')
def home():
    lll
    return render_template('pages/home.html')


@app.route('/about')
def about():
    return render_template('pages/about.html')


@app.route('/contact')
def contact():
    return render_template('pages/contact.html')


@app.route('/blog')
def posts_index():
    return render_template('posts/index.html', posts=Post.query.all())


@app.route('/blog/posts/<int:id>')
def posts_show(id):
    post = Post.query.filter_by(id=id).first_or_404()
    return render_template('posts/show.html', post=post)


@app.context_processor
def utility_processor():
    def pluralize(count, singular, plural=None):
        if not isinstance(count, int):
            raise ValueError(f'"{count}" must be an integer.')
        
        if plural is None:
            plural = singular + 's'

        if count == 1:
            string = singular
        else:
            string = plural

        return f"{count} {string}"

    return dict(pluralize=pluralize, now=datetime.now())
