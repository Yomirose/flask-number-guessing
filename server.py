from flask import Flask, request
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(f"Generated number: {random_number}")


# Common HTML wrapper for styling
def wrap_content(content):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Number Guessing Game</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
                margin: 0;
                background: #f9f9f9;
            }}
            img {{
                max-width: 100%;
                height: auto;
                border-radius: 10px;
            }}
            h1, h2, p {{
                margin: 15px 0;
            }}
            form {{
                margin-top: 20px;
            }}
            input[type=number] {{
                padding: 12px;
                font-size: 16px;
                width: 80%;
                max-width: 300px;
                margin-bottom: 10px;
            }}
            button {{
                padding: 12px 20px;
                font-size: 16px;
                background: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            button:hover {{
                background: #0056b3;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                color: #007BFF;
                font-size: 25px;
            }}
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """


@app.route("/")
def number_guessing():
    return wrap_content("""
        <h1>Guess a number between 0 and 9</h1>
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>
        <h2><a href='/start'>Let's begin!</a></h2>
    """)


@app.route("/start", methods=["GET", "POST"])
def start_game():
    global random_number
    if request.method == "POST":
        try:
            number = int(request.form.get("guess"))
        except (TypeError, ValueError):
            return wrap_content("""
                <p>❌ Invalid input. Please enter a number.</p>
                <a href='/start'>Try Again</a>
            """)

        if number < random_number:
            return wrap_content(f"""
                <p>Sorry, {number} is too low, try again!</p>
                <img src='https://media4.giphy.com/media/6RuhlzSdhIAqk/200.webp'/>
                <h2><a href='/start'>Play Again</a></h2>
            """)
        elif number > random_number:
            return wrap_content(f"""
                <p>Sorry, {number} is too high, try again!</p>
                <img src='https://media3.giphy.com/media/cXaeWuJ1oKO4g/giphy.webp'/>
                <h2><a href='/start'>Play Again</a></h2>
            """)
        else:
            random_number = random.randint(0, 9)  # reset for next round
            return wrap_content(f"""
                <p>✅ Correct! {number} is the right number! 🎉</p>
                <img src='https://media1.giphy.com/media/V3Z76ctCO3jG0/giphy.webp'/>
                <h2><a href='/'>Play Again</a></h2>
            """)

    # GET request (form)
    return wrap_content("""
        <h2>Enter your guess below:</h2>
        <form method='POST'>
            <input type='number' name='guess' placeholder='Enter a number' required/>
            <br>
            <button type='submit'>Submit</button>
        </form>
    """)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
