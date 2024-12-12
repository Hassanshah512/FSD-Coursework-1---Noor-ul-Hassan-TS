from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def profile():
    return render_template('profile.html')

@app.route('/credit')
def credit():
    return render_template('credit.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
