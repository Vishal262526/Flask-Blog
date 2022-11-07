from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = "TechBLOG: Home"
    return render_template("index.html", title=name)


@app.route("/blogs")
def blogs():
    name = "TechBLOG: Blogs"
    return render_template("blogs.html",title=name)


@app.route("/about")
def about():
    name = "TechBLOG: About"
    return render_template("about.html",title=name)


@app.route("/contact")
def contact():
    name = "TechBLOG: Contact"
    return render_template("contact.html",title = name)

app.run(debug=True)
