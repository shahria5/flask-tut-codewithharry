from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
import json
import os
from werkzeug.utils import secure_filename
import math

with open("config.json", "r") as f:
    params= json.load(f)["params"]

app = Flask(__name__)
app.secret_key= "super_secret_key"

app.config["UPLOAD_FOLDER"]= params["upload_location"]
app.config.update(
    MAIL_SERVER= "smtp.gmail.com",
    MAIL_PORT= 587,
    MAIL_USE_SSL= False,
    MAIL_USE_TLS= True,
    MAIL_USERNAME= params["gmail_user"],
    MAIL_PASSWORD= params["gmail_password"]
)

mail= Mail(app)

local_server= True
if local_server:    
    app.config["SQLALCHEMY_DATABASE_URI"] = params["local_uri"]
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["prod_uri"]

db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mess = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(35), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(50), nullable=True)
    img_file = db.Column(db.String(50), nullable=True)
    tag_line = db.Column(db.String(50), nullable=False)



@app.route("/")
def home():
    posts= Posts.query.filter_by().all()
    last= math.ceil(len(posts)/int(params["number_of_posts"]))
    """[:params["number_of_posts"]]"""

    

    page= request.args.get("number")
    print("first:", page)

    if(str(page).isnumeric()==False):
        page= 1

    print("second:", page)

    page= int(page)
    
    if page==1:
        prev= "#"
        nextp= "/?number=" + str(page+1)
    elif page==last:
        prev= "/?number=" + str(page-1)
        nextp= "#"
    else:
        prev= "/?number=" + str(page-1)
        nextp= "/?number=" + str(page+1)


    posts= posts[(page-1)*int(params["number_of_posts"]):(page-1)*int(params["number_of_posts"])+int(params["number_of_posts"])]



    

    return render_template("index.html", params=params, posts=posts, prev=prev, nextp=nextp)


@app.route("/about")
def about():
    return render_template("about.html", params=params)


@app.route("/post/<string:post_slug>", methods=["GET"])
def post_route(post_slug):
    post= Posts.query.filter_by(slug=post_slug).first()

    return render_template("post.html", post=post, params=params)



@app.route("/contact", methods=["GET", "POST"])
def contact():
    if(request.method=="POST"):
        
        name= request.form.get("name")
        email= request.form.get("email")
        phone= request.form.get("phone")
        message= request.form.get("message")
        
        entry= Contacts(name=name, phone_num=phone, mess=message, email=email, date=datetime.now())
      
        db.session.add(entry)
        db.session.commit()

        mail.send_message(f"new messsage from {name}", sender=email, recipients=[params["gmail_user"]], body=f"{message}\n{phone}")
        
    return render_template("contact.html", params=params)



@app.route("/post")
def post():
    return render_template("post.html", params=params)



@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if ("user" in session and session["user"]==params["admin_user"]):
        posts= Posts.query.all()
        return render_template("dashboard.html", params=params, posts=posts)

    if request.method=="POST":
        username= request.form.get("username")
        password= request.form.get("password")
        
        if (username==params["admin_user"] and password==params["admin_password"]):
            posts= Posts.query.all()
            session["user"] = username
            return render_template("dashboard.html", params=params, posts=posts)
        

    return render_template("login.html", params=params)


@app.route("/edit/<string:sno>", methods=["GET", "POST"])
def edit(sno):
    if ("user" in session and session["user"]==params["admin_user"]):
        
        if request.method=="POST": 
            box_title= request.form.get("title")
            tag_line= request.form.get("tag_line")
            slug= request.form.get("slug")
            content= request.form.get("content")
            img_file= request.form.get("img_file")

            if sno=="0": 
                post= Posts(title=box_title, tag_line=tag_line, slug=slug, content=content, img_file=img_file, date=datetime.now())
                db.session.add(post)
                db.session.commit()
            else:
                post= Posts.query.filter_by(sno=sno).first()
                post.title= box_title
                post.tag_line= tag_line
                post.slug= slug
                post.content= content
                post.img_file= img_file
                post.date= datetime.now()

                db.session.commit()

                return redirect(f"/edit/{sno}")
        post= Posts.query.filter_by(sno=sno).first()
        return render_template("edit.html", params=params, post=post)        

               
@app.route("/uploader", methods=["GET", "POST"])
def uploader():
    if ("user" in session and session["user"]==params["admin_user"]):
     if request.method=="POST": 
         f= request.files["file1"]
         print(f.filename)
         f.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(f.filename)))
         return "uploaded successfully"



@app.route("/logout")
def logout():
    session.pop("user")
    return redirect("/dashboard")

@app.route("/delete/<string:sno>", methods=["GET", "POST"])
def delete(sno):
    if ("user" in session and session["user"]==params["admin_user"]):
        post= Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()

        return redirect("/dashboard")


app.run(debug=True)






