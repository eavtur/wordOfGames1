import os
from flask import Flask, render_template
from Utils import SCORES_FILE_NAME

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, SCORES_FILE_NAME), "r") as file:
            try:
                score = int(file.read())
            except ValueError as error:
                raise error
            return render_template('index.html', SCORE=score)
    except Exception as error:
        return render_template('error.html', ERROR=error)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
