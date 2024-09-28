from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/gallery.html")
def gallery():
    return render_template("gallery.html")
@app.route("/menu.html")
def menu():
    return render_template("menu.html")
@app.route("/about.html")
def about():
    return render_template("about.html")
@app.route("/contact.html")
def contact():
    return render_template("contact.html")
if __name__=='__main__':
    app.run(debug=True)