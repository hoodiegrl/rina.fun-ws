from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)

@app.route('/')
def index():
   return render_template("home.html") 

@app.route('/home')
def home():
    return render_template('home1.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/manifesto')
def manifesto():
    return render_template('manifesto.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/kinlist')
def kin():
    return render_template('kinnie.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/rick')
def rick():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")



if __name__ == '__main__':
    app.debug = True
    app.run() # http://127.0.0.1:5000/ 