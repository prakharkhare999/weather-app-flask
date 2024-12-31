from flask import Flask, render_template
from form import RegistrationForm  # Assuming your form is named RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Don't forget to set a secret key for CSRF protection

@app.route('/', methods=["POST", "GET"])
def index():
    form = RegistrationForm()  # Create an instance of the form

    if form.validate_on_submit():  # Correct the typo here
        print(form.username.data)  # Access the form data
        return "Successful"
    
    return render_template("check.html", form=form)  # Pass the form to the template

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
