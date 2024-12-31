from flask import Flask,render_template,flash,redirect,url_for
from form import RegistrationForm,LoginForm
app=Flask(__name__)

app.config['SECRET_KEY']='9sJt17ArpPInvcVE'



@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        #data is a keyword
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))

    return render_template('register.html',title='Register',form=form)


@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',title='Login',form=form)

@app.route("/home")
def home():
    return render_template('home.html')












 


 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Change port here
