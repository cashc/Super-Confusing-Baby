from flask import Flask, render_template, request
from flask_mail import Mail, Message
import random
import os
import pprint

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'troll.talk.sms'
app.config['MAIL_PASSWORD'] = 'superbaby'

mail = Mail(app)

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
INSULTS_PATH = '/assets/talk.txt'

@app.route('/', methods=['POST'])
def parse_request():

    phone_num = request.form['phone_num']
    carrier = request.form['carrier']

    msg = 'Thanks for using Troll Talk!'
    insult = get_random_insult(insults)
    htmlInsult = 'Insult sent: '+insult
    return render_template('index.html', message=msg, insult=htmlInsult)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/test')
def index():
    msg = Message('Troll Talk SMS', sender=("Troll Talk", "troll.talk.sms@gmail.com"), recipients=['2484082851@vtext.com'])
    msg.body = "I need an apology letter. Can I borrow your birth certificate?"
    mail.send(msg)
    return 'Message Sent!'

def get_insult_list():
    with open(DIR_PATH+INSULTS_PATH) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def get_random_insult(insults):
    return insults[random.randint(0, len(insults))]

def send_insult(number, carrier):
    msg = Message('Troll Talk SMS', sender=("Troll Talk", "troll.talk.sms@gmail.com"),
                  recipients=['2484082851@vtext.com'])
    msg.body = "I need an apology letter. Can I borrow your birth certificate?"
    mail.send(msg)


insults = get_insult_list()

if __name__ == '__main__':
    app.run(debug=True)