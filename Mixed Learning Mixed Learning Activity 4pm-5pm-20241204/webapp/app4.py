from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def daily_quote():
    quotes = [
        "The best way to predict the future is to create it.",
        "Don't watch the clock; do what it does. Keep going.",
        "Act as if what you do makes a difference. It does.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "The only limit to our realization of tomorrow is our doubts of today.",
    ]
    quote = random.choice(quotes)
    return render_template('daily_quote.html', quote=quote)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
