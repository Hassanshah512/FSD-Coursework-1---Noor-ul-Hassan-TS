from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def random_year():
    year = random.randint(1, 2021)
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return render_template('random_year.html', year=year, is_leap=is_leap)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
