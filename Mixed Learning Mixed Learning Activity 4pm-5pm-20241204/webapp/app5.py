from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def weather_facts():
    facts = [
        "The highest temperature ever recorded on Earth was 56.7°C in Furnace Creek, California.",
        "The coldest temperature recorded on Earth was -89.2°C in Antarctica.",
        "Clouds can weigh more than a million pounds.",
        "A single lightning bolt is five times hotter than the surface of the sun.",
        "The windiest place on Earth is Commonwealth Bay in Antarctica."
    ]
    return render_template('weather_facts.html', facts=facts)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
