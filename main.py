import os
from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')


@app.route('/')
def home():
    return render_template('index.html')


# additional contact form
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
