from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/training/<prof>')
def index(prof):
    file = url_for('static', filename='img/training.jpg')
    file2 = url_for('static', filename='img/training2.jpg')
    return render_template('base.html', f1=file, f2=file2, prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
