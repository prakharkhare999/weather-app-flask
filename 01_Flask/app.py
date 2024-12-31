from flask import Flask,render_template
app=Flask(__name__)

@app.route("/about",methods=['Get','Post'])
def hello():
    return render_template('about.html')

@app.route("/home")
def index():
    return render_template('home.html')


if __name__=='__main__':
    app.run(debug=True)