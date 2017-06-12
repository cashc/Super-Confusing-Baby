from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'troll.talk.sms'
app.config['MAIL_PASSWORD'] = 'superbaby'

mail = Mail(app)

@app.route('/', methods=['POST'])
def parse_request():
    return 'Thanks for making a POST request!'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/test')
def index():
    msg = Message('Hello', sender='troll.talk.sms@gmail.com', recipients=['2484082851@vtext.com'])
    mail.send(msg)
    return 'Message Sent!'

if __name__ == '__main__':
    app.run(debug=True)
