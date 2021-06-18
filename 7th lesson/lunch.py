from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/lunch/')
def lunch():
    menu = ['부대찌개.jpg', '크림파스타.jpg']
    pickme = random.choice(menu)
    return render_template('index.html', food_img=pickme)


if __name__ == "__main__":
    app.run(debug=True)