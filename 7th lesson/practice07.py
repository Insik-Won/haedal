from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def introduce():
    return '저는 2021113585 컴퓨터학부 원인식입니다.'


@app.route('/me/')
def my_favorite():
    return render_template('index2.html', my_img='고양이.jpeg')


if __name__ == "__main__":
    app.run(debug=True)