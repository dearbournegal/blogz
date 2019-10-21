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
    #if request.method == 'POST':
    #     title = request.form['title']
    #     titles.append(title)
        title = request.form['title']
        body = request.form['body']
        title_error =""
        body_error = ""
        if len(title) == 0:
            title_error = "You need a title"
            #return redirect('/newpost', title_error = title)
        if len(body) == 0:
            body_error = "You need content"

        if title_error or body_error:
            return render_template('newpost.html',title="Build a blog!", 
            title_error = title_error, body_error = body_error)

        new_unit = Blog(title, body)    

        db.session.add(new_unit)
        db.session.commit()

        return redirect('/blog?id=' + str(new_unit.id))
    return render_template('/newpost.html')

@app.route('/blog')#, methods=['POST'])
def show():
    the_id = str(request.args.get('id'))
    the_post = Blog.query.get(the_id)



    
    #bodies = Blog.query.all()
    #    print(titles)
    #id = Blog.query.order_by(desc(Blog.id))
    #titles = Blog.query.all()
    #body = bodies = Blog.query.all()
    #for title in titles:
    #    print(title)
    #    return title
    #body = request.args.get['body']  #from html assign to python variable
    blogs = Blog.query.all()
    # return render_template('/blog.html?id=',id,titles = titles)
    return render_template('blog.html',blogs = blogs, mypost = the_post)

if __name__ == '__main__':
    app.run()