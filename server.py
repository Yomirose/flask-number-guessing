from flask import Flask, request
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(f"Generated number: {random_number}")


@app.route("/")
def number_guessing():
    return ("<div style='text-align: center'>"
            "<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"
            "<br><h2><a href='/start'>Let's begin!</a></h2></br>"
            "</div>")


@app.route("/start", methods=["GET", "POST"])
def start_game():
    if request.method == "POST":
        try:
            number = int(request.form.get("guess"))
        except (TypeError, ValueError):
            return ("<div style='text-align: center'>"
                    "<p>❌ Invalid input. Please enter a number.</p>"
                    "<a href='/start'>Try Again</a>"
                    "</div>")

        global random_number
        if number < random_number:
            return (f"<div style='text-align: center'>"
                    f"<p>Sorry, {number} is too low, try again!</p>"
                    "<img src='https://media4.giphy.com/media/6RuhlzSdhIAqk/200.webp'/>"
                    "<br><h2><a href='/start'>Play Again</a></h2></br>"
                    "</div>")
        elif number > random_number:
            return (f"<div style='text-align: center'>"
                    f"<p>Sorry, {number} is too high, try again!</p>"
                    "<img src='https://media3.giphy.com/media/cXaeWuJ1oKO4g/giphy.webp'/>"
                    "<br><h2><a href='/start'>Play Again</a></h2></br>"
                    "</div>")
        else:
            return (f"<div style='text-align: center'>"
                    f"<p>✅ Correct! {number} is the right number! 🎉</p>"
                    "<img src='https://media1.giphy.com/media/V3Z76ctCO3jG0/giphy.webp'/>"
                    "<br><h2><a href='/'>Play Again</a></h2></br>"
                    "</div>")

    # GET request (show form)
    return ("<div style='text-align: center'>"
            "<h2>Enter your guess below:</h2>"
            "<form method='POST'>"
            "<input type='number' name='guess' placeholder='Enter a number' required/>"
            "<button type='submit'>Submit</button>"
            "</form>"
            "</div>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
