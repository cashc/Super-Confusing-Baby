from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST'])
def parse_request():
    return 'Thanks for making a POST request!'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
