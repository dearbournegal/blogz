from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:root@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(255))
#Whatever we need from the user
    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/newpost', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        #new_title = Blog(title_name)
        #new_body = Blog(body_name)
        
        new_unit = Blog(title, body)    

        # db.session.add(new_title)
        # db.session.add(new_body)
        db.session.add(new_unit)

        db.session.commit()

    tasks = Blog.query.all()
    # body= Blog.query.all()
    return render_template('newpost.html',title="Build a blog!", 
        tasks=tasks)#, body_tasks=body_tasks)


@app.route('/blog')#, methods=['POST'])
def delete_task():
    #if request.method == 'POST':
    #     title = request.form['title']
    #     titles.append(title)
    # if len(title) == 0:
    #     return redirect('/newpost', title_error = title)
    # if request.method == 'POST'
    #     title = request.form['title']
    # id = Blog.query.all()
    
    #bodies = Blog.query.all()
    #    print(titles)

    #titles = Blog.query.all()
    #body = bodies = Blog.query.all()
    #for title in titles:
    #    print(title)
    #    return title
    #body = request.args.get['body']  #from html assign to python variable
    titles = Blog.query.all()
    return render_template('/blog.html',titles = titles)


if __name__ == '__main__':
    app.run()