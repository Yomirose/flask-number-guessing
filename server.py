from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)
print(f"Generated number: {random_number}")

@app.route("/")
def number_guessing():
    return ("<div style='text-align: center'>"
            "<h1>Guess a number between 0 and 9 and type your guess in the URL, e.g., /3 or /7</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"
            "</div>")

@app.route(f"/<int:number>")
def number_generated(number):
    global random_number
    if number < random_number:
        return (f"<div style='text-align: center'>"
                f"<p>Sorry the {number} is too low, try again! The right  number is: {random_number}</p>"
                "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXlxb3V0bDNtMm8xYTkwNXdrb282ZnlpdHdrcnF0NGFmMWJ5NDJ2bSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/6RuhlzSdhIAqk/200.webp'/>"
                "<br><h2><a href='/' />Play Again</a></h2></br>"
                "</div>")
    elif number > random_number:
        return (f"<div style='text-align: center'>"
                f"<p>Sorry the {number} is too high, try again! The right  number is: {random_number}</p>"
                "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXlxb3V0bDNtMm8xYTkwNXdrb282ZnlpdHdrcnF0NGFmMWJ5NDJ2bSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cXaeWuJ1oKO4g/giphy.webp'/>"
                "<br><h2><a href='/' />Play Again</a></h2></br>"
                "</div>")
    else:
        return (f"<div style='text-align: center'>"
                f"<p>Correct! {number} is the right number! 🎉</p>"
                "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExanB1cm9iczY4Y20yODNudDN0YXpvaXBnYnI2OWNuYnRhd2N0NmhlciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/V3Z76ctCO3jG0/giphy.webp'/>"
                "<br><h2><a href='/' />Play Again</a></h2></br>"
                "</div>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)