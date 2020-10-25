from flask import Flask
import random

app = Flask(__name__)


@app.route('/roll/<int:number>')
def roll(number):

    r = random.randint(1, 100)

    if number == r:
        return f'the number : {number} equal to the random number  the random number is {r}'

    return f'the number : {str(number)} not equal to the random number  the random number is {r}'


@app.route('/')
def index():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)
